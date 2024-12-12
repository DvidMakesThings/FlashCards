from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from core.manager import FlashcardManager
import json
import os

class CategoryScreen(Screen):
    def on_pre_enter(self):
        """Called before entering this screen to update the list of categories."""
        self.update_category_list()

    def update_category_list(self):
        """Update the list of available categories by adding a button for each category."""
        self.ids.category_list.clear_widgets()  # Clear existing buttons
        categories = self.get_available_categories()  # Get available categories
        for category in categories:
            btn = Button(
                text=category,
                size_hint_y=None,
                height='40dp',
                background_color=(0.2, 0.6, 0.9, 1),  # Soft blue background
                color=(1, 1, 1, 1),  # White text for contrast
                font_size='18sp'
            )
            btn.bind(on_press=self.select_category)  # Bind button to select category method
            self.ids.category_list.add_widget(btn)  # Add button to the layout

    def get_available_categories(self):
        """Get all categories from the stored flashcards."""
        storage_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'storage')
        categories = set()  # Use a set to avoid duplicates
        
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
            return ["No categories yet"]
            
        for file in os.listdir(storage_path):
            if file.endswith('.json'):
                with open(os.path.join(storage_path, file), 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        for card in data:
                            if 'category' in card:
                                categories.add(card['category'])
                    except json.JSONDecodeError:
                        continue
                        
        return sorted(categories) if categories else ["No categories yet"]

    def select_category(self, button):
        """Handle the selection of a category and transition to the StudyScreen."""
        category = button.text
        if category != "No categories yet":
            study_screen = self.manager.get_screen('study')
            study_screen.set_category(category)
            self.manager.current = 'study'