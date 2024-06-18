import qrcode
import qrcode.constants

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://portfolio-yasith-rashans-projects.vercel.app/")

img=qr.make_image()
img.save("Scanme.jpg")
