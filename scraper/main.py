#!/usr/bin/env python3
"""
Market Intelligence Scraper - Single entry point for all commands.
"""

import logging
import sys
from datetime import datetime, timedelta
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich.table import Table

from scraper.config.model_config import get_model_config
from scraper.core.ai_processor import summarize_content, summarize_with_anthropic
from scraper.core.data_organizer import DataOrganizer
from scraper.core.scraper_registry import ScraperRegistry
from scraper.core.scraper_runner import run_scraper
from scraper.utils.health_check import HealthStatus, run_health_check

console = Console()


@click.group()
def cli():
    """Market Intelligence Scraper - Collect and analyze trending tech content."""


@cli.command()
@click.option("--quiet", "-q", is_flag=True, help="Suppress non-essential output (errors only)")
def scrape(quiet):
    """Scrape content from tech sites."""
    log_level = logging.ERROR if quiet else logging.INFO
    logging.basicConfig(level=log_level, format="%(message)s", force=True)
    # Suppress verbose output from noisy modules
    if not quiet:
        logging.getLogger("selenium").setLevel(logging.ERROR)
        logging.getLogger("urllib3").setLevel(logging.ERROR)
    scraper_names = [
        "github",
        "hackernews_api",
        "devto",
        "reddit",
        "reddit_optimized",
        "tldr",
        "hnrss",
        "newsfeed",
    ]
    mode_text = "Scraping 8 sources"
    scrapers = ScraperRegistry.get_scrapers_for_names(scraper_names)
    success = 0
    if quiet:
        # Simple execution without progress
        for scraper_class in scrapers:
            try:
                if run_scraper(scraper_class, "json", dry_run=False, fetch_content=True):
                    success += 1
            except Exception:
                pass
    else:
        # Rich progress display
        console.print(Panel(mode_text, style="bold blue"))
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Scraping sources...", total=len(scrapers))
            for scraper_class in scrapers:
                name = scraper_class.__name__
                progress.update(task, description=f"[cyan]Scraping {name}...")
                try:
                    if run_scraper(scraper_class, "json", dry_run=False, fetch_content=True):
                        success += 1
                        progress.console.print(f"  ✅ {name} succeeded")
                    else:
                        progress.console.print(f"  ❌ {name} failed")
                except Exception as e:
                    progress.console.print(f"  ❌ {name} failed: {str(e)}")
                progress.update(task, advance=1)
        # Summary
        if success == len(scrapers):
            console.print(f"\n[bold green]✅ Perfect! All {success} scrapers succeeded.[/bold green]")
        elif success > 0:
            console.print(f"\n[bold yellow]✅ Done. {success}/{len(scrapers)} scrapers succeeded.[/bold yellow]")
        else:
            console.print("\n[bold red]❌ All scrapers failed.[/bold red]")
    sys.exit(0 if success > 0 else 1)


def get_available_dates(data_dir):
    """Get list of available date directories with content."""
    available_dates = []
    for item in data_dir.iterdir():
        if item.is_dir():
            try:
                datetime.strptime(item.name, "%Y-%m-%d")
                content_dir = item / "content"
                if content_dir.exists() and list(content_dir.glob("*.md")):
                    available_dates.append(item.name)
            except ValueError:
                continue
    return sorted(available_dates, reverse=True)


