# File: gui/handlers.py
from core.manager import FlashcardManager

class AppHandlers:
    def __init__(self):
        self.manager = FlashcardManager()

    def add_flashcard(self, question, answer):
        self.manager.add_card(question, answer)

    def get_due_cards(self):
        return self.manager.get_due_cards()

    def validate_answer(self, card, user_answer):
        result = card.check_answer(user_answer)
        difficulty = 'easy' if result else 'hard'
        card.update_review(difficulty)
        self.manager.save_cards()
        return result