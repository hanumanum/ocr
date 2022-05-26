#from PIL import Image #Open, manipulate etc... image
import cv2
from helper_functions import display, grayscale

image_file = "data/2.jpg"
wait_time = 10000

#====00 Opening an Image
#img = cv2.imread(image_file) # rows[columns[r,g,b]] 

#==== 01 Invert
"""
image_file_inverted = "data/2_inverted.jpg"
inverted = cv2.bitwise_not(img)
cv2.imwrite(image_file_inverted, inverted)
"""
#cv2.waitKey(wait_time)

#==== 03 Binarization 
#==== 03.1 grayscale
image_file_grayscaled = "data/2_grayscaled.jpg"
img = cv2.imread(image_file)
image_grayscaled = grayscale(img)
cv2.imwrite(image_file_grayscaled, image_grayscaled)
#display(image_file_grayscaled)

#==== 03.2 binarization
image_file_bw = "data/2_bw.jpg"

thresh, im_bw = cv2.threshold(image_grayscaled, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite(image_file_bw, im_bw)

display(image_file_bw)

# need to play with trashholding params eg. 100, 250
"""
for tr in range(100, 250):
    for mx in range(100, 250):
        img_file_tmp = "data/semples/transholdtest_"+ str(tr)  + "_" + str(mx) + ".jpg"
        thresh, im_bw = cv2.threshold(image_grayscaled, tr, mx, cv2.THRESH_BINARY)
        print(img_file_tmp)
        cv2.imwrite(img_file_tmp, im_bw)
"""
#display(image_file_bw)

#==== 04 noze removal

import numpy as np
kernel = np.ones((2, 2), np.uint8)
print(kernel)