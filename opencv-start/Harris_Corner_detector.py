import cv2
import os
import numpy as np

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/chessboard.png")

img = cv2.imread(imagePath, 1)
img = cv2.resize(img, (840, 840))
cv2.imshow('Image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
