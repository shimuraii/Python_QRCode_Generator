import os
import qrcode

img = qrcode.make(input("Enter a link: "))
type(img)  # qrcode.image.pil.PilImage
img.save(input("Enter name of img file: ") + ".png")
