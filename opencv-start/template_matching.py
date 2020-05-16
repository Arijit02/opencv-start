import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath1 = os.path.join(filePath, "../images/messi5.jpg")
imagePath2 = os.path.join(filePath, "../images/messi_face.jpg")

img = cv2.imread(imagePath1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread(imagePath2, 0)
w, h = template.shape[::-1]

print(template.shape)

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, ((pt[0] + w), (pt[1] + h)), (0, 255, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
