"""
Tests for study modes.
"""
import unittest
from unittest.mock import MagicMock
from gui.screens.study.study_mode import StudyMode
from gui.screens.study.practice_mode import PracticeMode

class TestStudyMode(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.screen = MagicMock()
        self.mode = StudyMode(self.screen)
        
    def test_correct_answer(self):
        """Test handling correct answer."""
        card = MagicMock()
        card.answer = "Test answer"
        self.mode.check_answer("Test answer", card)
        self.assertEqual(
            self.screen.ids.feedback_label.text,
            "Correct!"
        )
        
    def test_incorrect_answer(self):
        """Test handling incorrect answer."""
        card = MagicMock()
        card.answer = "Test answer"
        self.mode.check_answer("Wrong answer", card)
        self.assertEqual(
            self.screen.ids.user_input.foreground_color,
            (0.8, 0, 0, 1)
        )

class TestPracticeMode(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.screen = MagicMock()
        self.mode = PracticeMode(self.screen)
        
    def test_correct_answer_practice(self):
        """Test handling correct answer in practice mode."""
        card = MagicMock()
        card.answer = "Test answer"
        self.mode.check_answer("Test answer", card)
        self.assertEqual(
            self.screen.ids.feedback_label.text,
            "Correct!"
        )
        
    def test_incorrect_answer_practice(self):
        """Test handling incorrect answer in practice mode."""
        card = MagicMock()
        card.answer = "Test answer"
        self.mode.check_answer("Wrong answer", card)
        self.assertTrue(self.screen.ids.next_button.opacity)