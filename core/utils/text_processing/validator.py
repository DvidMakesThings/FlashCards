"""
Text validation utilities.
"""

def validate_text_input(text: str, min_length: int = 1, max_length: int = 1000) -> tuple[bool, str]:
    """
    Validate text input.
    
    Args:
        text: Text to validate
        min_length: Minimum allowed length
        max_length: Maximum allowed length
        
    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    text = text.strip()
    
    if not text:
        return False, "Text cannot be empty"
        
    if len(text) < min_length:
        return False, f"Text must be at least {min_length} characters"
        
    if len(text) > max_length:
        return False, f"Text cannot exceed {max_length} characters"
        
    return True, ""