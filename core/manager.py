import json
from core.flashcard import Flashcard
from core.algorithm import is_due

class FlashcardManager:
    def __init__(self, storage_path="storage/data.json"):
        self.storage_path = storage_path
        self.cards = self.load_cards()

    def load_cards(self):
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:  # Added encoding='utf-8'
                data = json.load(f)
                return [Flashcard(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            # Return an empty list if file is not found or JSON is corrupted
            return []

    def save_cards(self):
        if self.cards:  # Ensure that cards exist before saving
            with open(self.storage_path, 'w', encoding='utf-8') as f:  # Added encoding='utf-8'
                data = [card.__dict__ for card in self.cards]
                json.dump(data, f, indent=4, ensure_ascii=False)  # Added ensure_ascii=False

    def get_due_cards(self):
        return [card for card in self.cards if is_due(card.last_review, card.interval)]

    def add_card(self, question, answer):
        new_card = Flashcard(question, answer)
        self.cards.append(new_card)
        self.save_cards()