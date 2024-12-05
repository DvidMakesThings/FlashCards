# File: gui/screens.py
from kivy.uix.screenmanager import Screen
from core.manager import FlashcardManager
from kivy.animation import Animation
from kivy.clock import Clock
import unicodedata

class HomeScreen(Screen):
    pass

class StudyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_manager = FlashcardManager()
        self.current_card = None
        self.practice_mode = False  # Indicates whether we are in practice mode

    def on_enter(self):
        if self.practice_mode:
            self.load_all_cards()
        else:
            self.load_next_card()

    def load_next_card(self):
        due_cards = self.flashcard_manager.get_due_cards()

        if due_cards:
            self.current_card = due_cards.pop(0)  # Get the next card
            self.ids.question_label.text = self.current_card.question
            self.ids.feedback_label.text = ""
            self.ids.feedback_label.color = 1, 1, 1, 1  # Reset color
            self.ids.user_input.text = ""
            self.hide_next_button()
            self.hide_practice_button()
        else:
            self.current_card = None
            self.ids.question_label.text = "No cards to review today!"
            self.show_practice_button()

    def load_all_cards(self):
        cards = self.flashcard_manager.cards
        if cards:
            self.current_card = cards[0]  # Get the next card for practice
            self.ids.question_label.text = self.current_card.question
            self.ids.feedback_label.text = ""
            self.ids.feedback_label.color = 1, 1, 1, 1  # Reset color
            self.ids.user_input.text = ""
            self.hide_next_button()
        else:
            self.current_card = None
            self.ids.question_label.text = "No more cards to practice!"
            self.practice_mode = False

    def normalize_text(self, text):
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8').lower()

    def check_user_answer(self):
        if not self.current_card:
            return
        user_answer = self.normalize_text(self.ids.user_input.text)
        correct_answer = self.normalize_text(self.current_card.answer)
        if user_answer == correct_answer:
            self.ids.feedback_label.text = "Correct!"
            self.ids.feedback_label.color = 0, 0.5, 0, 1  # Darker green for correct answer
            if not self.practice_mode:
                self.current_card.update_review("easy")
            self.flashcard_manager.save_cards()
            Clock.schedule_once(lambda dt: self.next_question(), 0.5)  # Wait 0.5 seconds before loading the next question
        else:
            self.ids.feedback_label.text = f"Incorrect! Correct answer: {self.current_card.answer}"
            self.ids.feedback_label.color = 1, 0, 0, 1  # Red for incorrect answer
            if not self.practice_mode:
                self.current_card.update_review("hard")
            self.flashcard_manager.save_cards()
            self.show_next_button()  # Show "Next" button so user can control the flow

    def show_next_button(self):
        self.ids.next_button.opacity = 1
        self.ids.next_button.size_hint_y = None
        self.ids.next_button.height = '60dp'

    def hide_next_button(self):
        self.ids.next_button.opacity = 0
        self.ids.next_button.size_hint_y = None
        self.ids.next_button.height = '0dp'

    def show_practice_button(self):
        self.ids.practice_button.opacity = 1

    def hide_practice_button(self):
        self.ids.practice_button.opacity = 0

    def start_practice_mode(self):
        self.practice_mode = True
        self.load_all_cards()

    def next_question(self):
        if self.practice_mode:
            self.flashcard_manager.cards.append(self.flashcard_manager.cards.pop(0))  # Move current card to end for endless mode
            self.load_all_cards()
        else:
            self.load_next_card()

class AddCardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_manager = FlashcardManager()

    def save_card(self):
        question = self.ids.question_input.text
        answer = self.ids.answer_input.text
        if question and answer:
            self.flashcard_manager.add_card(question, answer)
            self.ids.question_input.text = ""
            self.ids.answer_input.text = ""
