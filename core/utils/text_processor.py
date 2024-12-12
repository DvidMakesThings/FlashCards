"""
Text processing utilities for answer checking and display formatting.
"""
import unicodedata
from typing import Tuple

def normalize_text(text: str) -> str:
    """
    Normalize text for comparison by removing formatting, extra spaces, and case.
    
    Args:
        text: Text to normalize
        
    Returns:
        Normalized text suitable for comparison
    """
    # Remove line breaks and extra spaces
    text = ' '.join(text.split())
    
    # Convert to lowercase and remove accents
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    
    return text.strip()

def format_display_text(text: str, max_length: int = 40) -> str:
    """
    Format text for display with line breaks for readability.
    
    Args:
        text: Text to format
        max_length: Maximum length per line
        
    Returns:
        Formatted text with line breaks
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