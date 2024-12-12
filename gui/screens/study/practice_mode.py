"""
Practice mode implementation without affecting card statistics.
"""
from kivy.clock import Clock
from core.utils.text_processor import normalize_text, format_display_text
from gui.utils.ui_helpers import toggle_widget
from gui.utils.ui_feedback import format_feedback_message

class PracticeMode:
    def __init__(self, screen):
        self.screen = screen

    def check_answer(self, user_input: str, current_card) -> None:
        """Handle answer checking in practice mode."""
        # Normalize both answers for comparison
        normalized_input = normalize_text(user_input)
        normalized_answer = normalize_text(current_card.answer)
        
        if normalized_input == normalized_answer:
            self._handle_correct_answer()
        else:
            # Format the display of the correct answer
            formatted_answer = format_display_text(current_card.answer)
            self._handle_incorrect_answer(formatted_answer)

    def _handle_correct_answer(self) -> None:
        """Handle correct answer by showing feedback and advancing."""
        feedback = format_feedback_message("Correct!", True)
        self.screen.ids.feedback_label.text = feedback['text']
        self.screen.ids.feedback_label.color = feedback['color']
        toggle_widget(self.screen.ids.check_button, False)
        # Automatically advance to next card after delay
        Clock.schedule_once(lambda dt: self.screen.next_practice_card(), 0.5)

    def _handle_incorrect_answer(self, formatted_answer: str) -> None:
        """Show correct answer and next button for incorrect answers."""
        feedback = format_feedback_message(f"Is the correct answer:", False)
        self.screen.ids.feedback_label.text = feedback['text']
        self.screen.ids.feedback_label.color = feedback['color']
        self.screen.ids.user_input.text = formatted_answer
        self.screen.ids.user_input.foreground_color = (0.8, 0, 0, 1)
        toggle_widget(self.screen.ids.check_button, False)
        toggle_widget(self.screen.ids.next_button, True)