@cli.command()
@click.option("--date", help="Date to summarize (YYYY-MM-DD). Default: today")
@click.option("--days-back", type=int, default=0, help="Summarize content from N days ago")
@click.option("--list-dates", is_flag=True, help="List available dates with content")
@click.option("--dry-run", is_flag=True, help="Show what would be done without summarizing")
@click.option("--force", is_flag=True, help="Force re-summarization even if summaries exist")
@click.option("--max-files", type=int, default=0, help="Maximum files to summarize (0 = all)")
@click.option("--model", default=None, help="Model to use (e.g. tinyllama:latest for fast models, llama3.2:1b for quality)")
@click.option("--quiet", "-q", is_flag=True, help="Suppress non-essential output (errors only)")
def summarize(
    date,
    days_back,
    list_dates,
    dry_run,
    force,
    max_files,
    model,
    quiet,
):
    """Summarize content for a single date."""
    log_level = logging.ERROR if quiet else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True,
    )
    # Suppress verbose output from modules
    logging.getLogger("scraper").setLevel(logging.ERROR)
    logging.getLogger("scraper.core.ai_processor").setLevel(logging.ERROR)
    logging.getLogger("scraper.utils.summarizer").setLevel(logging.ERROR)
    logging.getLogger("httpx").setLevel(logging.ERROR)
    logging.getLogger("httpcore").setLevel(logging.ERROR)
    logging.getLogger("openai").setLevel(logging.ERROR)
    logging.getLogger(__name__)
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"
    if list_dates:
        available_dates = get_available_dates(data_dir)
        if available_dates:
            if not quiet:
                # Rich table display
                table = Table(title="Available Dates with Content")
                table.add_column("Date", style="cyan")
                table.add_column("Files", style="green")
                for date in available_dates:
                    content_dir = data_dir / date / "content"
                    file_count = len(list(content_dir.glob("*.md")))
                    table.add_row(date, str(file_count))
                console.print(table)
            else:
                # In quiet mode, just print the dates
                for date in available_dates:
                    print(date)
        else:
            if not quiet:
                console.print("[yellow]No dates with content found[/yellow]")
        return
    # Determine date
    if days_back > 0:
        target_date = datetime.now() - timedelta(days=days_back)
        date_str = target_date.strftime("%Y-%m-%d")
    else:
        date_str = date or datetime.now().strftime("%Y-%m-%d")
    # Validate date format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        if not quiet:
            console.print(f"[red]Invalid date format: {date_str}. Use YYYY-MM-DD[/red]")
        sys.exit(1)
    # Check content directory
    content_dir = data_dir / date_str / "content"
    if not content_dir.exists():
        if not quiet:
            console.print(f"[red]No content directory found for {date_str}[/red]")
        if not quiet:
            console.print("[yellow]Use --list-dates to see available dates[/yellow]")
            available_dates = get_available_dates(data_dir)
            if available_dates:
                console.print(f"[green]Most recent date with content: {available_dates[0]}[/green]")
                console.print(f"[cyan]Run: poetry run scraper summarize --date {available_dates[0]}[/cyan]")
        sys.exit(1)
    content_files = list(content_dir.glob("*.md"))
    if not content_files:
        if not quiet:
            console.print(f"[red]No content files found in {content_dir}[/red]")
        if not quiet:
            console.print("[yellow]Did you run 'poetry run scraper scrape' first?[/yellow]")
        sys.exit(1)
    if not quiet:
        console.print(f"[green]Found {len(content_files)} content files for {date_str}[/green]")
    # Check for existing summaries
    data_organizer = DataOrganizer()
    summary_dir = data_organizer.ensure_directory(date_str, "summaries")
    if summary_dir.exists() and not force:
        existing_summaries = list(summary_dir.glob("*.md"))
        if existing_summaries:
            if not quiet:
                console.print(f"[yellow]Found {len(existing_summaries)} existing summaries[/yellow]")
                console.print("[cyan]Use --force to re-summarize[/cyan]")
            if not dry_run:
                return
    if dry_run:
        if not quiet:
            panel_content = f"""[bold]DRY RUN MODE[/bold]
Date: {date_str}
Content directory: {content_dir}
Summary directory: {summary_dir}
Model: {model}
Max files: {max_files or "all"}
Sample content files:"""
            for i, f in enumerate(content_files[:5]):
                panel_content += f"\n  - {f.name}"
            if len(content_files) > 5:
                panel_content += f"\n  ... and {len(content_files) - 5} more"
            console.print(Panel(panel_content, style="yellow"))
        return
    try:
        if quiet:
            # No progress for quiet mode
            success, summary_files = summarize_content(
                date_dir=date_str,
                model_name=model,
                max_files=max_files,
                fallback_model=None,  # Will use config default
            )
        else:
            # Rich progress display for summarization
            with Progress(
                SpinnerColumn(),
                BarColumn(),
                TaskProgressColumn(),
                TimeRemainingColumn(),
                TextColumn(" • "),
                TextColumn("[cyan]{task.fields[filename]}", style="cyan"),
                console=console,
            ) as progress:
                task = progress.add_task(
                    "[cyan]Summarizing...",
                    total=len(content_files),
                    filename=f"Starting ({len(content_files)} files total)",
                )

                def progress_callback(current, total, filename):
                    # Truncate filename if too long
                    if len(filename) > 50:
                        filename = filename[:47] + "..."
                    progress.update(task, completed=current, filename=filename)

                success, summary_files = summarize_content(
                    date_dir=date_str,
                    model_name=model,
                    max_files=max_files,
                    fallback_model=None,  # Will use config default
                    progress_callback=progress_callback,
                )
                progress.update(task, completed=len(content_files))
        if success:
            if not quiet:
                console.print(f"\n[bold green]✅ Successfully created {len(summary_files)} summaries[/bold green]")
        else:
            if not quiet:
                console.print("\n[bold red]❌ Summarization failed[/bold red]")
            sys.exit(1)
    except Exception as e:
        if not quiet:
            console.print(f"\n[bold red]❌ Summarization error: {str(e)}[/bold red]")
        sys.exit(1)


