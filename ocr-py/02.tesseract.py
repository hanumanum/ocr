import pytesseract
from PIL import Image

img_file = "data/2_bw.jpg"
img = Image.open(img_file)

orc_result = pytesseract.image_to_string(img)

print(orc_result)