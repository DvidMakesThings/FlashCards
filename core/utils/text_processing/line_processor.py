"""
Line break and formatting processor.
"""

def process_line_breaks(text: str, max_length: int = 40, preserve_breaks: bool = True) -> str:
    """
    Process text with line breaks while preserving meaning.
    
    Args:
        text: Text to process
        max_length: Maximum length per line
        preserve_breaks: Whether to preserve existing line breaks
        
    Returns:
        Processed text with appropriate line breaks
    """
    if preserve_breaks:
        # Replace line breaks with spaces for comparison
        return ' '.join(text.split('\n'))
    
    # Split by existing line breaks first
    parts = text.split('\n')
    
    # Process each part
    processed_parts = []
    for part in parts:
        words = part.split()
        current_line = []
        current_length = 0
        
        for word in words:
            word_length = len(word)
            if current_length + word_length + 1 <= max_length:
                current_line.append(word)
                current_length += word_length + 1
            else:
                if current_line:
                    processed_parts.append(' '.join(current_line))
                current_line = [word]
                current_length = word_length + 1
                
        if current_line:
            processed_parts.append(' '.join(current_line))
            
    return '\n'.join(processed_parts)