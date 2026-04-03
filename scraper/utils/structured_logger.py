"""
Structured logging system with metrics tracking.
Provides consistent log formatting and performance monitoring.
"""

import json
import logging
import threading
import time
from contextlib import contextmanager
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Dict, Optional


class StructuredLogger:
    """
    Enhanced logger that outputs structured logs with consistent format.
    Includes performance metrics and context tracking.
    """

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.context = {}
        self._timers = {}

    def _format_log_entry(self, level: str, message: str, **kwargs) -> Dict[str, Any]:
        """Format a structured log entry."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": level,
            "logger": self.logger.name,
            "message": message,
        }

        # Add context if available
        if self.context:
            entry["context"] = self.context.copy()

        # Add any additional fields
        if kwargs:
            entry.update(kwargs)

        return entry

    def _log(self, level: str, message: str, **kwargs):
        """Internal logging method."""
        entry = self._format_log_entry(level, message, **kwargs)

        # For structured output, log as JSON
        if self.logger.level <= logging.DEBUG:
            # In debug mode, pretty print
            log_message = json.dumps(entry, indent=2)
        else:
            # In production, single line JSON
            log_message = json.dumps(entry)

        # Use the appropriate logging method
        getattr(self.logger, level.lower())(log_message)

    def debug(self, message: str, **kwargs):
        """Log debug message with structured data."""
        self._log("DEBUG", message, **kwargs)

    def info(self, message: str, **kwargs):
        """Log info message with structured data."""
        self._log("INFO", message, **kwargs)

    def warning(self, message: str, **kwargs):
        """Log warning message with structured data."""
        self._log("WARNING", message, **kwargs)

    def error(self, message: str, **kwargs):
        """Log error message with structured data."""
        self._log("ERROR", message, **kwargs)

    def add_context(self, **kwargs):
        """Add persistent context that will be included in all logs."""
        self.context.update(kwargs)

    def clear_context(self):
        """Clear all persistent context."""
        self.context.clear()

    @contextmanager
    def with_context(self, **kwargs):
        """Temporary context for a block of code."""
        old_context = self.context.copy()
        self.context.update(kwargs)
        try:
            yield
        finally:
            self.context = old_context

    def start_timer(self, name: str):
        """Start a named timer for performance tracking."""
        self._timers[name] = time.time()

    def stop_timer(self, name: str) -> Optional[float]:
        """Stop a named timer and return elapsed time."""
        if name not in self._timers:
            return None

        elapsed = time.time() - self._timers[name]
        del self._timers[name]
        return elapsed

    @contextmanager
    def timer(self, operation: str, log_start: bool = True):
        """Context manager for timing operations."""
        if log_start:
            self.info(f"Starting {operation}", operation=operation, status="started")

        start_time = time.time()
        try:
            yield
            elapsed = time.time() - start_time
            self.info(
                f"Completed {operation}",
                operation=operation,
                status="completed",
                duration_seconds=round(elapsed, 3),
            )
        except Exception as e:
            elapsed = time.time() - start_time
            self.error(
                f"Failed {operation}",
                operation=operation,
                status="failed",
                duration_seconds=round(elapsed, 3),
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

    def log_metric(self, metric_name: str, value: Any, **tags):
        """Log a metric with optional tags."""
        self.info(
            f"Metric: {metric_name}",
            metric_name=metric_name,
            metric_value=value,
            metric_type="gauge",
            **tags,
        )

    def log_scraper_result(
        self,
        scraper_name: str,
        success: bool,
        items_count: int = 0,
        duration: float = 0,
        error: Optional[str] = None,
    ):
        """Log scraper execution results."""
        self.info(
            f"Scraper {scraper_name} {'succeeded' if success else 'failed'}",
            scraper=scraper_name,
            success=success,
            items_count=items_count,
            duration_seconds=round(duration, 3),
            error=error,
        )

    def log_http_request(
        self,
        method: str,
        url: str,
        status_code: Optional[int] = None,
        duration: Optional[float] = None,
        error: Optional[str] = None,
    ):
        """Log HTTP request details."""
        self.info(
            f"HTTP {method} {url}",
            http_method=method,
            http_url=url,
            http_status_code=status_code,
            duration_seconds=round(duration, 3) if duration else None,
            error=error,
        )


def timed_operation(logger: StructuredLogger, operation_name: str):
    """
    Decorator to automatically time and log function execution.

    Usage:
        @timed_operation(logger, "fetch_data")
        def fetch_data():
            ...
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            with logger.timer(operation_name):
                return func(*args, **kwargs)

        return wrapper

    return decorator


