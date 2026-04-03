"""
Generate visual analytics from links.csv data.

Produces PNG charts and displays them in the terminal via chafa.
"""

import os
import subprocess
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from rich.console import Console
from rich.table import Table

matplotlib.use("Agg")

console = Console()

# Consistent style
sns.set_theme(style="darkgrid")
PALETTE = "husl"
FIG_DPI = 150
FIG_SIZE = (12, 6)


def _load_data(csv_path: str, days: Optional[int] = None) -> pd.DataFrame:
    """Load and prepare the links CSV."""
    df = pd.read_csv(csv_path, parse_dates=["date_scraped"])
    df["date_published"] = pd.to_datetime(df["date_published"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
    df["comments"] = pd.to_numeric(df["comments"], errors="coerce").fillna(0).astype(int)
    df["seen_count"] = pd.to_numeric(df["seen_count"], errors="coerce").fillna(1).astype(int)
    if days:
        cutoff = df["date_scraped"].max() - pd.Timedelta(days=days)
        df = df[df["date_scraped"] >= cutoff]
    return df


def _wait_for_key() -> None:
    """Wait for any key press to continue."""
    console.print("[dim]Press any key to continue...[/dim]", end="")
    try:
        import sys
        import tty
        import termios

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        console.print()
    except Exception:
        input()


def _show_png(path: str, width: Optional[int] = None) -> None:
    """Display a PNG in the terminal using chafa."""
    cmd = ["chafa", "--size", str(width or 80) + "x", path]
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        console.print(f"[dim](chafa not found, saved to {path})[/dim]")


def _save_and_show(fig: plt.Figure, out_dir: str, name: str, width: Optional[int] = None) -> str:
    """Save figure to PNG and display via chafa."""
    path = os.path.join(out_dir, f"{name}.png")
    fig.savefig(path, dpi=FIG_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    _show_png(path, width)
    return path


# ------------------------------------------------------------------
# Chart generators
# ------------------------------------------------------------------


def chart_daily_volume(df: pd.DataFrame, out_dir: str, width: Optional[int] = None) -> str:
    """Daily link volume over time, stacked by source."""
    daily = df.groupby([df["date_scraped"].dt.date, "source"]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    daily.plot.area(ax=ax, alpha=0.7, colormap="tab10")
    ax.set_title("Daily Links by Source")
    ax.set_xlabel("")
    ax.set_ylabel("Links")
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    fig.autofmt_xdate()
    return _save_and_show(fig, out_dir, "daily_volume", width)


def chart_source_breakdown(df: pd.DataFrame, out_dir: str, width: Optional[int] = None) -> str:
    """Pie chart of total links per source."""
    counts = df["source"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = sns.color_palette(PALETTE, len(counts))
    wedges, texts, autotexts = ax.pie(counts, labels=counts.index, autopct="%1.1f%%", colors=colors, pctdistance=0.85)
    for t in autotexts:
        t.set_fontsize(9)
    ax.set_title("Links by Source (All Time)")
    return _save_and_show(fig, out_dir, "source_breakdown", width)


def chart_category_bars(df: pd.DataFrame, out_dir: str, width: Optional[int] = None) -> str:
    """Horizontal bar chart of category distribution."""
    counts = df["category"].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette(PALETTE, len(counts))
    counts.plot.barh(ax=ax, color=colors)
    ax.set_title("Links by Category")
    ax.set_xlabel("Count")
    ax.invert_yaxis()
    for i, v in enumerate(counts):
        ax.text(v + 10, i, str(v), va="center", fontsize=9)
    return _save_and_show(fig, out_dir, "category_bars", width)


def chart_category_trend(df: pd.DataFrame, out_dir: str, width: Optional[int] = None) -> str:
    """Weekly category trends over time."""
    df_copy = df.copy()
    df_copy["week"] = df_copy["date_scraped"].dt.to_period("W").dt.start_time
    top_cats = df_copy["category"].value_counts().head(6).index
    weekly = df_copy[df_copy["category"].isin(top_cats)].groupby(["week", "category"]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    weekly.plot(ax=ax, marker=".", linewidth=2)
    ax.set_title("Weekly Category Trends (Top 6)")
    ax.set_xlabel("")
    ax.set_ylabel("Links per Week")
    ax.legend(fontsize=8)
    fig.autofmt_xdate()
    return _save_and_show(fig, out_dir, "category_trend", width)


def chart_score_distribution(df: pd.DataFrame, out_dir: str, width: Optional[int] = None) -> str:
    """Box plot of scores by source (for sources that have scores)."""
    scored = df[df["score"] > 0].copy()
    if scored.empty:
        return ""
    # Keep sources with enough data
    source_counts = scored["source"].value_counts()
    valid_sources = source_counts[source_counts >= 10].index
    scored = scored[scored["source"].isin(valid_sources)]
    if scored.empty:
        return ""
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.boxplot(data=scored, x="source", y="score", ax=ax, palette=PALETTE, showfliers=False)
    ax.set_title("Score Distribution by Source")
    ax.set_xlabel("")
    ax.set_ylabel("Score")
    return _save_and_show(fig, out_dir, "score_dist", width)


def chart_top_trending(df: pd.DataFrame, out_dir: str, width: Optional[int] = None) -> str:
    """Top 20 most-seen URLs (trending)."""
    trending = df.sort_values("seen_count", ascending=False).drop_duplicates("url").head(20)
    if trending.empty:
        return ""
    fig, ax = plt.subplots(figsize=(12, 8))
    labels = trending["title"].str[:60].tolist()
    labels = [l if l else u[:60] for l, u in zip(labels, trending["url"])]
    colors = sns.color_palette(PALETTE, len(labels))
    ax.barh(range(len(labels)), trending["seen_count"].values, color=colors)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis()
    ax.set_title("Top 20 Trending Links (by seen_count)")
    ax.set_xlabel("Times Seen")
    fig.tight_layout()
    return _save_and_show(fig, out_dir, "top_trending", width)


def chart_heatmap(df: pd.DataFrame, out_dir: str, width: Optional[int] = None) -> str:
    """Heatmap: source x day-of-week activity."""
    df_copy = df.copy()
    df_copy["dow"] = df_copy["date_scraped"].dt.day_name()
    dow_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    pivot = df_copy.groupby(["source", "dow"]).size().unstack(fill_value=0)
    pivot = pivot.reindex(columns=[d for d in dow_order if d in pivot.columns])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot, annot=True, fmt="d", cmap="YlOrRd", ax=ax)
    ax.set_title("Source Activity by Day of Week")
    ax.set_xlabel("")
    ax.set_ylabel("")
    return _save_and_show(fig, out_dir, "heatmap_dow", width)


# ------------------------------------------------------------------
# Summary table
# ------------------------------------------------------------------


def print_summary_table(df: pd.DataFrame) -> None:
    """Print a rich summary table to the console."""
    table = Table(title="Links Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green", justify="right")

    table.add_row("Total links", f"{len(df):,}")
    table.add_row("Unique URLs", f"{df['url'].nunique():,}")
    table.add_row("Sources", str(df["source"].nunique()))
    table.add_row("Categories", str(df["category"].nunique()))
    table.add_row("Date range", f"{df['date_scraped'].min().date()} to {df['date_scraped'].max().date()}")
    table.add_row("Days covered", str(df["date_scraped"].dt.date.nunique()))
    avg_daily = len(df) / max(df["date_scraped"].dt.date.nunique(), 1)
    table.add_row("Avg links/day", f"{avg_daily:.0f}")

    top_source = df["source"].value_counts().idxmax()
    table.add_row("Top source", top_source)

    top_cat = df["category"].value_counts().idxmax()
    table.add_row("Top category", top_cat)

    scored = df[df["score"] > 0]
    if not scored.empty:
        top_scored = scored.sort_values("score", ascending=False).iloc[0]
        table.add_row("Highest score", f"{int(top_scored['score']):,} ({top_scored['source']})")

    console.print(table)


# ------------------------------------------------------------------
# Main runner
# ------------------------------------------------------------------

ALL_CHARTS = [
    ("daily_volume", chart_daily_volume),
    ("source_breakdown", chart_source_breakdown),
    ("category_bars", chart_category_bars),
    ("category_trend", chart_category_trend),
    ("score_dist", chart_score_distribution),
    ("top_trending", chart_top_trending),
    ("heatmap_dow", chart_heatmap),
]


def run_analytics(csv_path: str, out_dir: Optional[str] = None, days: Optional[int] = None, charts: Optional[list] = None, width: Optional[int] = None) -> list:
    """Generate all charts and return list of saved PNG paths."""
    df = _load_data(csv_path, days)
    if df.empty:
        console.print("[red]No data found in links.csv[/red]")
        return []

    print_summary_table(df)
    console.print()

    if out_dir is None:
        out_dir = tempfile.mkdtemp(prefix="tech-news-analytics-")
    os.makedirs(out_dir, exist_ok=True)

    chart_fns = ALL_CHARTS
    if charts:
        chart_fns = [(n, fn) for n, fn in ALL_CHARTS if n in charts]

    # Generate charts in parallel (matplotlib is thread-safe for separate figures)
    paths = []
    lock = threading.Lock()

    def _gen(name, fn):
        try:
            p = fn(df, out_dir, width)
            if p:
                with lock:
                    console.print(f"[dim]  saved: {p}[/dim]")
                return p
        except Exception as e:
            with lock:
                console.print(f"[red]  {name} failed: {e}[/red]")
        return None

    # Run sequentially to avoid matplotlib threading issues with display
    for i, (name, fn) in enumerate(chart_fns):
        result = _gen(name, fn)
        if result:
            paths.append(result)
            if i < len(chart_fns) - 1:
                _wait_for_key()

    console.print(f"\n[bold green]{len(paths)} charts saved to {out_dir}[/bold green]")
    return paths
