import unittest
import tkinter as tk
from qr_app.app.views.generator_page import QRCodeGeneratorPage

class TestGeneratorPage(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.page = QRCodeGeneratorPage(self.root, controller=self)

    def test_has_entry(self):
        self.assertTrue(hasattr(self.page, 'input_entry'))

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
