# TODO: Implement Qr Scanner
import cv2
from pyzbar import pyzbar
from PIL import Image, ImageTk
import numpy as np

def start_camera(page):
    page.cap = cv2.VideoCapture(0)
    page.scanning = True
    update_camera(page)

def stop_camera(page):
    if page.cap and page.cap.isOpened():
        page.cap.release()
    page.camera_label.config(image='')
    page.scanning = False

def update_camera(page):
    if page.scanning and page.cap.isOpened():
        ret, frame = page.cap.read()
        if not ret:
            stop_camera(page)
            return

        frame = cv2.flip(frame, 1)
        decoded = pyzbar.decode(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

        for obj in decoded:
            points = np.array([[p.x, p.y] for p in obj.polygon], np.int32).reshape((-1, 1, 2))
            cv2.polylines(frame, [points], True, (0, 255, 0), 2)
            page.result_text.set(obj.data.decode("utf-8"))
            stop_camera(page)
            break

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgtk = ImageTk.PhotoImage(Image.fromarray(img))
        page.camera_label.imgtk = imgtk
        page.camera_label.configure(image=imgtk)
        page.after(10, lambda: update_camera(page))
