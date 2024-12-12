"""
Tests for StudyScreen functionality.
"""
import unittest
from unittest.mock import MagicMock
from kivy.properties import DictProperty
from gui.screens.study_screen import StudyScreen
from core.flashcard import Flashcard
from gui.screens.study.answer_handler import AnswerHandler
from gui.screens.study.ui_state_manager import UIStateManager
from gui.screens.study.card_display import CardDisplay

class MockWidget:
    """Mock widget for testing."""
    def __init__(self):
        self.text = ""
        self.color = (1, 1, 1, 1)
        self.foreground_color = (0, 0, 0, 1)
        self.disabled = False
        self.opacity = 1

class TestStudyScreen(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.screen = StudyScreen()
        
        # Create mock widgets
        self.screen.ids = {
            'user_input': MockWidget(),
            'feedback_label': MockWidget(),
            'check_button': MockWidget(),
            'next_button': MockWidget(),
            'study_buttons': MockWidget(),
            'question_label': MockWidget()
        }
        
        # Initialize handlers
        self.screen.answer_handler = AnswerHandler(self.screen)
        self.screen.ui_manager = UIStateManager(self.screen)
        self.screen.card_display = CardDisplay(self.screen)
        
        # Mock controller
        self.screen.controller = MagicMock()
        
    def test_check_answer_with_formatting(self):
        """Test answer checking with formatted text.
        
        Specification:
            Verify answer checking with line breaks and formatting
            
        Criteria:
            - Should normalize line breaks
            - Should preserve essential formatting
            - Should match equivalent answers
        """
        # Set up test data with formatted answer
        test_card = Flashcard(
            question="felidegesíti magát",
            answer="mich sich aufregen,\nregte sich auf,\nhat sich aufgeregt über + A",
            category="Test"
        )
        self.screen.controller.current_card = test_card
        
        # Simulate user input with normalized format
        self.screen.ids['user_input'].text = (
            "mich sich aufregen, regte sich auf, hat sich aufgeregt über + A"
        )
        
        # Process answer
        self.screen.check_answer()
        
        # Verify feedback indicates correct answer
        self.assertEqual(
            self.screen.ids['feedback_label'].text,
            "Correct!"
        )