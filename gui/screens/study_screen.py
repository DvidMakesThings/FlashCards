"""
Study screen implementation.
"""
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from core.manager import FlashcardManager
from gui.screens.study.modes import StudyModeType
from gui.screens.study.study_controller import StudyController
from gui.screens.study.answer_handler import AnswerHandler
from gui.screens.study.ui_state_manager import UIStateManager
from gui.screens.study.card_display import CardDisplay

class StudyScreen(Screen):
    """Main study screen handling UI interactions."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
        self.category = None
        self.answer_handler = AnswerHandler(self)
        self.ui_manager = UIStateManager(self)
        self.card_display = CardDisplay(self)
        
    def set_category(self, category: str) -> None:
        """Initialize study controller with selected category."""
        self.category = category
        self.controller = StudyController(self, category)
        self.controller.load_next_card()
        
    def check_answer(self) -> None:
        """Handle answer checking."""
        if self.controller and self.controller.current_card:
            user_answer = self.ids.user_input.text
            is_correct = self.answer_handler.process_user_answer(
                user_answer,
                self.controller.current_card.answer
            )
            
            if is_correct:
                self.answer_handler.show_feedback(True)
                Clock.schedule_once(lambda dt: self.handle_difficulty('easy'), 0.5)
            else:
                formatted_answer = self.controller.current_card.answer
                self.answer_handler.show_feedback(False, formatted_answer)
                self.ui_manager.show_study_buttons()
            
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
        self.ui_manager.reset_state()