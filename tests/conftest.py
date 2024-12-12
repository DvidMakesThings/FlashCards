"""
Test configuration and shared fixtures.
"""
import os
import tempfile
import shutil
import pytest
from kivy.config import Config

# Configure Kivy for testing
Config.set('graphics', 'window_state', 'hidden')
Config.set('graphics', 'headless', '1')

@pytest.fixture(autouse=True)
def test_env():
    """Set up test environment."""
    # Create temp directory for test storage
    test_dir = tempfile.mkdtemp()
    os.environ['TEST_STORAGE_DIR'] = test_dir
    
    yield
    
    # Clean up after tests
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

@pytest.fixture
def temp_storage(tmpdir):
    """Provide temporary storage directory."""
    return str(tmpdir)