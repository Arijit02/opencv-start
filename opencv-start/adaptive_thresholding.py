import cv2
import os

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/sudoku.png")

img = cv2.imread(imagePath, 0)

th1 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)

cv2.waitKey(0)

cv2.destroyAllWindows()