def get_dates_to_process(data_dir, days_back=7, start_date=None, end_date=None):
    """Get list of dates to process for batch summarization."""
    dates_to_process = []
    if start_date and end_date:
        current = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        while current <= end:
            date_str = current.strftime("%Y-%m-%d")
            content_dir = data_dir / date_str / "content"
            if content_dir.exists() and list(content_dir.glob("*.md")):
                dates_to_process.append(date_str)
            current += timedelta(days=1)
    else:
        for i in range(days_back):
            date = datetime.now() - timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            content_dir = data_dir / date_str / "content"
            if content_dir.exists() and list(content_dir.glob("*.md")):
                dates_to_process.append(date_str)
    return sorted(dates_to_process)


@cli.command("summarize-batch")
@click.option("--days-back", type=int, default=7, help="Process last N days (default: 7)")
@click.option("--start-date", help="Start date for range (YYYY-MM-DD)")
@click.option("--end-date", help="End date for range (YYYY-MM-DD)")
@click.option("--dry-run", is_flag=True, help="Show what would be done")
@click.option("--skip-existing", is_flag=True, help="Skip dates with existing summaries")
@click.option("--max-files-per-date", type=int, default=0, help="Max files per date (0 = all)")
@click.option("--model", default=None, help="Model to use (e.g. tinyllama:latest for fast models, llama3.2:1b for quality)")
@click.option("--quiet", "-q", is_flag=True, help="Suppress non-essential output (errors only)")
def summarize_batch(
    days_back,
    start_date,
    end_date,
    dry_run,
    skip_existing,
    max_files_per_date,
    model,
    quiet,
):
    """Summarize content for multiple dates."""
    log_level = logging.ERROR if quiet else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True,
    )
    # Suppress verbose output from modules
    logging.getLogger("scraper").setLevel(logging.ERROR)
    logging.getLogger("scraper.core.ai_processor").setLevel(logging.ERROR)
    logging.getLogger("scraper.utils.summarizer").setLevel(logging.ERROR)
    logging.getLogger("httpx").setLevel(logging.ERROR)
    logging.getLogger("httpcore").setLevel(logging.ERROR)
    logging.getLogger("openai").setLevel(logging.ERROR)
    logging.getLogger(__name__)
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"
    dates = get_dates_to_process(
        data_dir,
        days_back=days_back,
        start_date=start_date,
        end_date=end_date,
    )
    if not dates:
        if not quiet:
            console.print("[yellow]No dates found with content to process[/yellow]")
        sys.exit(1)
    total_summaries = 0
    successful_dates = 0
    if quiet:
        # Simple execution without progress
        for date_str in dates:
            content_dir = data_dir / date_str / "content"
            content_files = list(content_dir.glob("*.md"))
            if skip_existing:
                summary_dir = data_dir / date_str / "summaries"
                if summary_dir.exists() and list(summary_dir.glob("*.md")):
                    continue
            if dry_run:
                continue
            try:
                success, summary_files = summarize_content(
                    date_dir=date_str,
                    model_name=model,
                    max_files=max_files_per_date,
                    fallback_model=None,  # Will use config default
                )
                if success:
                    total_summaries += len(summary_files)
                    successful_dates += 1
            except Exception:
                pass
    else:
        # Rich progress display
        console.print(f"[bold cyan]Found {len(dates)} dates to process[/bold cyan]")
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Processing dates...", total=len(dates))
            for date_str in dates:
                progress.update(task, description=f"[cyan]Processing {date_str}...")
                content_dir = data_dir / date_str / "content"
                content_files = list(content_dir.glob("*.md"))
                if skip_existing:
                    summary_dir = data_dir / date_str / "summaries"
                    if summary_dir.exists() and list(summary_dir.glob("*.md")):
                        progress.console.print(f"  🔄 {date_str} - skipped (summaries exist)")
                        progress.update(task, advance=1)
                        continue
                if dry_run:
                    progress.console.print(f"  🔍 {date_str} - would summarize {len(content_files)} files")
                    progress.update(task, advance=1)
                    continue
                try:
                    success, summary_files = summarize_content(
                        date_dir=date_str,
                        model_name=model,
                        max_files=max_files_per_date,
                        fallback_model=None,  # Will use config default
                    )
                    if success:
                        progress.console.print(f"  ✅ {date_str} - created {len(summary_files)} summaries")
                        total_summaries += len(summary_files)
                        successful_dates += 1
                    else:
                        progress.console.print(f"  ❌ {date_str} - failed")
                except Exception as e:
                    progress.console.print(f"  ❌ {date_str} - error: {str(e)}")
                progress.update(task, advance=1)
        # Summary panel
        summary_text = f"""[bold]BATCH SUMMARY[/bold]
Dates processed: {successful_dates}/{len(dates)}
Total summaries created: {total_summaries}"""
        if successful_dates == len(dates):
            console.print(Panel(summary_text, style="green", border_style="green"))
        elif successful_dates > 0:
            console.print(Panel(summary_text, style="yellow", border_style="yellow"))
        else:
            console.print(Panel(summary_text, style="red", border_style="red"))
    sys.exit(0 if successful_dates > 0 else 1)


