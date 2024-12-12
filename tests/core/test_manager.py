"""
Tests for FlashcardManager.
"""
import unittest
import os
import tempfile
import shutil
from core.manager import FlashcardManager

class TestFlashcardManager(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.manager = FlashcardManager(storage_path=self.test_dir)
        
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
        
    def test_get_due_cards_by_category(self):
        """Test retrieving due cards by category.
        
        Specification:
            Verify category-specific card retrieval
            
        Criteria:
            - Should only return cards from specified category
            - Should only include due cards
            - Should return both original and reverse cards
        """
        # Add cards to different categories
        self.manager.add_card("Q1", "A1", "Category1")
        self.manager.add_card("Q2", "A2", "Category2")
        
        # Get cards for Category1
        category1_cards = self.manager.get_due_cards("Category1")
        
        # Verify we get both original and reverse cards
        self.assertEqual(len(category1_cards), 2)  # Original + reverse
        self.assertTrue(all(card.category == "Category1" for card in category1_cards))
        
        # Verify card content
        questions = {card.question for card in category1_cards}
        answers = {card.answer for card in category1_cards}
        self.assertEqual(questions, {"Q1", "A1"})
        self.assertEqual(answers, {"A1", "Q1"})