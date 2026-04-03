"""
Daily digest generator — synthesizes individual summaries into a single briefing.

Two-stage pipeline:
  Stage 1 (Python): Pre-cluster articles by topic, detect cross-source stories,
                     apply user preferences/blocklist.
  Stage 2 (LLM):    Synthesize the pre-organized input into a polished digest.
"""

import difflib
import logging
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from scraper.config.model_config import get_model_config
from scraper.utils.url_registry import get_url_registry

try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAI = None  # type: ignore

logger = logging.getLogger(__name__)

DIGEST_PROMPT = """You are a senior analyst writing a comprehensive daily briefing.
You will receive article summaries that have already been organized into topic sections.
Your job is to synthesize within each section — do NOT reorganize or re-categorize.

Structure:
1. Executive Summary: 3-5 sentences capturing the day's most important developments across all domains.
2. Preserve the section structure provided in the input (Top Stories, themed categories, Notable Mentions).
   For each section, synthesize the articles into a coherent narrative.
3. For each story: one-line headline with source in brackets, and 1-2 sentence synthesis.
4. If a story is marked as trending (seen_count > 1), emphasize it.
5. Keep the Notable Mentions section as a bullet list.

Format as clean Markdown. Use H2 for sections, H3 for themes. Do not use bold formatting.
Be comprehensive. Cover all the important stories rather than artificially limiting coverage.
"""

MAX_DIGEST_INPUT_CHARS = 60000
CROSS_SOURCE_SIMILARITY_THRESHOLD = 0.7


