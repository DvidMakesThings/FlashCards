"""
Tests for study controller.
"""
import unittest
from unittest.mock import MagicMock, patch
from gui.screens.study.study_controller import StudyController
from gui.screens.study.modes import StudyModeType

class TestStudyController(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.screen = MagicMock()
        self.screen.category = "Test"
        self.controller = StudyController(self.screen, "Test")
        
    def test_switch_mode(self):
        """Test switching study modes."""
        self.controller.switch_mode(StudyModeType.PRACTICE)
        self.assertEqual(self.controller.mode_type, StudyModeType.PRACTICE)
        
    @patch('core.manager.FlashcardManager.get_due_cards')
    def test_load_next_card_no_cards(self, mock_get_cards):
        """Test loading next card when no cards available."""
        mock_get_cards.return_value = []
        self.controller.load_next_card()
        self.assertIsNone(self.controller.current_card)
        self.assertEqual(
            self.screen.ids.question_label.text,
            "No cards available!"
        )
        
    @patch('core.manager.FlashcardManager.get_due_cards')
    def test_load_next_card_with_cards(self, mock_get_cards):
        """Test loading next card with available cards."""
        mock_card = MagicMock()
        mock_card.question = "Test question"
        mock_get_cards.return_value = [mock_card]
        
        self.controller.load_next_card()
        self.assertEqual(self.controller.current_card, mock_card)