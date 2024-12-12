from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def on_study_press(self):
        """Handle Study button press."""
        self.manager.current = 'category'
        
    def on_add_card_press(self):
        """Handle Add Card button press."""
        self.manager.current = 'add_card'
        
    def on_search_press(self):
        """Handle Search button press."""
        self.manager.current = 'search'