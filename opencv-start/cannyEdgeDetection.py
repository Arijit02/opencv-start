import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/messi5.jpg")
tracker = cv2.namedWindow('Tracking')
cv2.createTrackbar('Th1', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('Th2', 'Tracking', 0, 255, nothing)

while True:
    th1 = cv2.getTrackbarPos('Th1', 'Tracking')
    th2 = cv2.getTrackbarPos('Th2', 'Tracking')

    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    canny = cv2.Canny(img, th1, th2)

    # titles = ['Original Image', 'Canny']
    # images = [img, canny]
#
    # for i in range(2):
    # plt.subplot(1, 2, i+1), plt.imshow(images[i], "gray")
    # plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])
#
    # plt.show()

    cv2.imshow('Original Image', img)
    cv2.imshow('Canny', canny)

    k = cv2.waitKey(1)
    if k == 27:
        break

# plt.close()
cv2.destroyAllWindows()
