"""
Text processing utilities for answer checking and display formatting.

This module serves as a facade for the text processing package,
providing a simplified interface to the most commonly used functions.
"""
from core.utils.text_processing import (
    normalize_text,
    format_display_text,
    validate_text_input,
    process_answer,
    compare_answers,
    process_line_breaks,
    normalize_special_chars,
    compare_grammar
)

__all__ = [
    'normalize_text',
    'format_display_text', 
    'validate_text_input',
    'process_answer',
    'compare_answers',
    'process_line_breaks',
    'normalize_special_chars',
    'compare_grammar'
]