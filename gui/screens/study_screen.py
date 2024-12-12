"""
Study screen implementation with SM2 spaced repetition.
"""
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.metrics import dp
from core.manager import FlashcardManager
from core.utils.text_processor import normalize_text
from core.utils.ui_helpers import format_long_text
from core.algorithm.sm2 import is_due
from gui.utils.animation_helpers import show_widget, hide_widget
from gui.utils.ui_feedback import format_feedback_message

class StudyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_manager = None
        self.current_card = None
        self.practice_mode = False
        self.category = None
        self.answer_shown = False

    def set_category(self, category):
        """Set the selected category and load the first card."""
        self.category = category
        self.flashcard_manager = FlashcardManager(category=self.category)
        self.load_next_card()

    def start_practice_mode(self):
        """Start practice mode with all cards in the selected category."""
        if not self.flashcard_manager or not self.flashcard_manager.cards:
            self.ids.question_label.text = "No cards available!"
            return
        self.practice_mode = True
        self.load_next_card()

    def load_next_card(self):
        """Load the next due card in the selected category."""
        if not self.category:
            return

        # Get all cards for the category
        category_cards = self.flashcard_manager.get_due_cards(self.category)
        
        # Filter for due cards if not in practice mode
        if not self.practice_mode:
            due_cards = [
                card for card in category_cards 
                if is_due(card.last_review, card.interval)
            ]
        else:
            due_cards = category_cards

        if due_cards:
            self.current_card = due_cards[0]
            self.ids.question_label.text = format_long_text(self.current_card.question)
            self.reset_ui_state()
            show_widget(self.ids.practice_button)
            self.answer_shown = False
        else:
            self.ids.question_label.text = "No due cards for this category!"
            show_widget(self.ids.practice_button)
            self.current_card = None

    def check_answer(self):
        """Check the user's answer and provide feedback."""
        if not self.current_card or self.answer_shown:
            return

        user_answer = normalize_text(self.ids.user_input.text)
        correct_answer = normalize_text(self.current_card.answer)
        
        self.answer_shown = True
        self.show_difficulty_buttons()

        if user_answer == correct_answer:
            feedback = format_feedback_message("Correct! How easy was it?", True)
            self.ids.feedback_label.text = feedback['text']
            self.ids.feedback_label.color = feedback['color']
        else:
            feedback = format_feedback_message(
                f"The correct answer is: {self.current_card.answer}", 
                False
            )
            self.ids.feedback_label.text = feedback['text']
            self.ids.feedback_label.color = feedback['color']
            self.ids.user_input.text = self.current_card.answer
            self.ids.user_input.foreground_color = (0.8, 0, 0, 1)

    def show_difficulty_buttons(self):
        """Show difficulty rating buttons with animation."""
        hide_widget(self.ids.check_button)
        show_widget(self.ids.difficulty_buttons, height='130dp')

    def handle_difficulty(self, difficulty):
        """Handle difficulty rating and update card."""
        if not self.current_card:
            return

        # Update card with new interval
        self.current_card.update_review(difficulty)
        
        # Save changes
        self.flashcard_manager.save_cards()
        
        # Load next card
        Clock.schedule_once(lambda dt: self.next_question(), 0.5)

    def next_question(self):
        """Load the next question."""
        if self.practice_mode:
            self.flashcard_manager.cards.append(self.flashcard_manager.cards.pop(0))
        
        self.load_next_card()
        self.reset_ui_state()

    def reset_ui_state(self):
        """Reset UI elements to initial state."""
        # Reset input field
        self.ids.user_input.text = ""
        self.ids.user_input.foreground_color = (0.1, 0.1, 0.4, 1)
        
        # Reset feedback
        self.ids.feedback_label.text = ""
        
        # Show check button, hide difficulty buttons
        show_widget(self.ids.check_button)
        hide_widget(self.ids.difficulty_buttons)