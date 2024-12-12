"""
UI feedback utilities for user interaction.
"""
from typing import Tuple

def get_feedback_color(success: bool) -> Tuple[float, float, float, float]:
    """
    Get the appropriate color for feedback messages.
    
    Args:
        success (bool): Whether the operation was successful
        
    Returns:
        Tuple[float, float, float, float]: RGBA color values
    """
    return (0, 0.5, 0, 1) if success else (0.8, 0, 0, 1)

def format_feedback_message(message: str, success: bool = True) -> dict:
    """
    Format a feedback message with appropriate styling.
    
    Args:
        message (str): The message to display
        success (bool): Whether the message indicates success
        
    Returns:
        dict: Message text and color
    """
    return {
        'text': message,
        'color': get_feedback_color(success)
    }