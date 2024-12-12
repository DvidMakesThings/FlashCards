"""
Tests for text processing utilities.
"""
import unittest
from core.utils.text_processor import normalize_text, format_display_text

class TestTextProcessor(unittest.TestCase):
    def test_normalize_text_removes_spaces(self):
        """Test space normalization.
        
        Specification:
            Verify space handling in text normalization
            
        Criteria:
            - Should remove leading/trailing spaces
            - Should normalize multiple spaces to single space
        """
        text = "  hello   world  "
        self.assertEqual(normalize_text(text), "hello world")
        
    def test_normalize_text_handles_line_breaks(self):
        """Test line break handling.
        
        Specification:
            Verify line break normalization
            
        Criteria:
            - Should convert line breaks to spaces
            - Should handle different line break types
            - Should normalize multiple line breaks
        """
        text = "hello\nworld\r\ntest"
        self.assertEqual(normalize_text(text), "hello world test")
        
    def test_normalize_text_removes_accents(self):
        """Test accent removal.
        
        Specification:
            Verify accent mark handling
            
        Criteria:
            - Should remove accent marks
            - Should preserve base characters
            - Should handle multiple accented characters
        """
        text = "hôtel crémè"
        self.assertEqual(normalize_text(text), "hotel creme")