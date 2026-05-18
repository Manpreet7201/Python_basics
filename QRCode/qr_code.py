# https://staff.blu-maritime.com/

# import segno
# data = "https://staff.blu-maritime.com/"
# qr = segno.make(data)
# qr.save(
#     "company_qr.png",
#     scale=10,
#     dark="blue",
#     light="white"
# )
# print("QR code Generated.")

import segno
from PIL import Image
data = "https://staff.blu-maritime.com/"
qr = segno.make(data,error='h')  #errro recovery ability
qr.save(
    "temp_qr.png",
    scale=10,
    dark="#3F758F",
    light="white"
)

qr_img = Image.open('temp_qr.png')
logo = Image.open('logo.png')
logo_size = 120
logo = logo.resize((logo_size, logo_size))

qr_width, qr_height = qr_img.size
pos = ((qr_width-logo_size)//2, (qr_height-logo_size)//2)

qr_img.paste(logo, pos, mask=logo)
qr_img.save("company_qr.png")

print("QR Code with logo generated successfully")