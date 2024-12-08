# File: unittest/test_flashcards.py
import sys
import os
import unittest
import shutil
from unittest.mock import MagicMock
from tempfile import mkdtemp
from io import StringIO
import logging
from termcolor import colored
import os
from kivy.config import Config
Config.set('graphics', 'window', 'none')  # Disable the window initialization


# Add the root directory (FlashCards) to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from core.flashcard import Flashcard
from core.manager import FlashcardManager
from core.algorithm import calculate_next_review, is_due
from gui.widgets import CustomButton
from gui.handlers import AppHandlers

# Function to generate the formatted HTML report
def write_html_report(report_path, results, debug_messages):
    """
    Generates and writes a formatted HTML report with test results and debug messages.

    Args:
        report_path (str): Path to save the HTML report.
        results (list): List of test results with status and messages.
        debug_messages (list): List of captured debug messages.
    """
    with open(report_path, 'w') as f:
        f.write("<html><head><title>Test Report</title></head><body>")
        f.write("<h1>Test Results</h1>")
        f.write("<table border='1'><tr><th>Test</th><th>Status</th><th>Message</th></tr>")

        # Writing test results
        for result in results:
            if result['status'] == 'pass':
                color = 'green'
            elif result['status'] == 'fail':
                color = 'red'
            else:
                color = 'yellow'

            f.write(f"<tr style='background-color:{color};'>")
            f.write(f"<td>{result['name']}</td><td>{result['status']}</td>")
            if result['status'] == 'fail' or result['status'] == 'error':
                f.write(f"<td>{result['message']}</td>")
            else:
                f.write("<td>N/A</td>")
            f.write("</tr>")

        f.write("</table>")

        # Insert debug messages at the end of the report
        f.write("<h2>Debug Messages</h2>")
        f.write("<pre>")
        for message in debug_messages:
            f.write(message + "\n")
        f.write("</pre>")

        f.write("<p>End of Report</p>")
        f.write("</body></html>")

# Global list to store captured debug messages
debug_messages = []

# Main test class
class TestFlashcards(unittest.TestCase):
    """
    A test class to test the functionality of flashcard management,
    including adding, reviewing, and calculating intervals.
    """
    # Path to original and test data
    original_data_path = os.path.join(project_root, 'storage', 'data.json')
    test_data_path = os.path.join(project_root, 'unittest', 'data_test.json')

    @classmethod
    def setUpClass(cls):
        """Run once before all tests."""
        # Backup original data.json
        cls.temp_dir = mkdtemp()  # Create a temporary directory
        cls.temp_backup = os.path.join(cls.temp_dir, 'data.json')
        
        # Copy the original data.json to a temp directory
        shutil.copy(cls.original_data_path, cls.temp_backup)
        
        # Remove the old test data if it exists
        if os.path.exists(cls.test_data_path):
            os.remove(cls.test_data_path)
        # Copy the original data.json to the unittest folder for testing
        shutil.copy(cls.original_data_path, cls.test_data_path)

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests."""
        # Restore the original data.json from the temp backup
        if os.path.exists(cls.temp_backup):
            shutil.copy(cls.temp_backup, cls.original_data_path)
        
        # Remove the test data file after tests
        if os.path.exists(cls.test_data_path):
            os.remove(cls.test_data_path)
        
        # Clean up the temporary directory
        shutil.rmtree(cls.temp_dir)

    def setUp(self):
        """Run before each test."""
        # Ensure that the test data is fresh before each test
        shutil.copy(self.original_data_path, self.test_data_path)  # Copy fresh data for each test
        self.manager = FlashcardManager(storage_path="unittest")  # Point to the unittest folder

        # Mock the save_cards method to prevent modifying the test data file
        self.manager.save_cards = MagicMock()

        # Redirect stdout to capture print statements
        self._stdout_backup = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Run after each test."""
        # Capture the printed output and store it
        printed_output = sys.stdout.getvalue().strip()
        sys.stdout = self._stdout_backup  # Restore original stdout

        # Add captured output to the global debug_messages list
        debug_messages.append(printed_output)

    def test_check_answer(self):
        """Test the check_answer method in Flashcard."""
        print("Running test_check_answer")
        flashcard = Flashcard("Capital of France?", "Paris", 2, "2024-12-05", 0, "General")
        self.assertTrue(flashcard.check_answer("Paris"))
        self.assertFalse(flashcard.check_answer("London"))

    def test_add_card(self):
        """Test the add_card method in FlashcardManager."""
        print("Running test_add_card")
        result = self.manager.add_card("Unique Test Question 2", "Unique Test Answer 2", "Test Category")
        self.assertTrue(result)  # Ensure the card was added successfully
        self.assertGreater(len(self.manager.cards), 0)

    def test_get_due_cards(self):
        """Test getting the due cards from FlashcardManager."""
        print("Running test_get_due_cards")
        cards = self.manager.get_due_cards("TestData")
        self.assertGreaterEqual(len(cards), 1)

    def test_calculate_next_review(self):
        """Test the calculate_next_review function."""
        print("Running test_calculate_next_review")
        self.assertEqual(calculate_next_review("easy", 2), 4)
        self.assertEqual(calculate_next_review("hard", 2), 1)

    def test_is_due(self):
        """Test the is_due function."""
        print("Running test_is_due")
        self.assertTrue(is_due("2024-12-05", 0))

    def test_custom_button(self):
        """Test the CustomButton widget."""
        print("Running test_custom_button")
        button = CustomButton(text="Click Me")
        self.assertEqual(button.text, "Click Me")

    def test_add_flashcard(self):
        """Test the add_flashcard method in AppHandlers."""
        print("Running test_add_flashcard")
        handlers = AppHandlers()
        handlers.add_flashcard("Test Question", "Test Answer")
        self.assertGreater(len(handlers.manager.cards), 0)

    def test_validate_answer(self):
        """Test the validate_answer method in AppHandlers."""
        print("Running test_validate_answer")
        card = Flashcard("Capital of France?", "Paris", 2, "2024-12-05", 0, "General")
        handlers = AppHandlers()
        self.assertTrue(handlers.validate_answer(card, "Paris"))
        self.assertFalse(handlers.validate_answer(card, "London"))

if __name__ == '__main__':
    # Create the HTML report path
    report_path = os.path.join(project_root, 'unittest', 'reports', 'test_report.html')

    # Run the tests and capture results
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestFlashcards)
    result = unittest.TextTestRunner().run(test_suite)

    # Collect the results in a list
    results = []

    # Collecting errors and failures
    for test, err in result.errors:
        results.append({'name': test._testMethodName, 'status': 'error', 'message': err})
    for test, fail in result.failures:
        results.append({'name': test._testMethodName, 'status': 'fail', 'message': fail})

    # Add passed tests manually (since TextTestResult doesn't have a 'successes' attribute)
    test_names = unittest.defaultTestLoader.getTestCaseNames(TestFlashcards)
    for test in test_names:
        if test not in [e[0] for e in result.errors + result.failures]:
            results.append({'name': test, 'status': 'pass'})

    # Write the formatted HTML report to a file
    write_html_report(report_path, results, debug_messages)

    print(f"Test report saved to: {report_path}")
