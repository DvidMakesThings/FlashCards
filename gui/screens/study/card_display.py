"""
Card display management for study screens.
"""
from core.utils.text_processing import format_display_text

class CardDisplay:
    """Manages card display formatting."""
    
    def __init__(self, screen):
        self.screen = screen
        
    def show_question(self, question: str):
        """Format and display question."""
        formatted = format_display_text(question)
        self.screen.ids.question_label.text = formatted
        
    def show_answer(self, answer: str):
        """Format and display answer."""
        formatted = format_display_text(answer)
        self.screen.ids.user_input.text = formatted
        
    def clear_display(self):
        """Clear question and answer display."""
        self.screen.ids.question_label.text = ""
        self.screen.ids.user_input.text = ""