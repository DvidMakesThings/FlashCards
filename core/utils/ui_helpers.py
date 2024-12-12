"""
UI helper functions for text formatting and display.
"""

def format_long_text(text: str, max_length: int = 40) -> str:
    """
    Format long text for display by adding line breaks.
    
    Args:
        text (str): The text to format
        max_length (int): Maximum length per line
        
    Returns:
        str: The formatted text with line breaks
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