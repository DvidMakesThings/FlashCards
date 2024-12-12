"""
Tests for Flashcard model.
"""
import unittest
from datetime import datetime
from core.flashcard import Flashcard

class TestFlashcard(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.card = Flashcard(
            question="Test question",
            answer="Test answer",
            category="Test category"
        )
        
    def test_check_answer_exact_match(self):
        """Test exact answer matching."""
        self.assertTrue(self.card.check_answer("Test answer"))
        
    def test_check_answer_case_insensitive(self):
        """Test case-insensitive answer matching."""
        self.assertTrue(self.card.check_answer("TEST ANSWER"))
        
    def test_check_answer_with_spaces(self):
        """Test answer matching with extra spaces."""
        self.assertTrue(self.card.check_answer("  Test   answer  "))
        
    def test_check_answer_incorrect(self):
        """Test incorrect answer."""
        self.assertFalse(self.card.check_answer("Wrong answer"))
        
    def test_update_review_easy(self):
        """Test review update with easy rating."""
        initial_interval = self.card.interval
        self.card.update_review("easy")
        self.assertGreater(self.card.interval, initial_interval)
        self.assertIsNotNone(self.card.last_review)
        
    def test_update_review_hard(self):
        """Test review update with hard rating."""
        self.card.interval = 4  # Set initial interval
        self.card.update_review("hard")
        self.assertLess(self.card.interval, 4)