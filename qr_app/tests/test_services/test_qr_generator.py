import qrcode
from PIL import Image


def generate_qr_code(data, fore_color="#000000", back_color="#ffffff", logo_path=None):
    """
    Generate a QR code with optional foreground/background colors and logo overlay.

    Parameters:
    - data (str): The text or URL to encode.
    - fore_color (str): Foreground color (default: black).
    - back_color (str): Background color (default: white).
    - logo_path (str): Optional path to logo image to embed in the center.

    Returns:
    - PIL.Image.Image: The generated QR code as a PIL image.
    """
    if not data:
        raise ValueError("QR data cannot be empty.")

    # Create QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=fore_color, back_color=back_color).convert('RGB')

    # Add logo if provided
    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            qr_width, qr_height = qr_img.size
            logo_size = qr_width // 4
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            qr_img.paste(logo, pos, mask=logo)
        except Exception as e:
            raise IOError(f"Failed to embed logo: {e}")

    return qr_img
