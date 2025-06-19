import qrcode
from PIL import Image

def generate_qr_code(data, fore_color, back_color, logo_path=None):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fore_color, back_color=back_color).convert("RGB")

    if logo_path:
        logo = Image.open(logo_path)
        w, h = img.size
        logo_size = w // 4
        logo = logo.resize((logo_size, logo_size))
        pos = ((w - logo_size) // 2, (h - logo_size) // 2)
        img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

    return img
# TODO: Implement Qr Generator
