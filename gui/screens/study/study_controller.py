"""
Study controller managing study logic and modes.
"""
from typing import Optional
from kivy.clock import Clock
from core.manager import FlashcardManager
from gui.screens.study.modes import StudyModeType
from gui.screens.study.study_mode import StudyMode
from gui.screens.study.practice_mode import PracticeMode
from gui.screens.study.card_loader import CardLoader

class StudyController:
    """Controls study session flow and mode switching."""
    
    def __init__(self, screen, category: str):
        self.screen = screen
        self.flashcard_manager = FlashcardManager(category=category)
        self.current_card = None
        self.mode_type = StudyModeType.SPACED_REPETITION
        self.study_mode = StudyMode(screen)
        self.practice_mode = PracticeMode(screen)
        
    def load_next_card(self) -> None:
        """Load the next card based on current mode."""
        cards = self.flashcard_manager.get_due_cards(self.screen.category)
        if not cards:
            self.screen.ids.question_label.text = "No cards available!"
            self.current_card = None
            return
            
        self.current_card = cards[0]
        self._update_question_display()
        self.screen.reset_ui_state()
        
    def check_answer(self, user_input: str) -> None:
        """Check answer using current mode."""
        if not self.current_card:
            return
            
        if self.mode_type == StudyModeType.PRACTICE:
            self.practice_mode.check_answer(user_input, self.current_card)
        else:
            self.study_mode.check_answer(user_input, self.current_card)
            
    def handle_difficulty(self, difficulty: str) -> None:
        """Handle difficulty rating and card updates."""
        if not self.current_card or self.mode_type == StudyModeType.PRACTICE:
            return
            
        self.current_card.update_review(difficulty)
        self.flashcard_manager.save_cards()
        Clock.schedule_once(lambda dt: self.load_next_card(), 0.5)
        
    def switch_mode(self, mode_type: StudyModeType) -> None:
        """Switch between study modes."""
        self.mode_type = mode_type
        self.load_next_card()
        
    def _update_question_display(self) -> None:
        """Update the question display."""
        if self.current_card:
            from core.utils.text_processor import format_display_text
            formatted_question = format_display_text(self.current_card.question)
            self.screen.ids.question_label.text = formatted_question