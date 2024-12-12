"""
Text processing utilities for string manipulation.
"""
import unicodedata

def normalize_text(text: str) -> str:
    """
    Normalizes text by removing accents, extra spaces, and converting to lowercase.
    
    Args:
        text (str): The text to normalize
        
    Returns:
        str: The normalized text
    """
    # Remove accents and convert to ASCII
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    # Convert to lowercase and remove extra spaces
    text = text.lower().strip()
    # Join with single spaces
    return ' '.join(text.split())