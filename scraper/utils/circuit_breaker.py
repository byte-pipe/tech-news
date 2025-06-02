"""
Circuit breaker pattern implementation for external service calls.
Prevents cascading failures when external services are unavailable.
"""

import logging
import time
from enum import Enum
from functools import wraps
from typing import Any, Callable, Type


class CircuitState(Enum):
    """Circuit breaker states."""

    CLOSED = "closed"  # Normal operation, requests go through
    OPEN = "open"  # Circuit is open, requests fail fast
    HALF_OPEN = "half_open"  # Testing if service has recovered


class CircuitBreakerError(Exception):
    """Raised when circuit breaker is open."""


class CircuitBreaker:
    """
    Circuit breaker implementation for protecting external service calls.

    States:
    - CLOSED: Normal operation, all requests pass through
    - OPEN: Service is failing, all requests fail fast
    - HALF_OPEN: Testing recovery, limited requests allowed
    """

    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60, expected_exception: Type[BaseException] = Exception, name: str = "circuit_breaker"):
        """
        Initialize circuit breaker.

        Args:
            failure_threshold: Number of failures before opening circuit
            recovery_timeout: Seconds to wait before trying again
            expected_exception: Exception type that counts as failure
            name: Name for logging purposes
        """
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        self.name = name

        # State tracking
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = 0
        self.success_count = 0

        self.logger = logging.getLogger(__name__)

    def __call__(self, func: Callable) -> Callable:
        """Decorator to wrap functions with circuit breaker."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            return self.call(func, *args, **kwargs)

        return wrapper

    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function with circuit breaker protection.

        Args:
            func: Function to execute
            *args, **kwargs: Function arguments

        Returns:
            Function result if successful

        Raises:
            CircuitBreakerError: If circuit is open
            Original exception: If function fails in closed state
        """
        # Check if we should attempt the call
        if not self._can_attempt():
            raise CircuitBreakerError(f"Circuit breaker '{self.name}' is open. " f"Last failure: {time.time() - self.last_failure_time:.1f}s ago")

        try:
            # Attempt the call
            result = func(*args, **kwargs)

            # Success - handle state transitions
            self._on_success()
            return result

        except self.expected_exception as e:
            # Expected failure - update failure tracking
            self._on_failure()
            raise e

    def _can_attempt(self) -> bool:
        """Check if we can attempt a call based on current state."""
        if self.state == CircuitState.CLOSED:
            return True

        if self.state == CircuitState.OPEN:
            # Check if enough time has passed to try recovery
            if time.time() - self.last_failure_time >= self.recovery_timeout:
                self.logger.info(f"Circuit breaker '{self.name}' transitioning to HALF_OPEN")
                self.state = CircuitState.HALF_OPEN
                return True
            return False

        if self.state == CircuitState.HALF_OPEN:
            # Allow limited attempts in half-open state
            return True

        return False

    def _on_success(self):
        """Handle successful call."""
        if self.state == CircuitState.HALF_OPEN:
            # Recovery successful - close circuit
            self.logger.info(f"Circuit breaker '{self.name}' recovered, closing circuit")
            self.state = CircuitState.CLOSED
            self.failure_count = 0
            self.success_count = 0
        elif self.state == CircuitState.CLOSED:
            # Reset failure count on success
            self.failure_count = 0

    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = time.time()

        if self.state == CircuitState.HALF_OPEN:
            # Failed during recovery attempt - back to open
            self.logger.warning(f"Circuit breaker '{self.name}' failed during recovery, reopening circuit")
            self.state = CircuitState.OPEN
        elif self.state == CircuitState.CLOSED:
            # Check if we should open the circuit
            if self.failure_count >= self.failure_threshold:
                self.logger.warning(f"Circuit breaker '{self.name}' opening after {self.failure_count} failures")
                self.state = CircuitState.OPEN

    def reset(self):
        """Manually reset circuit breaker to closed state."""
        self.logger.info(f"Circuit breaker '{self.name}' manually reset")
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = 0

    def get_status(self) -> dict:
        """Get current circuit breaker status."""
        return {
            "name": self.name,
            "state": self.state.value,
            "failure_count": self.failure_count,
            "last_failure_time": self.last_failure_time,
            "time_since_failure": time.time() - self.last_failure_time if self.last_failure_time else 0,
        }


# Pre-configured circuit breakers for common services
http_circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=30, expected_exception=Exception, name="http_requests")  # Catch all HTTP-related exceptions

ollama_circuit_breaker = CircuitBreaker(failure_threshold=2, recovery_timeout=60, expected_exception=Exception, name="ollama_service")  # Ollama service exceptions

content_fetch_circuit_breaker = CircuitBreaker(failure_threshold=5, recovery_timeout=45, expected_exception=Exception, name="content_fetching")  # Content fetching exceptions


def with_circuit_breaker(breaker: CircuitBreaker) -> Callable:
    """
    Decorator factory for applying circuit breaker to functions.

    Usage:
        @with_circuit_breaker(http_circuit_breaker)
        def fetch_data(url):
            return requests.get(url)
    """

    def decorator(func: Callable) -> Callable:
        return breaker(func)

    return decorator
