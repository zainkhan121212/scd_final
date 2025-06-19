# app/views/generator_page.py
from qr_app.app import theme

import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
import qrcode
import os

class QRCodeGeneratorPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logo_path = None
        self.qr_image = None
        self.fore_color = "#000000"
        self.back_color = "#ffffff"
        self.configure(bg="#ffffff")

        # Back Button
        tk.Button(self, text="← Back", bg="#e74c3c", fg="white", font=("Arial", 10),
                  command=lambda: controller.show_frame(controller.frames.keys().__iter__().__next__())).pack(anchor='nw', padx=10, pady=10)

        # Input
        tk.Label(self, text="Enter text or URL:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        self.input_entry = tk.Entry(self, width=45, font=("Arial", 12))
        self.input_entry.pack(pady=5)

        # Color + Logo Buttons
        btn_frame = tk.Frame(self, bg="#ffffff")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🎨 Foreground", bg="#3498db", fg="white", width=15,
                  command=self.choose_foreground).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="🎨 Background", bg="#9b59b6", fg="white", width=15,
                  command=self.choose_background).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="🖼 Upload Logo", bg="#e67e22", fg="white", width=15,
                  command=self.upload_logo).grid(row=0, column=2, padx=5)

        # Generate Button
        tk.Button(self, text="⚙️ Generate QR Code", bg="#27ae60", fg="white",
                  font=("Arial", 12), command=self.generate_qr).pack(pady=15)

        # QR Image Display
        self.qr_display = tk.Label(self, bg="#ecf0f1")
        self.qr_display.pack(pady=10)

        # Save Buttons
        save_frame = tk.Frame(self, bg="#ffffff")
        save_frame.pack(pady=10)

        tk.Button(save_frame, text="💾 Save as PNG", bg="#2980b9", fg="white", width=20,
                  command=self.save_png).grid(row=0, column=0, padx=10)

        tk.Button(save_frame, text="📄 Save as PDF", bg="#8e44ad", fg="white", width=20,
                  command=self.save_pdf).grid(row=0, column=1, padx=10)

    def choose_foreground(self):
        color = colorchooser.askcolor(title="Choose Foreground Color")[1]
        if color:
            self.fore_color = color

    def choose_background(self):
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            self.back_color = color

    def upload_logo(self):
        self.logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.logo_path:
            messagebox.showinfo("Logo Uploaded", "Logo successfully uploaded!")

    def generate_qr(self):
        data = self.input_entry.get()
        if not data:
            messagebox.showwarning("Input Required", "Please enter text or a URL.")
            return

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fore_color, back_color=self.back_color).convert('RGB')

        if self.logo_path:
            try:
                logo = Image.open(self.logo_path)
                qr_width, qr_height = img.size
                logo_size = qr_width // 4
                logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
                pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
                img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
            except Exception as e:
                messagebox.showerror("Logo Error", f"Couldn't embed logo: {e}")

        self.qr_image = img
        qr_img = ImageTk.PhotoImage(img)
        self.qr_display.config(image=qr_img)
        self.qr_display.image = qr_img

    def save_png(self):
        if self.qr_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if file_path:
                self.qr_image.save(file_path)
                messagebox.showinfo("Saved", f"QR code saved as PNG:\n{file_path}")
        else:
            messagebox.showwarning("No QR Code", "Please generate a QR code first.")

    def save_pdf(self):
        if self.qr_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if file_path:
                temp_image = "temp_qr_image.png"
                self.qr_image.save(temp_image)

                c = canvas.Canvas(file_path)
                c.drawImage(temp_image, 100, 500, width=300, height=300)
                c.save()

                os.remove(temp_image)
                messagebox.showinfo("Saved", f"QR code saved as PDF:\n{file_path}")
        else:
            messagebox.showwarning("No QR Code", "Please generate a QR code first.")
#so there are new cnages
