"""
Special character handling utilities.
"""
import unicodedata
from typing import Dict

def create_char_map() -> Dict[str, str]:
    """Create mapping for special characters."""
    return {
        'ä': 'ae',
        'ö': 'oe',
        'ü': 'ue',
        'ß': 'ss',
        'é': 'e',
        'è': 'e',
        'à': 'a',
        'ù': 'u',
        'ì': 'i',
        'ò': 'o'
    }

def normalize_special_chars(text: str) -> str:
    """
    Normalize special characters while preserving meaning.
    
    Args:
        text: Text containing special characters
        
    Returns:
        Normalized text
    """
    char_map = create_char_map()
    normalized = unicodedata.normalize('NFKD', text)
    
    # Replace known special characters
    for special, replacement in char_map.items():
        normalized = normalized.replace(special, replacement)
        
    return normalized