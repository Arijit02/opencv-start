import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/smarties.png")

img = cv2.imread(imagePath, 0)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones([3, 3], np.uint8)
# kernel2 = np.ones([2, 2], np.uint8)

dialation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel, iterations=2)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel, iterations=2)

titles = ['Original Image', 'Mask', 'Dialation',
          'Erosion', 'Opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dialation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
