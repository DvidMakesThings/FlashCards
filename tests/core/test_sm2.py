"""
Tests for SM2 algorithm implementation.
"""
import unittest
from datetime import datetime, timedelta
from core.algorithm.sm2 import (
    SM2Data,
    calculate_next_review,
    quality_from_difficulty,
    is_due
)

class TestSM2Algorithm(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.initial_data = SM2Data()
        
    def test_quality_from_difficulty(self):
        """Test difficulty to quality conversion.
        
        Specification:
            Convert user-friendly difficulty ratings to SM2 quality scores
            
        Criteria:
            - 'again' should return 0 (complete blackout)
            - 'hard' should return 2 (answer looked familiar)
            - 'good' should return 3 (correct with difficulty)
            - 'easy' should return 5 (perfect recall)
            - Unknown values should default to 3 (good)
        """
        self.assertEqual(quality_from_difficulty('again'), 0)
        self.assertEqual(quality_from_difficulty('hard'), 2)
        self.assertEqual(quality_from_difficulty('good'), 3)
        self.assertEqual(quality_from_difficulty('easy'), 5)
        self.assertEqual(quality_from_difficulty('unknown'), 3)
        
    def test_calculate_next_review_perfect_recall(self):
        """Test next review calculation for perfect recall.
        
        Specification:
            Calculate next review date for a perfect recall (quality=5)
            
        Criteria:
            - Interval should increase
            - Easiness factor should increase
            - Next review date should be further in the future
        """
        new_data, next_review = calculate_next_review(5, self.initial_data)
        self.assertGreater(new_data.interval, self.initial_data.interval)
        self.assertGreater(new_data.easiness, self.initial_data.easiness)
        self.assertGreater(next_review, datetime.now())
        
    def test_calculate_next_review_poor_recall(self):
        """Test next review calculation for poor recall.
        
        Specification:
            Calculate next review date for poor recall (quality=0)
            
        Criteria:
            - Interval should reset to 1
            - Repetitions should reset to 0
            - Next review should be tomorrow
        """
        new_data, next_review = calculate_next_review(0, self.initial_data)
        self.assertEqual(new_data.interval, 1)
        self.assertEqual(new_data.repetitions, 0)
        expected_next = datetime.now() + timedelta(days=1)
        self.assertLess(abs((next_review - expected_next).total_seconds()), 86400)
        
    def test_is_due_with_no_review(self):
        """Test is_due with no previous review.
        
        Specification:
            Check if a card with no review history is due
            
        Criteria:
            - Should return True when last_review is None
        """
        self.assertTrue(is_due(None, 1))
        
    def test_is_due_with_past_review(self):
        """Test is_due with past review date.
        
        Specification:
            Check if a card with past review date is due
            
        Criteria:
            - Should return True when review date has passed
        """
        past_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
        self.assertTrue(is_due(past_date, 1))
        
    def test_is_due_with_future_review(self):
        """Test is_due with future review date.
        
        Specification:
            Check if a card with future review date is due
            
        Criteria:
            - Should return False when review date is in the future
        """
        future_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        self.assertFalse(is_due(future_date, 1))