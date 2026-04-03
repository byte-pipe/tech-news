"""
Health check system for validating scraper environment and dependencies.
Ensures all required services and resources are available before starting.
"""

import logging
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple

import psutil
import requests

from scraper.core.config import get_config


class HealthStatus(Enum):
    """Health check status levels."""

    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


@dataclass
class HealthCheckResult:
    """Result of a single health check."""

    name: str
    status: HealthStatus
    message: str
    details: Optional[Dict] = None
    timestamp: Optional[datetime] = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {"name": self.name, "status": self.status.value, "message": self.message, "details": self.details or {}, "timestamp": self.timestamp.isoformat()}


class HealthChecker:
    """
    Comprehensive health checker for the scraper system.
    Validates filesystem, network, external services, and resources.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config = get_config()
        self.checks = []

    def check_all(self) -> Tuple[HealthStatus, List[HealthCheckResult]]:
        """
        Run all health checks and return overall status.

        Returns:
            Tuple of (overall_status, list_of_results)
        """
        results = []

        # Run all checks
        results.append(self.check_filesystem())
        results.append(self.check_disk_space())
        results.append(self.check_network_connectivity())
        results.append(self.check_ollama_service())
        results.append(self.check_memory_usage())
        results.append(self.check_configuration())

        # Determine overall status
        if any(r.status == HealthStatus.UNHEALTHY for r in results):
            overall_status = HealthStatus.UNHEALTHY
        elif any(r.status == HealthStatus.DEGRADED for r in results):
            overall_status = HealthStatus.DEGRADED
        else:
            overall_status = HealthStatus.HEALTHY

        return overall_status, results

    def check_filesystem(self) -> HealthCheckResult:
        """Check filesystem permissions and directory structure."""
        try:
            # Check data directory
            data_dir = self.config.data_dir
            if not data_dir.exists():
                return HealthCheckResult(name="filesystem", status=HealthStatus.UNHEALTHY, message=f"Data directory does not exist: {data_dir}")

            # Check write permissions
            test_file = data_dir / ".health_check_test"
            try:
                test_file.write_text("test")
                test_file.unlink()  # Clean up
            except Exception as e:
                return HealthCheckResult(name="filesystem", status=HealthStatus.UNHEALTHY, message=f"Cannot write to data directory: {str(e)}")

            # Check logs directory
            logs_dir = self.config.logs_dir
            if not logs_dir.exists():
                self.logger.warning(f"Logs directory does not exist: {logs_dir}")
                return HealthCheckResult(name="filesystem", status=HealthStatus.DEGRADED, message="Logs directory missing but can be created", details={"logs_dir": str(logs_dir)})

            return HealthCheckResult(name="filesystem", status=HealthStatus.HEALTHY, message="Filesystem permissions OK", details={"data_dir": str(data_dir), "logs_dir": str(logs_dir)})

        except Exception as e:
            return HealthCheckResult(name="filesystem", status=HealthStatus.UNHEALTHY, message=f"Filesystem check failed: {str(e)}")

    def check_disk_space(self) -> HealthCheckResult:
        """Check available disk space."""
        try:
            # Get disk usage for data directory
            stat = psutil.disk_usage(str(self.config.data_dir))

            # Convert to GB
            free_gb = stat.free / (1024**3)
            total_gb = stat.total / (1024**3)
            percent_used = stat.percent

            details = {"free_gb": round(free_gb, 2), "total_gb": round(total_gb, 2), "percent_used": percent_used}

            # Determine status based on free space
            if free_gb < 0.5:  # Less than 500MB
                return HealthCheckResult(name="disk_space", status=HealthStatus.UNHEALTHY, message=f"Critical: Only {free_gb:.2f}GB free", details=details)
            elif free_gb < 2.0:  # Less than 2GB
                return HealthCheckResult(name="disk_space", status=HealthStatus.DEGRADED, message=f"Warning: Only {free_gb:.2f}GB free", details=details)
            else:
                return HealthCheckResult(name="disk_space", status=HealthStatus.HEALTHY, message=f"{free_gb:.2f}GB free ({100-percent_used:.1f}% available)", details=details)

        except Exception as e:
            return HealthCheckResult(name="disk_space", status=HealthStatus.UNHEALTHY, message=f"Could not check disk space: {str(e)}")

    def check_network_connectivity(self) -> HealthCheckResult:
        """Check network connectivity to key services."""
        test_urls = [
            ("GitHub", "https://github.com"),
            ("HackerNews", "https://news.ycombinator.com"),
        ]

        failed_services = []
        response_times = []

        for service_name, url in test_urls:
            try:
                import time

                start_time = time.time()
                response = requests.head(url, timeout=5, allow_redirects=True)

                # If HEAD fails with 405, try GET (some sites block HEAD)
                if response.status_code == 405:
                    response = requests.get(url, timeout=5, allow_redirects=True, stream=True)
                    # Close the connection immediately to avoid downloading content
                    response.close()

                response_time = time.time() - start_time

                if response.status_code >= 400:
                    failed_services.append(f"{service_name} ({response.status_code})")
                else:
                    response_times.append((service_name, response_time))

            except Exception as e:
                failed_services.append(f"{service_name} ({str(e)})")

        if failed_services:
            return HealthCheckResult(
                name="network",
                status=HealthStatus.DEGRADED if len(failed_services) < len(test_urls) else HealthStatus.UNHEALTHY,
                message=f"Some services unreachable: {', '.join(failed_services)}",
                details={"failed": failed_services, "successful": [s for s, _ in response_times]},
            )
        else:
            avg_response_time = sum(t for _, t in response_times) / len(response_times)
            return HealthCheckResult(name="network", status=HealthStatus.HEALTHY, message=f"All services reachable (avg {avg_response_time:.2f}s)", details={"response_times": {s: f"{t:.2f}s" for s, t in response_times}})

    def check_ollama_service(self) -> HealthCheckResult:
        """Check if Ollama service is available."""
        try:
            # Check Ollama API endpoint
            response = requests.get("http://localhost:11434/api/tags", timeout=5)

            if response.status_code == 200:
                data = response.json()
                models = data.get("models", [])
                model_names = [m.get("name", "unknown") for m in models]

                return HealthCheckResult(
                    name="ollama", status=HealthStatus.HEALTHY, message=f"Ollama service available with {len(models)} models", details={"models": model_names[:5], "total_models": len(models)}  # Show first 5 models
                )
            else:
                return HealthCheckResult(name="ollama", status=HealthStatus.DEGRADED, message=f"Ollama service returned status {response.status_code}", details={"status_code": response.status_code})

        except requests.exceptions.ConnectionError:
            return HealthCheckResult(name="ollama", status=HealthStatus.DEGRADED, message="Ollama service not running (AI summarization unavailable)", details={"hint": "Start Ollama with: ollama serve"})
        except Exception as e:
            return HealthCheckResult(name="ollama", status=HealthStatus.DEGRADED, message=f"Ollama check failed: {str(e)}")

    def check_memory_usage(self) -> HealthCheckResult:
        """Check system memory usage."""
        try:
            memory = psutil.virtual_memory()

            # Convert to GB
            available_gb = memory.available / (1024**3)
            total_gb = memory.total / (1024**3)
            percent_used = memory.percent

            details = {"available_gb": round(available_gb, 2), "total_gb": round(total_gb, 2), "percent_used": percent_used}

            if percent_used > 90:
                return HealthCheckResult(name="memory", status=HealthStatus.UNHEALTHY, message=f"Critical: {percent_used}% memory used", details=details)
            elif percent_used > 80:
                return HealthCheckResult(name="memory", status=HealthStatus.DEGRADED, message=f"Warning: {percent_used}% memory used", details=details)
            else:
                return HealthCheckResult(name="memory", status=HealthStatus.HEALTHY, message=f"{available_gb:.1f}GB available ({100-percent_used:.1f}% free)", details=details)

        except Exception as e:
            return HealthCheckResult(name="memory", status=HealthStatus.UNHEALTHY, message=f"Could not check memory: {str(e)}")

    def check_configuration(self) -> HealthCheckResult:
        """Check if configuration is valid."""
        try:
            # Check if config files exist
            sites_config = self.config.project_root / "scraper" / "config" / "sites.yaml"

            if not sites_config.exists():
                return HealthCheckResult(name="configuration", status=HealthStatus.UNHEALTHY, message="sites.yaml configuration file not found")

            # Try to load the configuration
            import yaml

            try:
                with open(sites_config, "r") as f:
                    config_data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                return HealthCheckResult(name="configuration", status=HealthStatus.UNHEALTHY, message=f"YAML syntax error in sites.yaml: {str(e)}", details={"config_path": str(sites_config), "error_type": "yaml_syntax"})
            except Exception as e:
                return HealthCheckResult(name="configuration", status=HealthStatus.UNHEALTHY, message=f"Cannot read sites.yaml: {str(e)}", details={"config_path": str(sites_config), "error_type": "file_access"})

            if not config_data:
                return HealthCheckResult(name="configuration", status=HealthStatus.UNHEALTHY, message="sites.yaml is empty")

            # Validate required configuration sections
            required_keys = ["sites"]
            missing_keys = [key for key in required_keys if key not in config_data]
            if missing_keys:
                return HealthCheckResult(
                    name="configuration",
                    status=HealthStatus.UNHEALTHY,
                    message=f"Missing required configuration sections: {missing_keys}",
                    details={"missing_keys": missing_keys, "available_keys": list(config_data.keys())},
                )

            sites = config_data.get("sites", {})
            if not sites:
                return HealthCheckResult(name="configuration", status=HealthStatus.UNHEALTHY, message="No sites configured in sites.yaml")

            # Validate site configurations
            invalid_sites = []
            for site_name, site_config in sites.items():
                if not isinstance(site_config, dict):
                    invalid_sites.append(f"{site_name}: not a dictionary")
                elif "url" not in site_config:
                    invalid_sites.append(f"{site_name}: missing 'url' field")
                elif site_config.get("api_based") is not True and "selector" not in site_config and "json_selector" not in site_config:
                    invalid_sites.append(f"{site_name}: missing 'selector' or 'json_selector' field (not API-based)")

            if invalid_sites:
                return HealthCheckResult(
                    name="configuration",
                    status=HealthStatus.DEGRADED,
                    message=f"Some sites have invalid configuration: {', '.join(invalid_sites[:3])}{'...' if len(invalid_sites) > 3 else ''}",
                    details={"invalid_sites": invalid_sites, "total_sites": len(sites)},
                )

            return HealthCheckResult(name="configuration", status=HealthStatus.HEALTHY, message=f"Configuration valid with {len(sites)} sites", details={"sites": list(sites.keys()), "config_path": str(sites_config)})

        except Exception as e:
            return HealthCheckResult(name="configuration", status=HealthStatus.UNHEALTHY, message=f"Configuration check failed: {str(e)}")

    def print_report(self, results: List[HealthCheckResult]):
        """Print a formatted health check report."""
        print("\n" + "=" * 60)
        print("HEALTH CHECK REPORT")
        print("=" * 60)

        for result in results:
            # Choose symbol based on status
            if result.status == HealthStatus.HEALTHY:
                symbol = "✅"
            elif result.status == HealthStatus.DEGRADED:
                symbol = "⚠️ "
            else:
                symbol = "❌"

            print(f"\n{symbol} {result.name.upper()}")
            print(f"   Status: {result.status.value}")
            print(f"   Message: {result.message}")

            if result.details:
                print("   Details:")
                for key, value in result.details.items():
                    print(f"     - {key}: {value}")

        print("\n" + "=" * 60)


def run_health_check(verbose: bool = False) -> Tuple[HealthStatus, List[HealthCheckResult]]:
    """
    Run all health checks and return results.

    Args:
        verbose: If True, print detailed report

    Returns:
        Tuple of (overall_status, list_of_results)
    """
    checker = HealthChecker()
    overall_status, results = checker.check_all()

    if verbose:
        checker.print_report(results)

        # Print overall status
        if overall_status == HealthStatus.HEALTHY:
            print("\n✅ OVERALL STATUS: HEALTHY - All systems operational")
        elif overall_status == HealthStatus.DEGRADED:
            print("\n⚠️  OVERALL STATUS: DEGRADED - Some issues detected but system can run")
        else:
            print("\n❌ OVERALL STATUS: UNHEALTHY - Critical issues detected")

    return overall_status, results


if __name__ == "__main__":
    # Run health check when executed directly
    import sys

    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    status, results = run_health_check(verbose=True)

    # Exit with appropriate code
    if status == HealthStatus.UNHEALTHY:
        sys.exit(1)
    else:
        sys.exit(0)
