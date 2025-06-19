import unittest
import tkinter as tk
from qr_app.app.views.start_page import StartPage

class DummyController:
    def show_frame(self, _): pass
    def toggle_theme_and_refresh_all(self): pass  # Mock method

class TestStartPage(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.page = StartPage(self.root, controller=DummyController())
        self.root.update()

    def tearDown(self):
        self.root.destroy()

    def test_ui_elements(self):
        self.assertTrue(any(isinstance(w, tk.Button) for w in self.page.winfo_children()))
        self.assertTrue(any(isinstance(w, tk.Label) for w in self.page.winfo_children()))
