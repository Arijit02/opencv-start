import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/road.png")

img = cv2.imread(imagePath, 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow("Canny", canny)
lines = cv2.HoughLinesP(canny, 1, np.pi/180, 100,
                        minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv2.imshow("Probabilistic Hough Transform", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
