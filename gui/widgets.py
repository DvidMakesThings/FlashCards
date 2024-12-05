# File: gui/widgets.py
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '18sp'
        self.background_color = (0.2, 0.6, 0.8, 1)

class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '16sp'
        self.hint_text_color = (0.5, 0.5, 0.5, 1)