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
            self._handle_incorrect_answer(current_card.answer)

    def _handle_correct_answer(self):
        """Handle correct answer in practice mode."""
        feedback = format_feedback_message("Correct!", True)
        self.screen.ids.feedback_label.text = feedback['text']
        self.screen.ids.feedback_label.color = feedback['color']
        toggle_widget(self.screen.ids.check_button, False)

    def _handle_incorrect_answer(self, correct_answer: str):
        """Handle incorrect answer in practice mode."""
        # Format the display of the correct answer
        formatted_answer = format_display_text(correct_answer)
        feedback = format_feedback_message(f"... is the correct answer", False)
        self.screen.ids.feedback_label.text = feedback['text']
        self.screen.ids.feedback_label.color = feedback['color']
        self.screen.ids.user_input.text = formatted_answer
        self.screen.ids.user_input.foreground_color = (0.8, 0, 0, 1)
        toggle_widget(self.screen.ids.check_button, False)
        toggle_widget(self.screen.ids.next_button, True)