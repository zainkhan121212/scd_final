from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
import os


def save_png(image):
    """
    Opens a file dialog and saves the provided PIL image as PNG.

    Parameters:
    - image (PIL.Image.Image): The image to save.
    """
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")],
            title="Save QR Code as PNG"
        )
        if file_path:
            image.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as PNG:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save PNG: {e}")


def save_pdf(image):
    """
    Opens a file dialog and saves the provided PIL image as a single-page PDF.

    Parameters:
    - image (PIL.Image.Image): The image to embed in the PDF.
    """
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save QR Code as PDF"
        )
        if file_path:
            # Save temporary image
            temp_image = "temp_qr_image.png"
            image.save(temp_image)

            c = canvas.Canvas(file_path)
            c.drawImage(temp_image, 100, 500, width=300, height=300)
            c.save()

            os.remove(temp_image)
            messagebox.showinfo("Success", f"QR code saved as PDF:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save PDF: {e}")
