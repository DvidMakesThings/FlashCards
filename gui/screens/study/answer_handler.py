"""
Answer handling logic for study screens.
"""
from core.utils.text_processing import (
    process_answer,
    compare_answers,
    format_display_text
)
from gui.utils.ui_feedback import format_feedback_message

class AnswerHandler:
    """Handles answer processing and feedback."""
    
    def __init__(self, screen):
        self.screen = screen
        
    def process_user_answer(self, user_input: str, correct_answer: str) -> bool:
        """
        Process and validate user answer.
        
        Args:
            user_input: User's answer
            correct_answer: Correct answer to compare against
            
        Returns:
            bool: True if answer is correct
        """
        processed_input = process_answer(user_input)
        return compare_answers(processed_input, correct_answer)
        
    def show_feedback(self, is_correct: bool, formatted_answer: str = None):
        """Display feedback for answer."""
        if is_correct:
            feedback = format_feedback_message("Correct!", True)
            self.screen.ids.feedback_label.text = feedback['text']
            self.screen.ids.feedback_label.color = feedback['color']
        else:
            feedback = format_feedback_message("... is the correct answer", False)
            self.screen.ids.feedback_label.text = feedback['text']
            self.screen.ids.feedback_label.color = feedback['color']
            if formatted_answer:
                self.screen.ids.user_input.text = formatted_answer
                self.screen.ids.user_input.foreground_color = (0.8, 0, 0, 1)