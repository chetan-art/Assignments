import os
from PIL import Image

image1 = Image.open(r"G:\HD Wallpapers\3.jpg")

image2 = image1.convert('RGB')

image2.save(r"G:\MyFirstImage.pdf")


