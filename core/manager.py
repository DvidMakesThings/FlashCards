import datetime
import os
import json
import random
from core.flashcard import Flashcard
from core.algorithm import is_due


class FlashcardManager:
    """
    The FlashcardManager class is responsible for managing the flashcards in the application.
    This includes loading flashcards from storage, saving them, adding new cards, and handling
    card review operations (e.g., shuffling cards, checking duplicates).
    """

    def __init__(self, storage_path=None, category=None):
        """
        Initializes the FlashcardManager object with the specified storage path and category.
        
        Parameters:
            storage_path (str): The directory where the flashcard data is stored.
            category (str): The category of flashcards to be loaded (optional).
        """
        self.category = category
        # Set the storage path (default to 'storage' directory if not provided)
        self.storage_path = storage_path or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'storage'
        )
        print(f"[DEBUG] Storage path resolved to: {self.storage_path}")
        # Load the flashcards from the storage path
        self.cards = self.load_cards()
        print(f"[DEBUG] Loaded {len(self.cards)} cards for category: {self.category or 'All Categories'}")

    def load_cards(self):
        """
        Loads flashcards from JSON files in the specified storage path.
        
        Each card's data is loaded into a list of Flashcard objects.
        
        Returns:
            list: A list of Flashcard objects.
        """
        cards = []
        try:
            # Check if the storage path exists
            if not os.path.exists(self.storage_path):
                print(f"[ERROR] Storage path does not exist: {self.storage_path}")
                return cards

            # Iterate through all files in the storage directory
            for file in os.listdir(self.storage_path):
                if file.endswith('.json'):  # Only load .json files
                    file_path = os.path.join(self.storage_path, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # For each card, check if it matches the desired category (if any)
                        for card in data:
                            if self.category is None or card.get('category') == self.category:
                                cards.append(Flashcard(**card))  # Add the card to the list
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
        """
        Saves all the loaded flashcards to the 'data.json' file in the storage directory.
        
        This method ensures that all the flashcards, including their current state (question, 
        answer, category, etc.), are serialized to a JSON file for persistence.
        """
        try:
            # Ensure the storage directory exists
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_path)

            file_path = os.path.join(self.storage_path, "data.json")

            # Ensure all cards are dictionaries before saving
            cards_to_save = []
            for card in self.cards:
                if isinstance(card, Flashcard):
                    cards_to_save.append(card.__dict__)  # Convert Flashcard object to a dictionary
                elif isinstance(card, dict):
                    cards_to_save.append(card)  # If it's already a dictionary, add it directly
                else:
                    print(f"[ERROR] Unexpected card format: {card}")
                    continue

            # Save the cards list to the 'data.json' file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(cards_to_save, f, ensure_ascii=False, indent=4)

            print(f"[DEBUG] All cards saved to {file_path}")
        except Exception as e:
            print(f"[ERROR] Failed to save cards: {e}")

    def add_card(self, question, answer, category=None):
        """
        Adds a new flashcard to the collection, including a reversed version of the card.
        
        Parameters:
            question (str): The question for the flashcard.
            answer (str): The answer to the question.
            category (str): The category of the flashcard (optional).
        
        Returns:
            bool: True if the card was successfully added, False if a duplicate was detected.
        """
        # Check for duplicates (i.e., cards with the same question and answer)
        for card in self.cards:
            if isinstance(card, Flashcard):
                if card.question == question and card.answer == answer:
                    print(f"[WARNING] Duplicate card detected. Question: '{question}', Answer: '{answer}'")
                    return False  # Indicate failure due to duplicate
            elif isinstance(card, dict):
                if card.get("question") == question and card.get("answer") == answer:
                    print(f"[WARNING] Duplicate card detected. Question: '{question}', Answer: '{answer}'")
                    return False  # Indicate failure due to duplicate

        # Create the original card
        new_card = Flashcard(
            question=question,
            answer=answer,
            category=category or "Uncategorized",
            interval=1,
            last_review=None,
            score=0,
        )
        
        # Create the reversed card (question becomes answer and vice versa)
        reversed_card = Flashcard(
            question=answer,
            answer=question,
            category=category or "Uncategorized",
            interval=1,
            last_review=None,
            score=0,
        )

        # Add both the original and reversed cards to the list
        self.cards.append(new_card)
        self.cards.append(reversed_card)
        
        # Save the updated list of cards
        self.save_cards()
        print(f"[DEBUG] Added cards: {new_card.__dict__} and {reversed_card.__dict__}")
        return True  # Indicate success

    def check_duplicates(self, question, answer):
        """
        Checks whether a card with the given question or answer already exists.
        
        Parameters:
            question (str): The question to check for duplication.
            answer (str): The answer to check for duplication.
        
        Returns:
            bool: True if a duplicate is found, otherwise False.
        """
        for card in self.cards:
            if isinstance(card, Flashcard):
                if card.question == question or card.answer == answer:
                    return True
            elif isinstance(card, dict):
                if card.get("question") == question or card.get("answer") == answer:
                    return True
        return False

    def get_due_cards(self, category):
        """
        Retrieves a list of cards from the specified category and shuffles them for random display.
        
        Parameters:
            category (str): The category from which to fetch due cards.
        
        Returns:
            list: A shuffled list of Flashcard objects from the specified category.
        """
        # Get all cards from the selected category
        due_cards = [card for card in self.cards if card.category == category]
        random.shuffle(due_cards)  # Shuffle the cards to randomize the order
        return due_cards
