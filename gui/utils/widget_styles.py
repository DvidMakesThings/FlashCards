"""
Common styles for widgets.
"""
from typing import Dict, Any

BUTTON_STYLES: Dict[str, Any] = {
    'primary': {
        'background_color': (0.2, 0.6, 0.9, 1),
        'color': (1, 1, 1, 1),
        'font_size': '20sp',
        'height': '60dp'
    },
    'secondary': {
        'background_color': (0.5, 0.8, 0.2, 1),
        'color': (1, 1, 1, 1),
        'font_size': '20sp',
        'height': '60dp'
    }
}

TEXT_INPUT_STYLES: Dict[str, Any] = {
    'default': {
        'font_size': '18sp',
        'height': '48dp',
        'multiline': False,
        'padding': ('10dp', '10dp')
    }
}

LABEL_STYLES: Dict[str, Any] = {
    'title': {
        'font_size': '24sp',
        'height': '40dp',
        'color': (1, 1, 1, 1)
    },
    'section': {
        'font_size': '18sp',
        'height': '30dp',
        'color': (0.2, 0.2, 0.2, 1)
    }
}