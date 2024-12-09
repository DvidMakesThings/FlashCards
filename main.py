# File: main.py
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from gui.screens import HomeScreen, StudyScreen, AddCardScreen, CategoryScreen

# Set the window dimensions for the app
Config.set('graphics', 'width', '414')  # Set the screen width to 414px
Config.set('graphics', 'height', '736')  # Set the screen height to 736px

class FlashcardApp(App):
    """
    Main application class for the flashcard app.
    Initializes the screen manager and adds all screens to the app.
    """
    def build(self):
        """
        Build the app by loading the KV file and setting up the screen manager.

        Returns:
            ScreenManager: The screen manager that holds all the app screens.
        """
        Builder.load_file('app.kv')  # Load the KV layout file
        sm = ScreenManager()  # Create a new screen manager to manage the screens
        sm.add_widget(HomeScreen(name='home'))  # Add the Home screen
        sm.add_widget(CategoryScreen(name='category'))  # Add the Category screen
        sm.add_widget(StudyScreen(name='study'))  # Add the Study screen
        sm.add_widget(AddCardScreen(name='add_card'))  # Add the AddCard screen
        return sm  # Return the screen manager to display the screens

# Run the app if the script is executed directly
if __name__ == '__main__':
    __version__ = '1.0.0'  # Set the app version
    FlashcardApp().run()  # Start the FlashcardApp
