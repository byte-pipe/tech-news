"""
Tests for circuit breaker implementation.
"""

import os
import sys
import time
import unittest
from unittest.mock import Mock

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraper.utils.circuit_breaker import CircuitBreaker, CircuitBreakerError, CircuitState, http_circuit_breaker, with_circuit_breaker  # noqa: E402


class TestCircuitBreaker(unittest.TestCase):
    """Test circuit breaker functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=1, name="test_breaker")  # Short timeout for testing

    def test_initial_state(self):
        """Test circuit breaker starts in closed state."""
        self.assertEqual(self.circuit_breaker.state, CircuitState.CLOSED)
        self.assertEqual(self.circuit_breaker.failure_count, 0)

    def test_successful_calls(self):
        """Test successful calls keep circuit closed."""
        mock_func = Mock(return_value="success")

        # Multiple successful calls
        for _ in range(5):
            result = self.circuit_breaker.call(mock_func)
            self.assertEqual(result, "success")

        self.assertEqual(self.circuit_breaker.state, CircuitState.CLOSED)
        self.assertEqual(self.circuit_breaker.failure_count, 0)
        self.assertEqual(mock_func.call_count, 5)

    def test_circuit_opens_after_failures(self):
        """Test circuit opens after threshold failures."""
        mock_func = Mock(side_effect=Exception("Test failure"))

        # Fail enough times to open circuit
        for i in range(3):
            with self.assertRaises(Exception):
                self.circuit_breaker.call(mock_func)

            if i < 2:  # Should still be closed
                self.assertEqual(self.circuit_breaker.state, CircuitState.CLOSED)

        # Circuit should now be open
        self.assertEqual(self.circuit_breaker.state, CircuitState.OPEN)

        # Next call should fail fast without calling function
        with self.assertRaises(CircuitBreakerError):
            self.circuit_breaker.call(mock_func)

        # Function should only have been called 3 times (threshold)
        self.assertEqual(mock_func.call_count, 3)

    def test_circuit_recovery(self):
        """Test circuit recovery from open to closed state."""
        mock_func = Mock(side_effect=Exception("Test failure"))

        # Open the circuit
        for _ in range(3):
            with self.assertRaises(Exception):
                self.circuit_breaker.call(mock_func)

        self.assertEqual(self.circuit_breaker.state, CircuitState.OPEN)

        # Immediate call should fail fast
        with self.assertRaises(CircuitBreakerError):
            self.circuit_breaker.call(mock_func)

        # Wait for recovery timeout
        time.sleep(1.1)

        # Next call should transition to half-open and succeed
        mock_func.side_effect = None
        mock_func.return_value = "recovered"

        result = self.circuit_breaker.call(mock_func)

        self.assertEqual(result, "recovered")
        self.assertEqual(self.circuit_breaker.state, CircuitState.CLOSED)
        self.assertEqual(self.circuit_breaker.failure_count, 0)

    def test_half_open_failure(self):
        """Test failure during half-open state returns to open."""
        mock_func = Mock(side_effect=Exception("Test failure"))

        # Open the circuit
        for _ in range(3):
            with self.assertRaises(Exception):
                self.circuit_breaker.call(mock_func)

        # Wait for recovery timeout
        time.sleep(1.1)

        # Next call should transition to half-open but fail
        with self.assertRaises(Exception):
            self.circuit_breaker.call(mock_func)

        # Should be back to open state
        self.assertEqual(self.circuit_breaker.state, CircuitState.OPEN)

    def test_manual_reset(self):
        """Test manual reset of circuit breaker."""
        mock_func = Mock(side_effect=Exception("Test failure"))

        # Open the circuit
        for _ in range(3):
            with self.assertRaises(Exception):
                self.circuit_breaker.call(mock_func)

        self.assertEqual(self.circuit_breaker.state, CircuitState.OPEN)

        # Manual reset
        self.circuit_breaker.reset()

        self.assertEqual(self.circuit_breaker.state, CircuitState.CLOSED)
        self.assertEqual(self.circuit_breaker.failure_count, 0)

    def test_decorator_usage(self):
        """Test using circuit breaker as decorator."""

        @self.circuit_breaker
        def test_function():
            return "decorated"

        result = test_function()
        self.assertEqual(result, "decorated")
        self.assertEqual(self.circuit_breaker.state, CircuitState.CLOSED)

    def test_decorator_factory(self):
        """Test decorator factory pattern."""

        @with_circuit_breaker(self.circuit_breaker)
        def test_function():
            return "factory_decorated"

        result = test_function()
        self.assertEqual(result, "factory_decorated")

    def test_get_status(self):
        """Test getting circuit breaker status."""
        status = self.circuit_breaker.get_status()

        self.assertEqual(status["name"], "test_breaker")
        self.assertEqual(status["state"], "closed")
        self.assertEqual(status["failure_count"], 0)
        self.assertIsInstance(status["time_since_failure"], (int, float))

    def test_specific_exception_handling(self):
        """Test circuit breaker with specific exception types."""
        specific_breaker = CircuitBreaker(failure_threshold=2, recovery_timeout=1, expected_exception=ValueError, name="specific_breaker")

        # ValueError should trigger circuit breaker
        mock_func = Mock(side_effect=ValueError("Expected error"))

        for _ in range(2):
            with self.assertRaises(ValueError):
                specific_breaker.call(mock_func)

        self.assertEqual(specific_breaker.state, CircuitState.OPEN)

        # Different exception should not be caught by circuit breaker
        mock_func.side_effect = RuntimeError("Different error")

        # Reset to test different exception
        specific_breaker.reset()

        # RuntimeError should pass through without affecting circuit
        with self.assertRaises(RuntimeError):
            specific_breaker.call(mock_func)

        # Circuit should still be closed
        self.assertEqual(specific_breaker.state, CircuitState.CLOSED)


class TestPreconfiguredBreakers(unittest.TestCase):
    """Test pre-configured circuit breakers."""

    def test_http_circuit_breaker_exists(self):
        """Test HTTP circuit breaker is properly configured."""
        self.assertEqual(http_circuit_breaker.name, "http_requests")
        self.assertEqual(http_circuit_breaker.failure_threshold, 3)
        self.assertEqual(http_circuit_breaker.recovery_timeout, 30)
        self.assertEqual(http_circuit_breaker.state, CircuitState.CLOSED)

    def test_http_circuit_breaker_usage(self):
        """Test using HTTP circuit breaker."""
        # Reset to ensure clean state
        http_circuit_breaker.reset()

        @with_circuit_breaker(http_circuit_breaker)
        def mock_http_call():
            return "http_success"

        result = mock_http_call()
        self.assertEqual(result, "http_success")


if __name__ == "__main__":
    unittest.main()
