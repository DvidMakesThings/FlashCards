"""
Animation utilities for UI transitions.
"""
from kivy.animation import Animation
from kivy.metrics import dp

def _convert_to_dp(value):
    """Convert string height value to dp."""
    if isinstance(value, str) and value.endswith('dp'):
        return dp(float(value[:-2]))
    return value

def create_fade_animation(widget, duration=0.3, **kwargs):
    """
    Create a fade animation for a widget.
    
    Args:
        widget: The widget to animate
        duration (float): Animation duration in seconds
        **kwargs: Additional animation properties
        
    Returns:
        Animation: The created animation
    """
    # Convert height string to dp if present
    if 'height' in kwargs and isinstance(kwargs['height'], str):
        kwargs['height'] = _convert_to_dp(kwargs['height'])
    
    anim = Animation(duration=duration, **kwargs)
    anim.start(widget)
    return anim

def show_widget(widget, height='60dp', duration=0.3):
    """
    Show a widget with animation.
    
    Args:
        widget: The widget to show
        height (str): Target height in dp format (e.g., '60dp')
        duration (float): Animation duration
    """
    create_fade_animation(
        widget,
        duration=duration,
        opacity=1,
        height=_convert_to_dp(height)
    )

def hide_widget(widget, duration=0.3):
    """
    Hide a widget with animation.
    
    Args:
        widget: The widget to hide
        duration (float): Animation duration
    """
    create_fade_animation(
        widget,
        duration=duration,
        opacity=0,
        height=0
    )