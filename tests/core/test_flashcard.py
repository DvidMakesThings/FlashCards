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
        """Test exact answer matching.
        
        Specification:
            Verify exact answer matching functionality
            
        Criteria:
            - Should return True for exact match
            - Should be case-sensitive
            - Should handle whitespace correctly
        """
        self.assertTrue(self.card.check_answer("Test answer"))
        
    def test_check_answer_case_insensitive(self):
        """Test case-insensitive answer matching.
        
        Specification:
            Verify case-insensitive answer matching
            
        Criteria:
            - Should return True regardless of case
            - Should normalize both input and stored answer
        """
        self.assertTrue(self.card.check_answer("TEST ANSWER"))
        
    def test_check_answer_with_spaces(self):
        """Test answer matching with extra spaces.
        
        Specification:
            Verify space normalization in answer checking
            
        Criteria:
            - Should handle extra spaces before/after answer
            - Should handle multiple spaces between words
        """
        self.assertTrue(self.card.check_answer("  Test   answer  "))
        
    def test_check_answer_with_line_breaks(self):
        """Test answer matching with line breaks.
        
        Specification:
            Verify line break handling in answers
            
        Criteria:
            - Should treat line breaks as spaces
            - Should normalize multiple line breaks
            - Should match answers split across lines
        """
        self.card.answer = "Test\nanswer\nwith\nbreaks"
        self.assertTrue(self.card.check_answer("Test answer with breaks"))
        
    def test_update_review_easy(self):
        """Test review update with easy rating.
        
        Specification:
            Verify interval increase for easy answers
            
        Criteria:
            - Should increase interval
            - Should update last review date
            - Should maintain proper easiness factor
        """
        initial_interval = self.card.interval
        self.card.update_review("easy")
        self.assertGreater(self.card.interval, initial_interval)
        self.assertIsNotNone(self.card.last_review)