"""
Study screen implementation.
"""
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from core.manager import FlashcardManager
from gui.screens.study.modes import StudyModeType
from gui.screens.study.study_controller import StudyController
from gui.utils.ui_helpers import toggle_widget

class StudyScreen(Screen):
    """Main study screen handling UI interactions."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
        self.category = None
        
    def set_category(self, category: str) -> None:
        """Initialize study controller with selected category."""
        self.category = category
        self.controller = StudyController(self, category)
        self.controller.load_next_card()
        
    def check_answer(self) -> None:
        """Handle answer checking."""
        if self.controller:
            self.controller.check_answer(self.ids.user_input.text)
            
    def handle_difficulty(self, difficulty: str) -> None:
        """Handle difficulty rating in study mode."""
        if self.controller:
            self.controller.handle_difficulty(difficulty)
            
    def start_practice_mode(self) -> None:
        """Switch to practice mode."""
        if self.controller:
            self.controller.switch_mode(StudyModeType.PRACTICE)
            
    def next_practice_card(self) -> None:
        """Load next card in practice mode."""
        if self.controller:
            self.controller.load_next_card()
            
    def reset_ui_state(self) -> None:
        """Reset UI elements to initial state."""
        self.ids.user_input.text = ""
        self.ids.user_input.foreground_color = (0.1, 0.1, 0.4, 1)
        self.ids.feedback_label.text = ""
        toggle_widget(self.ids.check_button, True)
        toggle_widget(self.ids.next_button, False)
        toggle_widget(self.ids.study_buttons, False)
        toggle_widget(self.ids.practice_button, True)