@cli.command("summarize-anthropic")
@click.option("--date", help="Date to summarize (YYYY-MM-DD). Default: today")
@click.option("--days-back", type=int, default=0, help="Summarize content from N days ago")
@click.option("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY env var)")
@click.option("--model", default=None, help="Claude model to use (defaults to config setting)")
@click.option("--max-files", type=int, default=0, help="Maximum files to summarize (0 = all)")
@click.option("--quiet", "-q", is_flag=True, help="Suppress non-essential output (errors only)")
def summarize_anthropic(date, days_back, api_key, model, max_files, quiet):
    """Summarize content using Anthropic's Claude API."""
    log_level = logging.ERROR if quiet else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True,
    )

    # Suppress verbose output from modules
    logging.getLogger("scraper").setLevel(logging.ERROR)
    logging.getLogger("httpx").setLevel(logging.ERROR)
    logging.getLogger("httpcore").setLevel(logging.ERROR)

    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"

    # Determine date
    if days_back > 0:
        target_date = datetime.now() - timedelta(days=days_back)
        date_str = target_date.strftime("%Y-%m-%d")
    else:
        date_str = date or datetime.now().strftime("%Y-%m-%d")

    # Validate date format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        if not quiet:
            console.print(f"[red]Invalid date format: {date_str}. Use YYYY-MM-DD[/red]")
        sys.exit(1)

    # Check content directory
    content_dir = data_dir / date_str / "content"
    if not content_dir.exists():
        if not quiet:
            console.print(f"[red]No content directory found for {date_str}[/red]")
        sys.exit(1)

    content_files = list(content_dir.glob("*.md"))
    if not content_files:
        if not quiet:
            console.print(f"[red]No content files found in {content_dir}[/red]")
        sys.exit(1)

    if not quiet:
        console.print(f"[green]Found {len(content_files)} content files for {date_str}[/green]")
        console.print(Panel("[bold cyan]STARTING ANTHROPIC SUMMARIZATION[/bold cyan]", style="cyan"))

    try:
        if quiet:
            # No progress for quiet mode
            success, summary_files = summarize_with_anthropic(
                date_dir=date_str,
                api_key=api_key,
                model=model,
                max_files=max_files,
            )
        else:
            # Rich progress display
            with Progress(
                SpinnerColumn(),
                BarColumn(),
                TaskProgressColumn(),
                TimeRemainingColumn(),
                TextColumn(" • "),
                TextColumn("[cyan]{task.fields[filename]}", style="cyan"),
                console=console,
            ) as progress:
                task = progress.add_task(
                    "[cyan]Summarizing...",
                    total=len(content_files),
                    filename=f"Starting ({len(content_files)} files total)",
                )

                def progress_callback(current, total, filename):
                    # Truncate filename if too long
                    if len(filename) > 50:
                        filename = filename[:47] + "..."
                    progress.update(task, completed=current, filename=filename)

                success, summary_files = summarize_with_anthropic(
                    date_dir=date_str,
                    api_key=api_key,
                    model=model,
                    max_files=max_files,
                    progress_callback=progress_callback,
                )

                progress.update(task, completed=len(content_files))

        if success:
            if not quiet:
                console.print(f"\n[bold green]✅ Successfully created {len(summary_files)} Anthropic summaries[/bold green]")
        else:
            if not quiet:
                console.print("\n[bold red]❌ Anthropic summarization failed[/bold red]")
            sys.exit(1)
    except Exception as e:
        if not quiet:
            console.print(f"\n[bold red]❌ Anthropic summarization error: {str(e)}[/bold red]")
        sys.exit(1)


