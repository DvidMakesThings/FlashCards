"""
Test configuration and shared fixtures.
"""
import os
import tempfile
import shutil

def pytest_configure(config):
    """Configure test environment."""
    # Create temp directory for test storage
    os.environ['TEST_STORAGE_DIR'] = tempfile.mkdtemp()

def pytest_unconfigure(config):
    """Clean up test environment."""
    # Remove temp test storage
    test_dir = os.environ.get('TEST_STORAGE_DIR')
    if test_dir and os.path.exists(test_dir):
        shutil.rmtree(test_dir)