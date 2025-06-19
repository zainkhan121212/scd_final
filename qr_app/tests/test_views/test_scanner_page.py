import unittest
import tkinter as tk
from qr_app.app.views.scanner_page import QRCodeScannerPage

class TestScannerPage(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.page = QRCodeScannerPage(self.root, controller=self)
        self.root.update()

    def tearDown(self):
        self.root.destroy()

    def test_ui_layout(self):
        self.assertTrue(hasattr(self.page, 'result_var'))
        self.assertTrue(hasattr(self.page, 'history_listbox'))
