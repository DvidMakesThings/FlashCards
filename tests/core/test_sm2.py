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
        """Test difficulty to quality conversion."""
        self.assertEqual(quality_from_difficulty('again'), 0)
        self.assertEqual(quality_from_difficulty('hard'), 2)
        self.assertEqual(quality_from_difficulty('good'), 3)
        self.assertEqual(quality_from_difficulty('easy'), 5)
        self.assertEqual(quality_from_difficulty('unknown'), 3)  # Default case
        
    def test_calculate_next_review_perfect_recall(self):
        """Test calculation with perfect recall."""
        new_data, next_review = calculate_next_review(5, self.initial_data)
        self.assertGreater(new_data.interval, self.initial_data.interval)
        self.assertGreater(new_data.easiness, self.initial_data.easiness)
        
    def test_calculate_next_review_poor_recall(self):
        """Test calculation with poor recall."""
        new_data, next_review = calculate_next_review(0, self.initial_data)
        self.assertEqual(new_data.interval, 1)
        self.assertEqual(new_data.repetitions, 0)
        
    def test_is_due_with_no_review(self):
        """Test is_due with no previous review."""
        self.assertTrue(is_due(None, 1))
        
    def test_is_due_with_past_review(self):
        """Test is_due with past review date."""
        past_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
        self.assertTrue(is_due(past_date, 1))
        
    def test_is_due_with_future_review(self):
        """Test is_due with future review date."""
        future_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        self.assertFalse(is_due(future_date, 1))