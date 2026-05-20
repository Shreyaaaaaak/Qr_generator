import qrcode
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=5,
)
qr.add_data("https://github.com/Shreyaaaaaak")
qr.make(fit=True)

img = qr.make_image(fill_color="Pink", back_color="Black")
img.save("github_prof.png")