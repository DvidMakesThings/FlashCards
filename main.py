# File: main.py

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from gui.screens import HomeScreen, StudyScreen, AddCardScreen

# Set the window size to a 9:16 ratio for a smartphone-like appearance
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')

class FlashcardApp(App):
    def build(self):
        Builder.load_file('app.kv')
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(StudyScreen(name='study'))
        sm.add_widget(AddCardScreen(name='add_card'))
        return sm


if __name__ == '__main__':
    FlashcardApp().run()
