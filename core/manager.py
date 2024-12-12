"""
Flashcard management system implementation.
"""
import os
from typing import List, Optional
from core.flashcard import Flashcard
from core.utils.file_handler import ensure_storage_dir, load_json_file, save_json_file
from core.utils.text_formatter import format_category_filename
from core.algorithm.sm2 import is_due

class FlashcardManager:
    """Manages flashcard operations and persistence."""
    
    def __init__(self, storage_path: Optional[str] = None, category: Optional[str] = None):
        """Initialize the flashcard manager."""
        self.category = category
        self.storage_path = storage_path or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'storage'
        )
        ensure_storage_dir(self.storage_path)
        self.cards = self._load_cards()

    def _load_cards(self) -> List[Flashcard]:
        """Load flashcards from storage."""
        cards = []
        seen_cards = set()  # Track unique cards to prevent duplicates
        
        # If category is specified, only load that category's file
        if self.category:
            filename = format_category_filename(self.category) + '.json'
            file_path = os.path.join(self.storage_path, filename)
            if os.path.exists(file_path):
                data = load_json_file(file_path)
                for card_data in data:
                    card_id = f"{card_data.get('question')}:{card_data.get('answer')}"
                    if card_id not in seen_cards:
                        cards.append(Flashcard(**card_data))
                        seen_cards.add(card_id)
            return cards
        
        # If no category specified, load all files
        for file in os.listdir(self.storage_path):
            if file.endswith('.json'):
                file_path = os.path.join(self.storage_path, file)
                data = load_json_file(file_path)
                for card_data in data:
                    card_id = f"{card_data.get('question')}:{card_data.get('answer')}"
                    if card_id not in seen_cards:
                        cards.append(Flashcard(**card_data))
                        seen_cards.add(card_id)
        return cards

    def get_due_cards(self, category: str) -> List[Flashcard]:
        """Get due cards for a specific category."""
        # Filter cards by category and due status
        category_cards = [
            card for card in self.cards 
            if card.category == category and is_due(card.last_review, card.interval)
        ]
        return category_cards

    def add_card(self, question: str, answer: str, category: str) -> bool:
        """Add a new flashcard."""
        if self._is_duplicate(question, answer):
            return False

        # Create new cards (original and reverse)
        new_card = Flashcard(question=question, answer=answer, category=category)
        reverse_card = Flashcard(question=answer, answer=question, category=category)
        
        self.cards.extend([new_card, reverse_card])
        self.save_cards()
        return True

    def save_cards(self) -> None:
        """Save flashcards to storage."""
        if not self.category:
            return  # Don't save if no category specified
            
        filename = format_category_filename(self.category) + '.json'
        file_path = os.path.join(self.storage_path, filename)
        
        # Only save cards belonging to this category
        category_cards = [card for card in self.cards if card.category == self.category]
        cards_data = [vars(card) for card in category_cards]
        save_json_file(file_path, cards_data)

    def _is_duplicate(self, question: str, answer: str) -> bool:
        """Check for duplicate cards."""
        return any(
            (card.question == question and card.answer == answer) or
            (card.question == answer and card.answer == question)
            for card in self.cards
        )