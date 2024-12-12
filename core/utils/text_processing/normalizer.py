"""
Text normalization utilities.
"""
import unicodedata

def normalize_text(text: str) -> str:
    """
    Normalize text by removing formatting, extra spaces, and case.
    
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