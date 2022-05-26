from matplotlib import image
from numpy import imag
from helper_functions import display
import pytesseract
import cv2

img_file = "data/2_bw.jpg"
img_file_gray = "data/2_bw_gray.jpg"
img_file_blur = "data/2_bw_blur.jpg"
img_file_thrash = "data/2_bw_trash.jpg"
img_file_dilate = "data/2_bw_dilate.jpg"
img_file_contuers = "data/2_contuers.jpg"

img = cv2.imread(img_file)
height, width, *_ = img.shape
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(img_file_gray, img_gray)

img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
cv2.imwrite(img_file_blur, img_blur)

img_thrash = cv2.threshold(
    img_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite(img_file_thrash, img_thrash)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
img_dilate = cv2.dilate(img_thrash, kernel=kernel, iterations=1)

cv2.imwrite(img_file_dilate, img_dilate)

cnts = cv2.findContours(img_dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# organaize contours from left to right
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

i = 0
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    if w > 20 and h > 10:
        roi = img[y:y+h, x:x+w]
        cv2.imwrite("data/parts/roi_"+str(i)+".jpg", roi)
        i=i+1
        cv2.rectangle(img, (x, y), (x+w, y+h), (36, 255, 12), 2)
cv2.imwrite(img_file_contuers, img)

display(img_file_contuers)
