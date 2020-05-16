import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/messi5.jpg")

img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['Original Image', 'Laplacian', 'SobelX', 'SobelY', 'Sobel Combined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
