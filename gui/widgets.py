# File: gui/widgets.py
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CustomButton(Button):
    """
    Custom button widget with predefined styling.
    Inherits from Kivy's Button class and sets custom font size
    and background color.
    """
    def __init__(self, **kwargs):
        """
        Initializes the custom button with default properties.
        
        Parameters:
            kwargs: Additional properties to pass to the Button class.
        """
        super().__init__(**kwargs)
        self.font_size = '18sp'  # Set the font size of the button text
        self.background_color = (0.2, 0.6, 0.8, 1)  # Set the background color to a soft blue

class CustomTextInput(TextInput):
    """
    Custom text input widget with predefined styling.
    Inherits from Kivy's TextInput class and sets custom font size
    and hint text color.
    """
    def __init__(self, **kwargs):
        """
        Initializes the custom text input with default properties.
        
        Parameters:
            kwargs: Additional properties to pass to the TextInput class.
        """
        super().__init__(**kwargs)
        self.font_size = '16sp'  # Set the font size of the text input text
        self.hint_text_color = (0.5, 0.5, 0.5, 1)  # Set the hint text color to a gray shade