@cli.command()
@click.option("--date", help="Date to generate digest for (YYYY-MM-DD). Default: most recent with summaries")
@click.option("--days-back", type=int, default=0, help="Generate digest for N days ago")
@click.option("--model", default=None, help="Model to use (e.g. gemma3:27b)")
@click.option("--force", is_flag=True, help="Force regeneration even if digest exists")
@click.option("--quiet", "-q", is_flag=True, help="Suppress non-essential output (errors only)")
def digest(date, days_back, model, force, quiet):
    """Generate a daily digest from individual summaries."""
    log_level = logging.ERROR if quiet else logging.WARNING
    logging.basicConfig(level=log_level, format="%(message)s", force=True)
    logging.getLogger("scraper").setLevel(logging.ERROR)
    logging.getLogger("httpx").setLevel(logging.ERROR)
    logging.getLogger("httpcore").setLevel(logging.ERROR)
    logging.getLogger("openai").setLevel(logging.ERROR)

    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"

    # Determine date
    if days_back > 0:
        target_date = datetime.now() - timedelta(days=days_back)
        date_str = target_date.strftime("%Y-%m-%d")
    elif date:
        date_str = date
    else:
        # Find most recent date with summaries
        available = get_available_dates(data_dir)
        found = None
        for d in available:
            summary_dir = data_dir / d / "summaries"
            if summary_dir.exists() and list(summary_dir.glob("*.md")):
                found = d
                break
        if not found:
            if not quiet:
                console.print("[red]No dates with summaries found[/red]")
            sys.exit(1)
        date_str = found

    # Validate
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        if not quiet:
            console.print(f"[red]Invalid date format: {date_str}. Use YYYY-MM-DD[/red]")
        sys.exit(1)

    summary_dir = data_dir / date_str / "summaries"
    if not summary_dir.exists() or not list(summary_dir.glob("*.md")):
        if not quiet:
            console.print(f"[red]No summaries found for {date_str}[/red]")
        sys.exit(1)

    if not quiet:
        summary_count = len(list(summary_dir.glob("*.md")))
        console.print(f"[cyan]Generating digest for {date_str} ({summary_count} summaries)[/cyan]")

    from scraper.core.digest import DigestGenerator

    generator = DigestGenerator(model_name=model)

    if not quiet:
        console.print(f"[cyan]Using model: {generator.model_name}[/cyan]")

    result = generator.generate(date_str, force=force)

    if result:
        if not quiet:
            console.print(f"\n[bold green]Digest saved to {result}[/bold green]")
    else:
        if not quiet:
            console.print("\n[bold red]Digest generation failed[/bold red]")
        sys.exit(1)


