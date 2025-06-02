#!/usr/bin/env python3
"""
Command-line health check tool for the scraper system.
Run this before starting scrapers to ensure environment is ready.
"""

import argparse
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scraper.utils.health_check import HealthStatus, run_health_check  # noqa: E402


def main():
    """Main entry point for health check CLI."""
    parser = argparse.ArgumentParser(
        description="Health check for scraper system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run basic health check
  python health_check.py

  # Run with verbose output
  python health_check.py -v

  # Run and exit with error if unhealthy
  python health_check.py --strict
""",
    )

    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed health check information")

    parser.add_argument("--strict", action="store_true", help="Exit with error code if any check fails (including degraded)")

    parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()

    # Run health checks
    overall_status, results = run_health_check(verbose=args.verbose and not args.json)

    # JSON output if requested
    if args.json:
        import json

        output = {"overall_status": overall_status.value, "checks": [r.to_dict() for r in results]}
        print(json.dumps(output, indent=2))
    elif not args.verbose:
        # Simple output for non-verbose mode
        if overall_status == HealthStatus.HEALTHY:
            print("✅ All health checks passed")
        elif overall_status == HealthStatus.DEGRADED:
            print("⚠️  Some health checks degraded")
            failed = [r for r in results if r.status != HealthStatus.HEALTHY]
            for r in failed:
                print(f"  - {r.name}: {r.message}")
        else:
            print("❌ Health checks failed")
            failed = [r for r in results if r.status == HealthStatus.UNHEALTHY]
            for r in failed:
                print(f"  - {r.name}: {r.message}")

    # Determine exit code
    if args.strict and overall_status != HealthStatus.HEALTHY:
        sys.exit(1)
    elif overall_status == HealthStatus.UNHEALTHY:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
