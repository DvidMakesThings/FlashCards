"""
Tests for UI helper functions.
"""
import unittest
from kivy.uix.widget import Widget
from gui.utils.ui_helpers import (
    get_feedback_color,
    format_long_text,
    toggle_widget
)

class TestUIHelpers(unittest.TestCase):
    def test_get_feedback_color_success(self):
        """Test feedback color for success."""
        color = get_feedback_color(True)
        self.assertEqual(color, (0, 0.5, 0, 1))
        
    def test_get_feedback_color_failure(self):
        """Test feedback color for failure."""
        color = get_feedback_color(False)
        self.assertEqual(color, (1, 0, 0, 1))
        
    def test_format_long_text(self):
        """Test text formatting."""
        text = "This is a long text that needs to be formatted"
        formatted = format_long_text(text, max_length=20)
        lines = formatted.split('\n')
        self.assertTrue(all(len(line) <= 20 for line in lines))
        
    def test_toggle_widget(self):
        """Test widget visibility toggling."""
        widget = Widget()
        
        # Test showing widget
        toggle_widget(widget, True)
        self.assertFalse(widget.disabled)
        self.assertEqual(widget.opacity, 1)
        
        # Test hiding widget
        toggle_widget(widget, False)
        self.assertTrue(widget.disabled)
        self.assertEqual(widget.opacity, 0)