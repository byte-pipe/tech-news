import subprocess
import sys
from pathlib import Path

import tomli

SRC_FOLDER = "src"


def load_pyproject_config():
    """Load configuration from pyproject.toml."""
    config_path = Path("pyproject.toml")
    if not config_path.exists():
        raise FileNotFoundError("No pyproject.toml found")

    with open(config_path, "rb") as f:
        return tomli.load(f)


def autoflake_check():
    """Run autoflake to remove unused imports and variables."""
    src_dir = Path(f"{SRC_FOLDER}")
    tests_dir = Path("tests")
    cmd = [
        "autoflake",
        "--recursive",
        "--in-place",
        "--remove-all-unused-imports",
        "--remove-unused-variables",
        "--ignore-init-module-imports",
        str(src_dir),
        str(tests_dir),
    ]
    try:
        subprocess.run(cmd, check=True)
        print("✨ Autoflake completed successfully!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Autoflake failed with error code {e.returncode}")
        return e.returncode


def isort_check():
    """Run isort to sort imports."""
    src_dir = Path(f"{SRC_FOLDER}")
    tests_dir = Path("tests")
    load_pyproject_config()
    args = ["--settings-path", "pyproject.toml"]
    cmd = ["isort"] + args + [str(src_dir), str(tests_dir)]
    try:
        subprocess.run(cmd, check=True)
        print("✨ isort completed successfully!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ isort failed with error code {e.returncode}")
        return e.returncode


def black_check():
    """Run black to format code."""
    src_dir = Path(f"{SRC_FOLDER}")
    tests_dir = Path("tests")
    args = ["--config", "pyproject.toml"]
    cmd = ["black"] + args + [str(src_dir), str(tests_dir)]
    try:
        subprocess.run(cmd, check=True)
        print("✨ black completed successfully!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ black failed with error code {e.returncode}")
        return e.returncode


def flake8_check():
    """Run flake8 to check for style and logical errors."""
    src_dir = Path(f"{SRC_FOLDER}")
    tests_dir = Path("tests")
    args = ["--config", ".flake8"]
    cmd = ["flake8"] + args + [str(src_dir), str(tests_dir)]
    try:
        subprocess.run(cmd, check=True)
        print("✨ flake8 completed successfully!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ flake8 found issues (exit code {e.returncode})")
        return e.returncode


def mypy_check():
    """Run mypy to check types."""
    args = ["--config-file", "pyproject.toml"]
    cmd = ["mypy"] + args + [f"{SRC_FOLDER}"]
    try:
        subprocess.run(cmd, check=True)
        print("✨ mypy completed successfully!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ mypy found issues (exit code {e.returncode})")
        return e.returncode


def bandit_check():
    """Run bandit to check for security issues."""
    args = ["-c", "pyproject.toml"]
    cmd = ["bandit"] + args + ["-r", f"{SRC_FOLDER}"]
    try:
        subprocess.run(cmd, check=True)
        print("✨ bandit completed successfully!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ bandit found issues (exit code {e.returncode})")
        return e.returncode


def main():
    """Run all quality checks."""
    autoflake_exit = autoflake_check()
    isort_exit = isort_check()
    black_exit = black_check()
    flake8_exit = flake8_check()
    mypy_exit = mypy_check()
    bandit_exit = bandit_check()
    # Return non-zero if any tool failed
    return max(autoflake_exit, isort_exit, black_exit, flake8_exit, mypy_exit, bandit_exit)


if __name__ == "__main__":
    sys.exit(main())
