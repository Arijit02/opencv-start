import cv2
from os import path
import numpy as np
import pytesseract

filePath = path.dirname(__file__)
# imagePath = path.join(filePath, "../images/opencv-logo.png")
imagePath = path.join(filePath, "../images/forest.jpg")

img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((2, 2), np.uint8)
img_gray = cv2.dilate(img_gray, kernel, iterations=1)
img_gray = cv2.erode(img_gray, kernel, iterations=1)

img_gray = cv2.adaptiveThreshold(img_gray, 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

result = pytesseract.image_to_string(img_gray)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", img_gray)

print(result)

cv2.waitKey(0)
cv2.destroyAllWindows()
