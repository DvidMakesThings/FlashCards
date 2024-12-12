"""
Validation utilities for input checking.
"""

def validate_card_input(category: str, question: str, answer: str) -> tuple[bool, str]:
    """
    Validates the input for a new flashcard.
    
    Args:
        category (str): The category for the flashcard
        question (str): The question text
        answer (str): The answer text
        
    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not category or category == "Select or Add Category":
        return False, "Please select or add a category."
    if not question:
        return False, "Question field cannot be empty."
    if not answer:
        return False, "Answer field cannot be empty."
    return True, ""