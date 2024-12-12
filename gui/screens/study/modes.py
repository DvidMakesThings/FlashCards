"""
Study mode types and shared functionality.
"""
from enum import Enum, auto

class StudyModeType(Enum):
    """Enumeration of study mode types."""
    PRACTICE = auto()
    SPACED_REPETITION = auto()

class BaseMode:
    """Base class for study modes with shared functionality."""
    def __init__(self, screen):
        self.screen = screen

    def reset_ui(self) -> None:
        """Reset UI elements to initial state."""
        self.screen.ids.user_input.text = ""
        self.screen.ids.user_input.foreground_color = (0.1, 0.1, 0.4, 1)
        self.screen.ids.feedback_label.text = ""