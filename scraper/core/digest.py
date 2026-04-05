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
from datetime import datetime, timedelta
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

WEEKLY_DIGEST_PROMPT = """You are a senior analyst writing a weekly tech intelligence briefing.
You will receive daily digests from the past week.
Your job is to synthesize them into a cohesive weekly overview.

Structure:
1. Executive Summary: 3-5 sentences on the week's most important developments.
2. Key Themes: recurring topics and trends that appeared across multiple days.
3. Top Stories: the 5-10 most significant stories, with context on why they matter.
4. Category Highlights: brief summary per category (AI, Security, DevTools, etc.) — only include categories with notable activity.
5. What to Watch: emerging stories or trends gaining momentum.

Format as clean Markdown. Use H2 for sections.
Focus on patterns and significance, not exhaustive coverage of every daily story.
"""

MONTHLY_DIGEST_PROMPT = """You are a senior analyst writing a monthly tech intelligence report.
You will receive weekly digests from the past month.
Your job is to synthesize them into a strategic monthly overview.

Structure:
1. Executive Summary: 3-5 sentences on the month's defining developments.
2. Major Developments: the most significant stories and shifts this month.
3. Trend Analysis: what topics gained or lost momentum compared to earlier weeks.
4. Category Deep Dive: key developments per category with month-over-month context.
5. Outlook: what trends are likely to continue or evolve.

Format as clean Markdown. Use H2 for sections.
Prioritize strategic insight over individual story details.
"""

YEARLY_DIGEST_PROMPT = """You are a senior analyst writing an annual tech intelligence review.
You will receive monthly digests from the past year.
Your job is to synthesize them into a comprehensive year-in-review.

Structure:
1. Executive Summary: the year's most defining developments in 5-7 sentences.
2. Year-Defining Stories: the top 10-15 stories that shaped the year.
3. Trend Evolution: how major themes evolved across the year (rise, peak, decline).
4. Category Review: annual summary per category with key milestones.
5. Year-over-Year Shifts: what changed fundamentally compared to the prior period.

Format as clean Markdown. Use H2 for sections.
Focus on the big picture and lasting impact, not transient news.
"""

