"""
Core utilities package initialization.
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