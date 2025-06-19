import tkinter as tk
from tkinter import messagebox
import cv2
from pyzbar.pyzbar import decode
import datetime
from qr_app.app import theme

class QRCodeScannerPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f7f7f7")
        self.controller = controller
        self.scan_history = []

        tk.Label(self, text="📷 QR Code Scanner", font=("Arial", 20, "bold"), bg="#f7f7f7", fg="#333").pack(pady=20)

        self.result_var = tk.StringVar(value="No QR code scanned yet.")
        tk.Entry(self, textvariable=self.result_var, width=60, font=("Arial", 12), state="readonly").pack(pady=10)

        btn_frame = tk.Frame(self, bg="#f7f7f7")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="📸 Start Scanner", font=("Arial", 11), bg="#27ae60", fg="white", width=18,
                  command=self.scan_in_opencv).grid(row=0, column=0, padx=10)

        tk.Button(btn_frame, text="🗑 Clear History", font=("Arial", 11), bg="#e67e22", fg="white", width=18,
                  command=self.clear_history).grid(row=0, column=1, padx=10)

        tk.Button(btn_frame, text="← Back", font=("Arial", 11), bg="#e74c3c", fg="white", width=18,
                  command=lambda: controller.show_frame(list(controller.frames)[0])).grid(row=0, column=2, padx=10)

        # History label
        tk.Label(self, text="📜 Scan History", font=("Arial", 14, "bold"), bg="#f7f7f7", fg="#444").pack(pady=15)

        # History box
        self.history_listbox = tk.Listbox(self, font=("Consolas", 11), width=75, height=7)
        self.history_listbox.pack(pady=10)

    def scan_in_opencv(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not cap.isOpened():
            messagebox.showerror("Error", "Camera could not be opened.")
            return

        messagebox.showinfo("Scanner", "Hold up a QR code. Press ESC to exit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            decoded = decode(frame)
            print("Decoded:", decoded)  # ← Add this line

            if decoded:
                data = decoded[0].data.decode("utf-8")
                self.result_var.set(data)
                self.add_to_history(data)
                self.copy_to_clipboard(data)
                messagebox.showinfo("✅ QR Code Found", f"Result copied:\n{data}")
                break

            cv2.imshow("📷 QR Scanner - Press ESC to close", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    def copy_to_clipboard(self, data):
        self.clipboard_clear()
        self.clipboard_append(data)

    def add_to_history(self, data):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {data}"
        self.scan_history.append(entry)
        self.history_listbox.insert(tk.END, entry)

    def clear_history(self):
        self.scan_history.clear()
        self.history_listbox.delete(0, tk.END)
