"""
UI state management for study screens.
"""
from gui.utils.ui_helpers import toggle_widget

class UIStateManager:
    """Manages UI element states."""
    
    def __init__(self, screen):
        self.screen = screen
        
    def reset_state(self):
        """Reset UI to initial state."""
        self.screen.ids.user_input.text = ""
        self.screen.ids.user_input.foreground_color = (0.1, 0.1, 0.4, 1)
        self.screen.ids.feedback_label.text = ""
        toggle_widget(self.screen.ids.check_button, True)
        toggle_widget(self.screen.ids.next_button, False)
        toggle_widget(self.screen.ids.study_buttons, False)
        toggle_widget(self.screen.ids.practice_button, True)
        
    def show_correct_answer_state(self):
        """Update UI for showing correct answer."""
        toggle_widget(self.screen.ids.check_button, False)
        toggle_widget(self.screen.ids.next_button, True)
        
    def show_study_buttons(self):
        """Show difficulty rating buttons."""
        toggle_widget(self.screen.ids.check_button, False)
        toggle_widget(self.screen.ids.study_buttons, True)