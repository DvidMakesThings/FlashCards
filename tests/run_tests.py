"""
Test runner script with HTML report generation.
"""
import unittest
import sys
import os
from datetime import datetime
from html_test_runner import HTMLTestRunner

def run_tests():
    """Run all unit tests and generate HTML report."""
    try:
        # Add project root to Python path
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
        
        # Create test suite
        loader = unittest.TestLoader()
        tests = []
        
        # Add test modules explicitly
        test_modules = [
            'tests.core.test_flashcard',
            'tests.core.test_manager',
            'tests.core.test_sm2',
            'tests.core.test_text_processor',
            'tests.gui.test_study_controller',
            'tests.gui.test_study_modes',
            'tests.gui.test_study_screen',
            'tests.gui.test_ui_helpers'
        ]
        
        suite = unittest.TestSuite()
        for module in test_modules:
            try:
                tests = loader.loadTestsFromName(module)
                suite.addTests(tests)
            except Exception as e:
                print(f"Error loading tests from {module}: {e}")
        
        # Run tests with HTML reporter
        runner = HTMLTestRunner(output_dir="test_reports")
        result = runner.run(suite)
        
        # Print summary to console
        print(f"\nTest Summary:")
        print(f"Ran {result.testsRun} tests")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0
        print(f"Success Rate: {success_rate:.2f}%")
        
        return 0 if result.wasSuccessful() else 1
        
    except Exception as e:
        print(f"Error running tests: {str(e)}")
        return 1

if __name__ == '__main__':
    sys.exit(run_tests())