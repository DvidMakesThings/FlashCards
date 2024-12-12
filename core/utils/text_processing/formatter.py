"""
Text formatting utilities.
"""

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