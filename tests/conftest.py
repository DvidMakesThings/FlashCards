"""
Test configuration and fixtures.
"""
import pytest
from kivy.core.window import Window
from kivy.base import EventLoop

@pytest.fixture(autouse=True)
def kivy_config():
    """Configure Kivy for testing."""
    Window.size = (800, 600)
    EventLoop.ensure_window()
    return Window

@pytest.fixture
def temp_storage(tmpdir):
    """Provide temporary storage directory."""
    return str(tmpdir)