class MetricsCollector:
    """
    Collects and aggregates metrics during scraper execution.
    """

    def __init__(self):
        self.metrics = {
            "scrapers": {},
            "http_requests": {"total": 0, "success": 0, "failed": 0, "by_status": {}},
            "items": {"total_scraped": 0, "by_scraper": {}},
            "performance": {"total_duration": 0, "by_operation": {}},
            "errors": [],
        }
        self.start_time = time.time()
        self._lock = threading.Lock()  # Thread safety

    def record_scraper_run(
        self,
        scraper_name: str,
        success: bool,
        items_count: int = 0,
        duration: float = 0,
        error: Optional[str] = None,
    ):
        """Record metrics for a scraper run."""
        with self._lock:
            if scraper_name not in self.metrics["scrapers"]:
                self.metrics["scrapers"][scraper_name] = {
                    "runs": 0,
                    "success": 0,
                    "failed": 0,
                    "items_total": 0,
                    "total_duration": 0,
                    "errors": [],
                }

            scraper_metrics = self.metrics["scrapers"][scraper_name]
            scraper_metrics["runs"] += 1

            if success:
                scraper_metrics["success"] += 1
                scraper_metrics["items_total"] += items_count
                self.metrics["items"]["total_scraped"] += items_count
                self.metrics["items"]["by_scraper"][scraper_name] = scraper_metrics["items_total"]
            else:
                scraper_metrics["failed"] += 1
                if error:
                    scraper_metrics["errors"].append(error)
                    self.metrics["errors"].append(
                        {
                            "scraper": scraper_name,
                            "error": error,
                            "timestamp": datetime.utcnow().isoformat() + "Z",
                        }
                    )

            scraper_metrics["total_duration"] += duration
            self.metrics["performance"]["total_duration"] += duration

    def record_http_request(
        self,
        status_code: Optional[int] = None,
        success: bool = True,
        duration: float = 0,
    ):
        """Record metrics for an HTTP request."""
        with self._lock:
            self.metrics["http_requests"]["total"] += 1

            if success:
                self.metrics["http_requests"]["success"] += 1
            else:
                self.metrics["http_requests"]["failed"] += 1

            if status_code:
                status_str = str(status_code)
                if status_str not in self.metrics["http_requests"]["by_status"]:
                    self.metrics["http_requests"]["by_status"][status_str] = 0
                self.metrics["http_requests"]["by_status"][status_str] += 1

    def record_operation_duration(self, operation: str, duration: float):
        """Record duration for a named operation."""
        with self._lock:
            if operation not in self.metrics["performance"]["by_operation"]:
                self.metrics["performance"]["by_operation"][operation] = {
                    "count": 0,
                    "total_duration": 0,
                    "min_duration": float("inf"),
                    "max_duration": 0,
                }

            op_metrics = self.metrics["performance"]["by_operation"][operation]
            op_metrics["count"] += 1
            op_metrics["total_duration"] += duration
            op_metrics["min_duration"] = min(op_metrics["min_duration"], duration)
            op_metrics["max_duration"] = max(op_metrics["max_duration"], duration)

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of collected metrics."""
        with self._lock:
            total_elapsed = time.time() - self.start_time

            # Calculate scraper success rate
            total_runs = sum(s["runs"] for s in self.metrics["scrapers"].values())
            total_success = sum(s["success"] for s in self.metrics["scrapers"].values())
            success_rate = (total_success / total_runs * 100) if total_runs > 0 else 0

            # Calculate average durations
            for op_name, op_data in self.metrics["performance"]["by_operation"].items():
                if op_data["count"] > 0:
                    op_data["avg_duration"] = op_data["total_duration"] / op_data["count"]

            summary = {
                "execution_time": round(total_elapsed, 3),
                "scrapers": {
                    "total_runs": total_runs,
                    "success_rate": round(success_rate, 2),
                    "by_scraper": self.metrics["scrapers"],
                },
                "items": self.metrics["items"],
                "http_requests": self.metrics["http_requests"],
                "performance": self.metrics["performance"],
                "errors_count": len(self.metrics["errors"]),
                "errors": self.metrics["errors"][-10:],  # Last 10 errors
            }

        return summary

    def print_summary(self):
        """Print a human-readable summary of metrics."""
        summary = self.get_summary()

        print("\n" + "=" * 60)
        print("EXECUTION METRICS SUMMARY")
        print("=" * 60)

        print(f"\nTotal Execution Time: {summary['execution_time']}s")

        print("\nScraper Performance:")
        print(f"  Total Runs: {summary['scrapers']['total_runs']}")
        print(f"  Success Rate: {summary['scrapers']['success_rate']}%")

        print("\nItems Scraped:")
        print(f"  Total: {summary['items']['total_scraped']}")
        if summary["items"]["by_scraper"]:
            print("  By Scraper:")
            for scraper, count in summary["items"]["by_scraper"].items():
                print(f"    - {scraper}: {count}")

        print("\nHTTP Requests:")
        print(f"  Total: {summary['http_requests']['total']}")
        print(f"  Success: {summary['http_requests']['success']}")
        print(f"  Failed: {summary['http_requests']['failed']}")

        if summary["errors_count"] > 0:
            print(f"\nErrors ({summary['errors_count']} total):")
            for error in summary["errors"][-5:]:  # Show last 5
                print(f"  - {error['scraper']}: {error['error']}")

        print("\n" + "=" * 60)


# Global metrics collector instance
_metrics_collector = None


def get_metrics_collector() -> MetricsCollector:
    """Get the global metrics collector instance."""
    global _metrics_collector
    if _metrics_collector is None:
        _metrics_collector = MetricsCollector()
    return _metrics_collector


def reset_metrics():
    """Reset the global metrics collector."""
    global _metrics_collector
    _metrics_collector = MetricsCollector()
