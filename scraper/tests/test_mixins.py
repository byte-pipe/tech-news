"""Tests for mixin classes."""

import unittest
from unittest.mock import MagicMock


class TestResourceManagerMixin(unittest.TestCase):
    def _make_concrete(self):
        from scraper.utils.mixins import ResourceManagerMixin

        class Concrete(ResourceManagerMixin):
            def __init__(self):
                self.closed = False

            def close(self):
                self.closed = True

        return Concrete()

    def test_context_manager_enter_returns_self(self):
        obj = self._make_concrete()
        result = obj.__enter__()
        assert result is obj

    def test_context_manager_exit_calls_close(self):
        obj = self._make_concrete()
        obj.__exit__(None, None, None)
        assert obj.closed is True

    def test_del_calls_close(self):
        obj = self._make_concrete()
        obj.__del__()
        assert obj.closed is True

    def test_del_ignores_exception_from_close(self):
        from scraper.utils.mixins import ResourceManagerMixin

        class Broken(ResourceManagerMixin):
            def close(self):
                raise RuntimeError("cleanup failed")

        obj = Broken()
        obj.__del__()  # Should not raise

    def test_close_not_implemented_raises(self):
        from scraper.utils.mixins import ResourceManagerMixin
        obj = ResourceManagerMixin()
        with self.assertRaises(NotImplementedError):
            obj.close()


class TestSessionManagerMixin(unittest.TestCase):
    def _make_session_obj(self):
        from scraper.utils.mixins import SessionManagerMixin

        class SessionObj(SessionManagerMixin):
            def __init__(self):
                self.session = MagicMock()

        return SessionObj()

    def test_close_closes_session(self):
        obj = self._make_session_obj()
        obj.close()
        obj.session.close.assert_called_once()

    def test_close_handles_session_exception(self):
        obj = self._make_session_obj()
        obj.session.close.side_effect = Exception("session error")
        obj.close()  # Should not raise

    def test_context_manager_closes_session(self):
        obj = self._make_session_obj()
        with obj:
            pass
        obj.session.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
