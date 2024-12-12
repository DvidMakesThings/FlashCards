"""
Grammar-specific text processing utilities.
"""
from typing import List, Tuple
from .normalizer import normalize_text

def extract_grammar_parts(text: str) -> List[str]:
    """Extract grammatical components from text."""
    # Normalize first to handle special characters
    text = normalize_text(text)
    # Split by common grammar separators
    parts = text.replace(',', ' , ').split()
    return [part.strip() for part in parts if part.strip()]

def compare_grammar(text1: str, text2: str) -> Tuple[bool, List[str]]:
    """Compare two texts for grammatical equivalence."""
    parts1 = extract_grammar_parts(text1)
    parts2 = extract_grammar_parts(text2)
    
    differences = []
    if len(parts1) != len(parts2):
        differences.append("Different number of components")
        return False, differences
        
    for p1, p2 in zip(parts1, parts2):
        if p1 != p2:
            differences.append(f"Mismatch: '{p1}' vs '{p2}'")
            
    return len(differences) == 0, differences