import cv2
import os
import numpy as np

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/chessboard.png")

img = cv2.imread(imagePath, 1)
img = cv2.resize(img, (840, 840))
cv2.imshow('Image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int64(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