class DigestGenerator:
    """Generates a daily digest from individual article summaries."""

    def __init__(
        self,
        model_name: Optional[str] = None,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",
        timeout: float = 600.0,
    ):
        config = get_model_config()
        self.model_name = model_name or config.get_model_for_mode("digest")
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.project_root = Path(__file__).parent.parent.parent
        self.config_dir = Path(__file__).parent.parent / "config"

        if not OPENAI_AVAILABLE:
            logger.error("OpenAI library not installed")
            self.client = None
            return

        try:
            self.client = OpenAI(base_url=self.base_url, api_key=self.api_key, timeout=self.timeout)
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            self.client = None

    def generate(self, date_str: str, force: bool = False) -> Optional[str]:
        """Generate a daily digest for the given date.

        Args:
            date_str: Date in YYYY-MM-DD format.
            force: Regenerate even if digest already exists.

        Returns:
            Path to saved digest file, or None on failure.
        """
        digest_path = self.project_root / "data" / date_str / "digest.md"

        if digest_path.exists() and not force:
            logger.info(f"Digest already exists: {digest_path}")
            return str(digest_path)

        # Find summaries directory
        summary_dir = self.project_root / "data" / date_str / "summaries"
        if not summary_dir.exists():
            logger.error(f"No summaries directory for {date_str}")
            return None

        summaries = self._load_summaries(summary_dir)
        if not summaries:
            logger.error(f"No summaries found for {date_str}")
            return None

        # Get trending data from URL registry
        urls = [s["url"] for s in summaries if s.get("url")]
        trending = self._load_trending_data(urls)

        # --- Stage 1: Pre-cluster (Python, no LLM) ---
        categories = self._load_categories()
        preferences = self._load_preferences()
        summaries = self._apply_preferences(summaries, preferences)

        if not summaries:
            logger.error(f"All summaries filtered out by preferences for {date_str}")
            return None

        top_stories = self._detect_cross_source(summaries)
        categorized = self._categorize_summaries(summaries, categories)

        # --- Stage 2: Synthesize (LLM call with pre-organized input) ---
        prompt = self._build_digest_prompt(categorized, top_stories, trending, preferences)

        if not OPENAI_AVAILABLE or self.client is None:
            logger.error("Cannot generate digest: OpenAI client not initialized")
            return None

        digest_content = self._call_llm(prompt)
        if not digest_content:
            return None

        return self._save_digest(date_str, digest_content)

    # ------------------------------------------------------------------
    # Config loaders
    # ------------------------------------------------------------------

    def _load_categories(self) -> Dict[str, Any]:
        """Load category definitions from categories.yaml."""
        config_path = self.config_dir / "categories.yaml"
        if not config_path.exists():
            logger.warning("categories.yaml not found, using empty categories")
            return {}
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            return data.get("categories", {}) if isinstance(data, dict) else {}
        except Exception as e:
            logger.warning(f"Failed to load categories.yaml: {e}")
            return {}

    def _load_preferences(self) -> Dict[str, Any]:
        """Load user preferences from preferences.yaml."""
        config_path = self.config_dir / "preferences.yaml"
        if not config_path.exists():
            return self._default_preferences()
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if not isinstance(data, dict):
                return self._default_preferences()
            return data
        except Exception as e:
            logger.warning(f"Failed to load preferences.yaml: {e}")
            return self._default_preferences()

    @staticmethod
    def _default_preferences() -> Dict[str, Any]:
        """Return default preferences when preferences.yaml is missing."""
        return {
            "blocklist": {"keywords": [], "domains": []},
            "min_score": {},
            "digest": {"max_stories_per_section": 8, "show_notable_mentions": True},
        }

    # ------------------------------------------------------------------
    # Stage 1: Pre-clustering helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _categorize_summaries(summaries: List[Dict], categories: Dict[str, Any]) -> Dict[str, List[Dict]]:
        """Score each summary against categories by keyword overlap.

        Returns a dict mapping category keys to lists of summaries.
        Articles that don't match any category go to 'uncategorized'.
        """
        result: Dict[str, List[Dict]] = {}

        for s in summaries:
            searchable = (s.get("title", "") + " " + s.get("body", "")).lower()
            best_cat = "uncategorized"
            best_score = 0

            for cat_key, cat_def in categories.items():
                keywords = cat_def.get("keywords", [])
                score = sum(1 for kw in keywords if kw.lower() in searchable)
                if score > best_score:
                    best_score = score
                    best_cat = cat_key

            result.setdefault(best_cat, []).append(s)

        return result

    @staticmethod
    def _detect_cross_source(summaries: List[Dict]) -> List[List[Dict]]:
        """Detect stories that appear across multiple sources.

        Uses difflib.SequenceMatcher on titles: ratio > threshold = same story.
        Returns a list of groups, each group being a list of matching summaries.
        """
        used: set = set()
        groups: List[List[Dict]] = []

        for i, a in enumerate(summaries):
            if i in used:
                continue
            group = [a]
            for j, b in enumerate(summaries):
                if j <= i or j in used:
                    continue
                # Skip if same source
                if a.get("site") == b.get("site"):
                    continue
                ratio = difflib.SequenceMatcher(None, a.get("title", "").lower(), b.get("title", "").lower()).ratio()
                if ratio >= CROSS_SOURCE_SIMILARITY_THRESHOLD:
                    group.append(b)
                    used.add(j)
            if len(group) > 1:
                used.add(i)
                groups.append(group)

        return groups

    @staticmethod
    def _apply_preferences(summaries: List[Dict], preferences: Dict[str, Any]) -> List[Dict]:
        """Filter summaries based on user preferences (blocklist)."""
        blocklist = preferences.get("blocklist", {})
        blocked_keywords = [kw.lower() for kw in blocklist.get("keywords", [])]
        blocked_domains = [d.lower() for d in blocklist.get("domains", [])]

        if not blocked_keywords and not blocked_domains:
            return summaries

        filtered = []
        for s in summaries:
            searchable = (s.get("title", "") + " " + s.get("body", "")).lower()
            url = s.get("url", "").lower()

            if any(kw in searchable for kw in blocked_keywords):
                continue
            if any(domain in url for domain in blocked_domains):
                continue
            filtered.append(s)

        return filtered

    # ------------------------------------------------------------------
    # Summary loading & parsing
    # ------------------------------------------------------------------

    def _load_summaries(self, summary_dir: Path) -> List[Dict]:
        """Load and parse all summary files from a directory."""
        summaries = []
        for md_file in sorted(summary_dir.glob("*.md")):
            try:
                text = md_file.read_text(encoding="utf-8")
                meta, body = self._parse_frontmatter(text)

                summaries.append(
                    {
                        "title": meta.get("title", md_file.stem),
                        "url": meta.get("url", ""),
                        "site": meta.get("site", "unknown"),
                        "body": body,
                    }
                )
            except Exception as e:
                logger.warning(f"Failed to parse {md_file.name}: {e}")
        return summaries

    @staticmethod
    def _parse_frontmatter(text: str) -> tuple:
        """Parse YAML frontmatter, falling back to line-by-line on YAML errors.

        Handles unquoted colons in values (common in titles like
        'GitHub - user/repo: description').
        """
        if not text.startswith("---"):
            return {}, text

        parts = text.split("---", 2)
        if len(parts) < 3:
            return {}, text

        raw_fm, body = parts[1], parts[2].strip()

        # Try standard YAML first
        try:
            meta = yaml.safe_load(raw_fm)
            if isinstance(meta, dict):
                return meta, body
        except yaml.YAMLError:
            pass

        # Fallback: parse key: value line-by-line, treating first colon as separator
        fallback_meta: Dict[str, str] = {}
        for line in raw_fm.strip().splitlines():
            colon_idx = line.find(":")
            if colon_idx > 0:
                key = line[:colon_idx].strip()
                val = line[colon_idx + 1 :].strip()
                fallback_meta[key] = val
        return fallback_meta, body

    # ------------------------------------------------------------------
    # Trending data
    # ------------------------------------------------------------------

    def _load_trending_data(self, urls: List[str]) -> Dict[str, int]:
        """Get seen_count for each URL from the URL registry."""
        try:
            registry = get_url_registry(str(self.project_root))
            trending = {}
            for url in urls:
                entry = registry.get_entry(url)
                if entry and entry.get("seen_count", 1) > 1:
                    trending[url] = entry["seen_count"]
            return trending
        except Exception as e:
            logger.warning(f"Could not load trending data: {e}")
            return {}

    # ------------------------------------------------------------------
    # Stage 2: Prompt building
    # ------------------------------------------------------------------

    def _build_digest_prompt(
        self,
        categorized: Dict[str, List[Dict]],
        top_stories: List[List[Dict]],
        trending: Dict[str, int],
        preferences: Dict[str, Any],
    ) -> str:
        """Build the user-content portion of the digest prompt with pre-clustered input."""
        categories_config = self._load_categories()
        max_per_section = preferences.get("digest", {}).get("max_stories_per_section", 8)
        show_notable = preferences.get("digest", {}).get("show_notable_mentions", True)
        parts: List[str] = []

        # --- Top Stories (cross-source) ---
        if top_stories:
            top_lines = ["## TOP STORIES (appeared across multiple sources)"]
            for group in top_stories:
                sources = ", ".join(s.get("site", "unknown") for s in group)
                primary = group[0]
                header = f"- {primary.get('title', 'Untitled')} [Sources: {sources}]"
                if primary.get("url") and primary["url"] in trending:
                    header += f" (trending: seen {trending[primary['url']]}x)"
                top_lines.append(header)
            parts.append("\n".join(top_lines))

        # Collect URLs used in top stories to avoid duplication
        top_story_urls: set = set()
        for group in top_stories:
            for s in group:
                if s.get("url"):
                    top_story_urls.add(s["url"])

        # --- Categorized sections ---
        # Ordered: known categories first, then uncategorized
        ordered_keys = [k for k in categories_config if k in categorized]
        if "uncategorized" in categorized:
            ordered_keys.append("uncategorized")

        notable_mentions: List[str] = []

        for cat_key in ordered_keys:
            cat_summaries = categorized[cat_key]
            # Remove articles already in top stories
            cat_summaries = [s for s in cat_summaries if s.get("url") not in top_story_urls]
            if not cat_summaries:
                continue

            label = categories_config.get(cat_key, {}).get("label", cat_key.replace("_", " ").title())

            # Cap per section; overflow goes to notable mentions
            main_batch = cat_summaries[:max_per_section]
            overflow = cat_summaries[max_per_section:]

            section_lines = [f"## {label} ({len(main_batch)} articles)"]
            for s in main_batch:
                header = f"### {s['title']} [{s['site']}]"
                if s.get("url") and s["url"] in trending:
                    header += f" (trending: seen {trending[s['url']]}x)"
                body = s["body"][:3000] if len(s["body"]) > 3000 else s["body"]
                section_lines.append(f"{header}\n{body}")

            parts.append("\n\n".join(section_lines))

            if show_notable and overflow:
                for s in overflow:
                    notable_mentions.append(f"- {s['title']} [{s['site']}]")

        # --- Notable Mentions ---
        if show_notable and notable_mentions:
            parts.append("## Notable Mentions\n" + "\n".join(notable_mentions))

        combined = "\n\n---\n\n".join(parts)
        # Truncate total input
        if len(combined) > MAX_DIGEST_INPUT_CHARS:
            combined = combined[:MAX_DIGEST_INPUT_CHARS] + "\n\n[... truncated for context window ...]"
        return combined

    # ------------------------------------------------------------------
    # LLM call & save
    # ------------------------------------------------------------------

    def _call_llm(self, user_content: str, max_retries: int = 3) -> Optional[str]:
        """Send prompt to LLM and return the digest text."""
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": DIGEST_PROMPT},
                        {"role": "user", "content": user_content},
                    ],
                    temperature=0.3,
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                logger.warning(f"Digest LLM attempt {attempt + 1} failed: {e}")
                if "model not found" in str(e).lower():
                    logger.error(f"Model '{self.model_name}' not available. Pull it with: ollama pull {self.model_name}")
                    break
                if attempt < max_retries - 1:
                    time.sleep(10 * (2**attempt))
        return None

    def _save_digest(self, date_str: str, content: str) -> str:
        """Save digest with YAML frontmatter."""
        digest_dir = self.project_root / "data" / date_str
        digest_dir.mkdir(parents=True, exist_ok=True)
        digest_path = digest_dir / "digest.md"

        frontmatter = {
            "date": date_str,
            "model": self.model_name,
            "generated_at": datetime.now().isoformat(),
        }

        with open(digest_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, default_flow_style=False, sort_keys=False))
            f.write("---\n\n")
            f.write(content)

        logger.info(f"Saved digest to {digest_path}")

        # Keep a copy at project root for quick access
        root_digest = self.project_root / "digest.md"
        shutil.copy2(digest_path, root_digest)
        logger.info(f"Copied digest to {root_digest}")

        return str(digest_path)
