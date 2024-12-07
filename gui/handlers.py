# File: gui/handlers.py
from core.manager import FlashcardManager

class AppHandlers:
    """
    This class handles various user interactions related to flashcards.
    It communicates with the FlashcardManager to perform actions such as adding
    flashcards, validating answers, and retrieving due cards.
    """

    def __init__(self):
        """
        Initializes the AppHandlers instance and sets up the FlashcardManager.
        """
        self.manager = FlashcardManager()

    def add_flashcard(self, question, answer):
        """
        Adds a new flashcard to the collection, including a reversed card.
        
        Parameters:
            question (str): The question to be asked on the flashcard.
            answer (str): The answer to the question on the flashcard.
        """
        self.manager.add_card(question, answer)

    def get_due_cards(self):
        """
        Retrieves all the flashcards that are due for review.
        
        Returns:
            list: A list of flashcards that are due for review.
        """
        return self.manager.get_due_cards()

    def validate_answer(self, card, user_answer):
        """
        Validates the user's answer for a given flashcard and updates the review
        status based on whether the answer was correct.
        
        Parameters:
            card (Flashcard): The flashcard being reviewed.
            user_answer (str): The user's answer to the flashcard's question.
        
        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        result = card.check_answer(user_answer)
        difficulty = 'easy' if result else 'hard'
        card.update_review(difficulty)
        self.manager.save_cards()  # Save the updated cards after validation
        return result
