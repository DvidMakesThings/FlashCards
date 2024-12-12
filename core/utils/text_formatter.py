"""
Utility functions for text formatting.
"""

def format_category_filename(category: str) -> str:
    """
    Format category name for use as filename.
    
    Args:
        category (str): The category name to format
        
    Returns:
        str: Formatted filename (capitalized, spaces replaced with underscores)
    """
    # Replace spaces with underscores and capitalize first letter
    formatted = category.strip().replace(' ', '_')
    return formatted[0].upper() + formatted[1:] if formatted else 'Default'