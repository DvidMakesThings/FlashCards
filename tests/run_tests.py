"""
Test runner script.
"""
import unittest
import sys
import os

def run_tests():
    """Run all unit tests."""
    # Add project root to Python path
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, project_root)
    
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add test modules explicitly
    test_modules = [
        'tests.core.test_flashcard',
        'tests.core.test_manager',
        'tests.core.test_sm2',
        'tests.core.test_text_processor',
        'tests.gui.test_study_controller',
        'tests.gui.test_study_modes',
        'tests.gui.test_ui_helpers'
    ]
    
    for module in test_modules:
        try:
            suite.addTests(unittest.defaultTestLoader.loadTestsFromName(module))
        except Exception as e:
            print(f"Error loading tests from {module}: {e}")
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return non-zero exit code if tests failed
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests())