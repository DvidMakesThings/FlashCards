from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder

# Set the window dimensions for the app
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')

class FlashcardApp(App):
    def build(self):
        """Build the app by loading the KV files and setting up the screen manager."""
        # Load all KV files
        Builder.load_file('app.kv')
        
        # Import here to avoid circular imports
        from gui.utils.screen_manager import ScreenManagerUtil
        
        # Create and return the screen manager
        return ScreenManagerUtil.create_screen_manager()

if __name__ == '__main__':
    FlashcardApp().run()