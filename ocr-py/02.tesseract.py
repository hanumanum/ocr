import pytesseract
from PIL import Image

img_file = "/home/hanuman/Desktop/cards/52616e646f6d4956a0e862652c64136faa0f4ebf0f821d925a4acd5e21fec7b2_rotated.jpeg"
img = Image.open(img_file)

orc_result = pytesseract.image_to_string(img)

print(orc_result)