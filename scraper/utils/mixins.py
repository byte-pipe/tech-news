"""
Common mixins for the scraper package.

This module provides reusable mixin classes to reduce code duplication.
"""

import logging

logger = logging.getLogger(__name__)


class ResourceManagerMixin:
    """Mixin for classes that manage resources requiring cleanup.

    Provides context manager support and ensures cleanup happens.
    Classes using this mixin should implement the close() method.
    """

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with cleanup."""
        self.close()

    def __del__(self):
        """Ensure cleanup happens even if context manager isn't used."""
        try:
            self.close()
        except Exception:
            pass  # Ignore errors during cleanup

    def close(self):
        """Close and clean up resources. Should be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the close() method")


class SessionManagerMixin(ResourceManagerMixin):
    """Mixin for classes that manage HTTP sessions.

    Provides automatic session cleanup through context manager support.
    Classes using this mixin should have a 'session' attribute.
    """

    def close(self):
        """Close the HTTP session and clean up resources."""
        if hasattr(self, "session") and self.session:
            try:
                self.session.close()
            except Exception as e:
                logger.debug(f"Error closing session: {e}")
