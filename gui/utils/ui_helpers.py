"""
Utility functions for UI operations.
"""
from typing import Tuple

def get_feedback_color(success: bool) -> Tuple[float, float, float, float]:
    """
    Returns the appropriate color for feedback messages.
    
    Args:
        success (bool): Whether the operation was successful
        
    Returns:
        Tuple[float, float, float, float]: RGBA color values
    """
    return (0, 0.5, 0, 1) if success else (1, 0, 0, 1)

def format_long_text(text: str, max_length: int = 40) -> str:
    """
    Formats long text for display by adding line breaks.
    
    Args:
        text (str): The text to format
        max_length (int): Maximum length per line
        
    Returns:
        str: The formatted text
    """
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(' '.join(current_line + [word])) <= max_length:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return '\n'.join(lines)