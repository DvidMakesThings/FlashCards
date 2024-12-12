"""
Text processing orchestrator.
"""
from .normalizer import normalize_text
from .formatter import format_display_text
from .validator import validate_text_input
from .answer_processor import process_answer, compare_answers
from .line_processor import process_line_breaks
from .special_chars import normalize_special_chars
from .grammar_processor import compare_grammar

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