import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from qr_app.app.views.start_page import StartPage
from qr_app.app.views.generator_page import QRCodeGeneratorPage
from qr_app.app.views.scanner_page import QRCodeScannerPage

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Tool")
        self.geometry("600x600")
        self.configure(bg="#ecf0f1")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for Page in (StartPage, QRCodeGeneratorPage, QRCodeScannerPage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

    def toggle_theme_and_refresh_all(self):
        from app import theme
        theme.toggle_theme()
        for frame in self.frames.values():
            if hasattr(frame, "refresh_theme"):
                frame.refresh_theme()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