PERIODIC_PROMPTS = {
    "weekly": WEEKLY_DIGEST_PROMPT,
    "monthly": MONTHLY_DIGEST_PROMPT,
    "yearly": YEARLY_DIGEST_PROMPT,
}

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
        return self._call_llm_with_prompt(DIGEST_PROMPT, user_content, max_retries)

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

        # Keep a copy at project root for quick access (only for today's digest)
        if date_str == datetime.now().strftime("%Y-%m-%d"):
            root_digest = self.project_root / "digest-daily.md"
            shutil.copy2(digest_path, root_digest)
            logger.info(f"Copied digest to {root_digest}")

        return str(digest_path)

    # ------------------------------------------------------------------
    # Periodic digests (weekly / monthly / yearly)
    # ------------------------------------------------------------------

    def _collect_daily_digests(self, start_date: str, end_date: str) -> List[str]:
        """Collect daily digest contents for a date range."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        digests = []

        current = start
        while current <= end:
            date_str = current.strftime("%Y-%m-%d")
            # Check both directory layouts
            candidates = [
                self.project_root / "data" / date_str / "digest.md",
                self.project_root / "data" / current.strftime("%Y-%m") / date_str / "digest.md",
            ]
            for path in candidates:
                if path.exists():
                    content = path.read_text(encoding="utf-8")
                    # Strip YAML frontmatter
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            content = parts[2].strip()
                    digests.append(f"## Daily Digest: {date_str}\n\n{content}")
                    break
            current += timedelta(days=1)

        return digests

    def _get_period_range(self, period: str, end_date: str) -> tuple:
        """Calculate start and end dates for a period.

        For auto-trigger, end_date is typically yesterday:
        - weekly (Monday trigger): end_date=Sunday -> returns Mon-Sun of that week
        - monthly (1st trigger): end_date=last day of prev month -> returns that full month
        - yearly (Jan 1 trigger): end_date=Dec 31 -> returns that full year
        """
        end = datetime.strptime(end_date, "%Y-%m-%d")

        if period == "weekly":
            # Find the Monday of the week containing end_date
            days_since_monday = end.weekday()  # Mon=0, Sun=6
            monday = end - timedelta(days=days_since_monday)
            sunday = monday + timedelta(days=6)
            return monday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")

        elif period == "monthly":
            # Full month containing end_date
            first = end.replace(day=1)
            # Find last day of month
            if end.month == 12:
                last = end.replace(day=31)
            else:
                last = end.replace(month=end.month + 1, day=1) - timedelta(days=1)
            return first.strftime("%Y-%m-%d"), last.strftime("%Y-%m-%d")

        elif period == "yearly":
            return f"{end.year}-01-01", f"{end.year}-12-31"

        return end_date, end_date

    def generate_periodic(self, period: str, end_date: Optional[str] = None, force: bool = False) -> Optional[str]:
        """Generate a periodic digest (weekly/monthly/yearly).

        Args:
            period: One of "weekly", "monthly", "yearly".
            end_date: Reference date for calculating the period range.
            force: Regenerate even if digest already exists.

        Returns:
            Path to the saved root digest file, or None on failure.
        """
        if period not in PERIODIC_PROMPTS:
            logger.error(f"Unknown period: {period}")
            return None

        if not OPENAI_AVAILABLE or self.client is None:
            logger.error("Cannot generate periodic digest: OpenAI client not initialized")
            return None

        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")

        root_path = self.project_root / f"digest-{period}.md"
        if root_path.exists() and not force:
            logger.info(f"Periodic digest already exists: {root_path}")
            return str(root_path)

        start_date, period_end = self._get_period_range(period, end_date)
        logger.info(f"Generating {period} digest for {start_date} to {period_end}")

        # For monthly/yearly, try to use higher-level digests first
        input_parts = []
        if period == "monthly":
            # Try reading weekly digests — but they live at root and get overwritten,
            # so fall back to daily digests
            input_parts = self._collect_daily_digests(start_date, period_end)
        elif period == "yearly":
            input_parts = self._collect_daily_digests(start_date, period_end)
        else:
            input_parts = self._collect_daily_digests(start_date, period_end)

        if not input_parts:
            logger.warning(f"No daily digests found for {period} period {start_date} to {period_end}")
            return None

        combined = "\n\n---\n\n".join(input_parts)
        if len(combined) > MAX_DIGEST_INPUT_CHARS:
            combined = combined[:MAX_DIGEST_INPUT_CHARS] + "\n\n[... truncated for context window ...]"

        logger.info(f"Collected {len(input_parts)} daily digests ({len(combined)} chars) for {period} digest")

        # Call LLM with period-appropriate prompt
        system_prompt = PERIODIC_PROMPTS[period]
        digest_content = self._call_llm_with_prompt(system_prompt, combined)
        if not digest_content:
            return None

        # Save to root
        frontmatter = {
            "period": period,
            "start_date": start_date,
            "end_date": period_end,
            "model": self.model_name,
            "generated_at": datetime.now().isoformat(),
            "source_count": len(input_parts),
        }

        with open(root_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, default_flow_style=False, sort_keys=False))
            f.write("---\n\n")
            f.write(digest_content)

        logger.info(f"Saved {period} digest to {root_path}")
        return str(root_path)

    def _call_llm_with_prompt(self, system_prompt: str, user_content: str, max_retries: int = 3) -> Optional[str]:
        """Send prompt to LLM with a custom system prompt."""
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content},
                    ],
                    temperature=0.3,
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                logger.warning(f"Periodic digest LLM attempt {attempt + 1} failed: {e}")
                if "model not found" in str(e).lower():
                    logger.error(f"Model '{self.model_name}' not available")
                    break
                if attempt < max_retries - 1:
                    time.sleep(10 * (2**attempt))
        return None

    def auto_generate_periodic(self, today_str: str, force: bool = False) -> None:
        """Auto-generate periodic digests based on today's date.

        Called after daily digest generation:
        - Monday: generate weekly digest for the previous week
        - 1st of month: generate monthly digest for the previous month
        - Jan 1st: generate yearly digest for the previous year
        """
        dt = datetime.strptime(today_str, "%Y-%m-%d")
        yesterday = (dt - timedelta(days=1)).strftime("%Y-%m-%d")

        if dt.weekday() == 0:  # Monday
            logger.info("Monday detected — generating weekly digest")
            self.generate_periodic("weekly", end_date=yesterday, force=force)

        if dt.day == 1:
            logger.info("1st of month detected — generating monthly digest")
            self.generate_periodic("monthly", end_date=yesterday, force=force)

        if dt.month == 1 and dt.day == 1:
            logger.info("January 1st detected — generating yearly digest")
            self.generate_periodic("yearly", end_date=yesterday, force=force)
