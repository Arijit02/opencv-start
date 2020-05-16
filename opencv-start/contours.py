import cv2
import os
import numpy as np

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/opencv-logo.png")

img = cv2.imread(imagePath, 1)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

_, contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_NONE
)

print("Number of contours : ", str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("Image", img)
cv2.imshow("Gray-Image", imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()
