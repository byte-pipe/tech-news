"""
Logging configuration for the scraper application.
"""

import logging
import os
import threading


class ThreadSafeFileHandler(logging.FileHandler):
    """Thread-safe file handler to prevent reentrant call issues."""

    def __init__(self, filename, mode="a", encoding=None, delay=False):
        super().__init__(filename, mode, encoding, delay)
        self.lock = threading.Lock()

    def emit(self, record):
        """Emit a record with thread safety."""
        with self.lock:
            try:
                super().emit(record)
            except Exception:
                # Silently ignore logging errors to prevent crashes
                pass


def setup_logging():
    """Configure logging for the application."""
    # Create logs directory
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "scraper.log")

    # Clear ALL existing handlers from root logger
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        try:
            handler.close()  # Properly close file handles
        except Exception:
            pass
        root_logger.removeHandler(handler)

    # Use thread-safe file handler instead of RotatingFileHandler
    # Simple file handler is more stable than rotating handler
    try:
        file_handler = ThreadSafeFileHandler(log_file, mode="a")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        file_handler.setLevel(logging.DEBUG)
        root_logger.addHandler(file_handler)
    except Exception as e:
        # If file logging fails, just use console
        print(f"Warning: Could not set up file logging: {e}")

    # Console logging - only warnings and errors (no INFO spam)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(message)s"))
    console_handler.setLevel(logging.WARNING)
    root_logger.addHandler(console_handler)

    root_logger.setLevel(logging.DEBUG)

    # Disable logging from noisy libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)

    return root_logger
