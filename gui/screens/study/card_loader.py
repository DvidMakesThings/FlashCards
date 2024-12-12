"""
Card loading and management functionality.
"""
from typing import List
from core.flashcard import Flashcard
from core.algorithm.sm2 import is_due

class CardLoader:
    """Handles loading and managing flashcards."""
    
    @staticmethod
    def get_due_cards(cards: List[Flashcard], category: str) -> List[Flashcard]:
        """Get cards due for review in a category."""
        category_cards = [card for card in cards if card.category == category]
        return [card for card in category_cards if is_due(card.last_review, card.interval)]

    @staticmethod
    def format_question(card: Flashcard) -> str:
        """Format card question for display."""
        from gui.utils.ui_helpers import format_long_text
        return format_long_text(card.question)