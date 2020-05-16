import cv2
import os
import numpy as np

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/smarties.png")

img = cv2.imread(imagePath, -1)
output = img.copy
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT,
                           1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
rounded_circles = np.uint16(np.around(circles))
for (x, y, r) in rounded_circles[0, :]:
    cv2.circle(img, (x, y), r, (0, 255, 0), 3)
    cv2.circle(img, (x, y), 2, (0, 255, 255), -1)


cv2.imshow("Image HoughCircle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
