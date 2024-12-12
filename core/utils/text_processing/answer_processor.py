"""
Answer processing utilities for flashcard validation.
"""
from .normalizer import normalize_text
from .line_processor import process_line_breaks
from .grammar_processor import compare_grammar

def process_answer(answer: str, preserve_formatting: bool = False) -> str:
    """
    Process an answer for comparison or display.
    
    Args:
        answer: Answer text to process
        preserve_formatting: Whether to preserve formatting
        
    Returns:
        Processed answer text
    """
    if preserve_formatting:
        return process_line_breaks(answer)
    return normalize_text(answer)

def compare_answers(user_answer: str, correct_answer: str) -> bool:
    """
    Compare user answer with correct answer.
    
    Args:
        user_answer: User's input answer
        correct_answer: Correct answer to compare against
        
    Returns:
        bool: True if answers match
    """
    # Normalize both answers for comparison
    normalized_user = normalize_text(user_answer)
    normalized_correct = normalize_text(correct_answer)
    
    # First try exact match after normalization
    if normalized_user == normalized_correct:
        return True
        
    # Try comparing with preserved line breaks
    processed_user = process_line_breaks(user_answer)
    processed_correct = process_line_breaks(correct_answer)
    if processed_user == processed_correct:
        return True
        
    # If no exact match, try grammar comparison
    is_match, _ = compare_grammar(user_answer, correct_answer)
    return is_match