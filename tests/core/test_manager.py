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
        
    def test_add_card(self):
        """Test adding a new card."""
        result = self.manager.add_card(
            question="Test question",
            answer="Test answer",
            category="Test"
        )
        self.assertTrue(result)
        self.assertEqual(len(self.manager.cards), 2)  # Original + reverse
        
    def test_add_duplicate_card(self):
        """Test adding a duplicate card."""
        self.manager.add_card("Q1", "A1", "Test")
        result = self.manager.add_card("Q1", "A1", "Test")
        self.assertFalse(result)
        
    def test_get_due_cards(self):
        """Test retrieving due cards."""
        self.manager.add_card("Q1", "A1", "Test")
        due_cards = self.manager.get_due_cards("Test")
        self.assertEqual(len(due_cards), 2)  # Original + reverse
        
    def test_save_and_load_cards(self):
        """Test saving and loading cards."""
        self.manager.add_card("Q1", "A1", "Test")
        self.manager.save_cards()
        
        # Create new manager instance to test loading
        new_manager = FlashcardManager(storage_path=self.test_dir)
        self.assertEqual(len(new_manager.cards), 2)