@cli.command()
@click.option("--model", default=None, help="Model to use for digest generation")
@click.option("--no-push", is_flag=True, help="Skip git push after generating digest")
@click.option("--quiet", "-q", is_flag=True, help="Suppress non-essential output (errors only)")
def morning(model, no_push, quiet):
    """Morning workflow: git pull, generate digest, git push."""
    import subprocess

    log_level = logging.ERROR if quiet else logging.INFO
    logging.basicConfig(level=log_level, format="%(message)s", force=True)
    if not quiet:
        logging.getLogger("selenium").setLevel(logging.ERROR)
        logging.getLogger("urllib3").setLevel(logging.ERROR)

    project_root = Path(__file__).parent.parent

    # Step 1: git pull
    if not quiet:
        console.print("Pulling latest changes...")
    result = subprocess.run(["git", "pull", "--rebase", "origin", "master"], cwd=str(project_root), capture_output=True, text=True)
    if result.returncode != 0:
        if not quiet:
            console.print(f"git pull failed: {result.stderr.strip()}")
        sys.exit(1)
    if not quiet:
        console.print(f"  {result.stdout.strip()}")

    # Step 2: Scrape + summarize today if no data exists yet
    data_dir = project_root / "data"
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_content = data_dir / today_str / "content"
    today_summaries = data_dir / today_str / "summaries"

    if not today_content.exists() or not list(today_content.glob("*.md")):
        if not quiet:
            console.print(f"[cyan]No content for {today_str}, scraping...[/cyan]")
        scraper_names = ["github", "hackernews_api", "devto", "reddit", "reddit_optimized", "tldr", "hnrss", "newsfeed"]
        scrapers = ScraperRegistry.get_scrapers_for_names(scraper_names)
        scrape_ok = 0
        for scraper_class in scrapers:
            try:
                if run_scraper(scraper_class, "json", dry_run=False, fetch_content=True):
                    scrape_ok += 1
            except Exception:
                pass
        if scrape_ok == 0:
            if not quiet:
                console.print("[red]All scrapers failed[/red]")
            sys.exit(1)
        if not quiet:
            console.print(f"[green]Scraped {scrape_ok}/{len(scrapers)} sources[/green]")

    if not today_summaries.exists() or not list(today_summaries.glob("*.md")):
        if not quiet:
            console.print(f"[cyan]No summaries for {today_str}, summarizing...[/cyan]")
        success, summary_files = summarize_content(date_dir=today_str, model_name=None, max_files=0, fallback_model=None)
        if not success:
            if not quiet:
                console.print("[red]Summarization failed[/red]")
            sys.exit(1)
        if not quiet:
            console.print(f"[green]Created {len(summary_files)} summaries[/green]")

    # Find most recent date with summaries (should be today now)
    available = get_available_dates(data_dir)
    date_str = None
    for d in available:
        summary_dir = data_dir / d / "summaries"
        if summary_dir.exists() and list(summary_dir.glob("*.md")):
            date_str = d
            break

    if not date_str:
        if not quiet:
            console.print("[red]No dates with summaries found[/red]")
        sys.exit(1)

    if not quiet:
        console.print(f"[cyan]Generating digest for {date_str}...[/cyan]")

    # Step 3: Generate digest
    from scraper.core.digest import DigestGenerator

    generator = DigestGenerator(model_name=model)
    if not quiet:
        console.print(f"[cyan]Using model: {generator.model_name}[/cyan]")

    digest_path = generator.generate(date_str, force=True)
    if not digest_path:
        if not quiet:
            console.print("[red]Digest generation failed[/red]")
        sys.exit(1)

    if not quiet:
        console.print(f"[green]Digest saved to {digest_path}[/green]")

    # Step 4: git add, commit, push
    subprocess.run(["git", "add", "data/"], cwd=str(project_root), capture_output=True, text=True)

    # Check if there's anything to commit
    status = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=str(project_root), capture_output=True)
    if status.returncode == 0:
        if not quiet:
            console.print("No changes to commit")
        return

    commit_msg = f"Add daily digest for {date_str}"
    commit_result = subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(project_root), capture_output=True, text=True)
    if commit_result.returncode != 0:
        if not quiet:
            console.print(f"git commit failed: {commit_result.stderr.strip()}")
        sys.exit(1)
    if not quiet:
        console.print(f"Committed: {commit_msg}")

    if no_push:
        if not quiet:
            console.print("Skipping push (--no-push)")
        return

    # Pull again before push in case CI pushed while we were working
    pull2 = subprocess.run(["git", "pull", "--rebase", "origin", "master"], cwd=str(project_root), capture_output=True, text=True)
    if pull2.returncode != 0:
        if not quiet:
            console.print(f"git pull before push failed: {pull2.stderr.strip()}")
        sys.exit(1)

    push_result = subprocess.run(["git", "push", "origin", "master"], cwd=str(project_root), capture_output=True, text=True)
    if push_result.returncode != 0:
        if not quiet:
            console.print(f"git push failed: {push_result.stderr.strip()}")
        sys.exit(1)
    if not quiet:
        console.print("Pushed to origin/master")


