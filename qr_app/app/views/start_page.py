# app/views/start_page.py

import tkinter as tk
from qr_app.app.views.generator_page import QRCodeGeneratorPage
from qr_app.app.views.scanner_page import QRCodeScannerPage
from qr_app.app import theme
from PIL import Image, ImageTk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logo = None
        self.render_ui()

    def render_ui(self):
        self.configure(bg=theme.current_theme["bg"])
        for widget in self.winfo_children():
            widget.destroy()

        try:
            logo_img = Image.open("logo.png")
            logo_img = logo_img.resize((80, 80), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(self, image=self.logo, bg=theme.current_theme["bg"]).pack(pady=(30, 10))
        except:
            tk.Label(self, text="🔳", font=("Arial", 40), bg=theme.current_theme["bg"]).pack(pady=(30, 10))

        tk.Label(self, text="QR Toolkit", font=("Helvetica", 26, "bold"),
                 bg=theme.current_theme["bg"], fg=theme.current_theme["fg"]).pack(pady=(10, 5))

        tk.Label(self, text="Smart QR Code Generator & Scanner", font=("Arial", 14),
                 bg=theme.current_theme["bg"], fg=theme.current_theme["tip"]).pack(pady=(0, 25))

        self.create_button("🖨 Generate QR Code", QRCodeGeneratorPage, "#27ae60").pack(pady=10)
        self.create_button("📷 Scan QR Code", QRCodeScannerPage, "#2980b9").pack(pady=10)

        tk.Button(self, text="🌓 Toggle Theme", font=("Arial", 11),
                  bg=theme.current_theme["accent"], fg=theme.current_theme["button_fg"],
                  command=self.controller.toggle_theme_and_refresh_all).pack(pady=20)

        tk.Label(self, text="Tip: Hold phone steady when scanning QR codes!",
                 font=("Arial", 10, "italic"),
                 bg=theme.current_theme["bg"], fg=theme.current_theme["tip"]).pack(side="bottom", pady=15)

    def create_button(self, text, target_page, color):
        return tk.Button(
            self,
            text=text,
            font=("Arial", 14),
            bg=color,
            fg="white",
            activebackground="#34495e",
            activeforeground="white",
            width=25,
            height=2,
            bd=0,
            relief="ridge",
            command=lambda: self.controller.show_frame(target_page)
        )

    def refresh_theme(self):
        self.render_ui()
