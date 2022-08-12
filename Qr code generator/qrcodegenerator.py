import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # 15 means the version of the qr code high the number bigger the code image and complicated
    box_size = 10, #size of the box where the qr code will be displayed
    border = 5, # it is the white part of image
)

data = "https://open.spotify.com/track/19GqnCuVdOlSPHp6rHdYR2?si=dcGPYpX5SV2pGgttdOnNnQ"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color = "white")
img.save("test.png")
