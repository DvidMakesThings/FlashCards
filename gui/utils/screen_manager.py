"""
Utility functions for screen management.
"""
from typing import Dict, Any
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenManagerUtil:
    @staticmethod
    def create_screen_manager() -> ScreenManager:
        """
        Creates and initializes the screen manager with all screens.
        
        Returns:
            ScreenManager: The initialized screen manager
        """
        sm = ScreenManager()
        
        # Import screens here to avoid circular imports
        from gui.screens.home_screen import HomeScreen
        from gui.screens.category_screen import CategoryScreen
        from gui.screens.study_screen import StudyScreen
        from gui.screens.add_card_screen import AddCardScreen
        from gui.screens.search_screen import SearchScreen
        
        # Add all screens
        screens = {
            'home': HomeScreen,
            'category': CategoryScreen,
            'study': StudyScreen,
            'add_card': AddCardScreen,
            'search': SearchScreen
        }
        
        for name, screen_class in screens.items():
            sm.add_widget(screen_class(name=name))
        
        return sm