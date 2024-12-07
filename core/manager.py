import datetime
import os
import json
import random
from core.flashcard import Flashcard
from core.algorithm import is_due


class FlashcardManager:
    def __init__(self, storage_path=None, category=None):
        self.category = category
        self.storage_path = storage_path or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'storage'
        )
        print(f"[DEBUG] Storage path resolved to: {self.storage_path}")
        self.cards = self.load_cards()  # Load cards from the file only when initializing
        print(f"[DEBUG] Loaded {len(self.cards)} cards for category: {self.category or 'All Categories'}")

    def load_cards(self):
        cards = []
        try:
            if not os.path.exists(self.storage_path):
                print(f"[ERROR] Storage path does not exist: {self.storage_path}")
                return cards

            for file in os.listdir(self.storage_path):
                if file.endswith('.json'):
                    file_path = os.path.join(self.storage_path, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        for card in data:
                            if self.category is None or card.get('category') == self.category:
                                cards.append(Flashcard(**card))
            if not cards:
                print(f"[ERROR] No cards found for category: {self.category or 'All Categories'}")
            return cards
        except FileNotFoundError as e:
            print(f"[WARNING] File not found: {e}")
            return cards
        except Exception as e:
            print(f"[ERROR] Unexpected error in load_cards: {str(e)}")
            return cards

    def save_cards(self):
        """Save all cards to a single storage file."""
        try:
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_path)

            file_path = os.path.join(self.storage_path, "data.json")

            # Ensure all cards are dictionaries before saving
            cards_to_save = []
            for card in self.cards:
                if isinstance(card, Flashcard):
                    cards_to_save.append(card.__dict__)
                elif isinstance(card, dict):
                    cards_to_save.append(card)
                else:
                    print(f"[ERROR] Unexpected card format: {card}")
                    continue

            # Save all cards to the single JSON file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(cards_to_save, f, ensure_ascii=False, indent=4)

            print(f"[DEBUG] All cards saved to {file_path}")
        except Exception as e:
            print(f"[ERROR] Failed to save cards: {e}")


    def add_card(self, question, answer, category=None):
        """Add a new card to the list and assign it a category."""
        # Check for duplicates where both question and answer are identical
        for card in self.cards:
            if isinstance(card, Flashcard):
                if card.question == question and card.answer == answer:
                    print(f"[WARNING] Duplicate card detected. Question: '{question}', Answer: '{answer}'")
                    return False  # Indicate failure due to duplicate
            elif isinstance(card, dict):
                if card.get("question") == question and card.get("answer") == answer:
                    print(f"[WARNING] Duplicate card detected. Question: '{question}', Answer: '{answer}'")
                    return False  # Indicate failure due to duplicate

        # Create a new card
        new_card = Flashcard(
            question=question,
            answer=answer,
            category=category or "Uncategorized",
            interval=1,
            last_review=None,
            score=0,
        )
        self.cards.append(new_card)
        self.save_cards()
        print(f"[DEBUG] Added card: {new_card.__dict__}")
        return True  # Indicate success



    def check_duplicates(self, question, answer):
        """Check for duplicate cards by question or answer."""
        for card in self.cards:
            if isinstance(card, Flashcard):
                if card.question == question or card.answer == answer:
                    return True
            elif isinstance(card, dict):
                if card.get("question") == question or card.get("answer") == answer:
                    return True
        return False

    
    def get_due_cards(self, category):
        # Return all cards from the selected category, shuffled
        due_cards = [card for card in self.cards if card.category == category]
        random.shuffle(due_cards)  # Shuffle the cards to randomize the order
        return due_cards
