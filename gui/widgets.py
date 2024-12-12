"""
Custom widget implementations.
"""
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from gui.utils.widget_styles import BUTTON_STYLES, TEXT_INPUT_STYLES

class StyledButton(Button):
    """Button with predefined styling."""
    
    def __init__(self, style='primary', **kwargs):
        super().__init__(**kwargs)
        self.apply_style(style)

    def apply_style(self, style: str):
        """Apply predefined style to the button."""
        if style in BUTTON_STYLES:
            for key, value in BUTTON_STYLES[style].items():
                setattr(self, key, value)

class StyledTextInput(TextInput):
    """TextInput with predefined styling."""
    
    def __init__(self, style='default', **kwargs):
        super().__init__(**kwargs)
        self.apply_style(style)

    def apply_style(self, style: str):
        """Apply predefined style to the text input."""
        if style in TEXT_INPUT_STYLES:
            for key, value in TEXT_INPUT_STYLES[style].items():
                setattr(self, key, value)