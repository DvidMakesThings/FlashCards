"""
Tests for text processing utilities.
"""
import unittest
from core.utils.text_processor import normalize_text, format_display_text

class TestTextProcessor(unittest.TestCase):
    def test_normalize_text_removes_spaces(self):
        """Test that normalize_text removes extra spaces."""
        text = "  hello   world  "
        self.assertEqual(normalize_text(text), "hello world")
        
    def test_normalize_text_handles_line_breaks(self):
        """Test that normalize_text handles line breaks."""
        text = "hello\nworld\r\ntest"
        self.assertEqual(normalize_text(text), "hello world test")
        
    def test_normalize_text_removes_accents(self):
        """Test that normalize_text removes accents."""
        text = "hôtel crémè"
        self.assertEqual(normalize_text(text), "hotel creme")
        
    def test_format_display_text_handles_short_text(self):
        """Test format_display_text with short text."""
        text = "Short text"
        self.assertEqual(format_display_text(text), "Short text")
        
    def test_format_display_text_breaks_long_text(self):
        """Test format_display_text breaks long text appropriately."""
        text = "This is a very long text that should be broken into multiple lines for better display"
        formatted = format_display_text(text, max_length=20)
        self.assertTrue(all(len(line) <= 20 for line in formatted.split('\n')))