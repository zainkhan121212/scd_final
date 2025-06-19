# app/theme.py

THEMES = {
    "light": {
        "bg": "#ecf0f1",
        "fg": "#2c3e50",
        "accent": "#3498db",
        "button_fg": "white",
        "tip": "#95a5a6"
    },
    "dark": {
        "bg": "#2c3e50",
        "fg": "#ecf0f1",
        "accent": "#8e44ad",
        "button_fg": "white",
        "tip": "#bdc3c7"
    }
}

# Global theme state
current_theme_name = "light"
current_theme = THEMES[current_theme_name]

def toggle_theme():
    global current_theme_name, current_theme
    current_theme_name = "dark" if current_theme_name == "light" else "light"
    current_theme = THEMES[current_theme_name]