@cli.command()
@click.option("-v", "--verbose", is_flag=True, help="Show detailed health check information")
@click.option("--strict", is_flag=True, help="Exit with error if any check fails")
@click.option("--json", is_flag=True, help="Output results as JSON")
def health(verbose, strict, json):
    """Check system health and dependencies."""
    overall_status, results = run_health_check(verbose=verbose and not json)
    if json:
        import json as json_module

        output = {
            "overall_status": overall_status.value,
            "checks": [r.to_dict() for r in results],
        }
        print(json_module.dumps(output, indent=2))
    else:
        # Rich display for health checks
        if verbose:
            # Detailed table view
            table = Table(title="Health Check Results")
            table.add_column("Check", style="cyan")
            table.add_column("Status", style="bold")
            table.add_column("Message")
            for r in results:
                if r.status == HealthStatus.HEALTHY:
                    status_text = "[green]✅ HEALTHY[/green]"
                elif r.status == HealthStatus.DEGRADED:
                    status_text = "[yellow]⚠️  DEGRADED[/yellow]"
                else:
                    status_text = "[red]❌ UNHEALTHY[/red]"
                table.add_row(r.name, status_text, r.message)
            console.print(table)
        else:
            # Simple status display
            if overall_status == HealthStatus.HEALTHY:
                console.print("[bold green]✅ All health checks passed[/bold green]")
            elif overall_status == HealthStatus.DEGRADED:
                console.print("[bold yellow]⚠️  Some health checks degraded[/bold yellow]")
                failed = [r for r in results if r.status != HealthStatus.HEALTHY]
                for r in failed:
                    console.print(f"  [yellow]- {r.name}: {r.message}[/yellow]")
            else:
                console.print("[bold red]❌ Health checks failed[/bold red]")
                failed = [r for r in results if r.status == HealthStatus.UNHEALTHY]
                for r in failed:
                    console.print(f"  [red]- {r.name}: {r.message}[/red]")
    if strict and overall_status != HealthStatus.HEALTHY:
        sys.exit(1)
    elif overall_status == HealthStatus.UNHEALTHY:
        sys.exit(1)


def main():
    """Main entry point."""
    cli()


if __name__ == "__main__":
    main()
