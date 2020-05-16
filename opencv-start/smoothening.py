import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/lena.jpg")

img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones([5, 5], np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
mblur = cv2.medianBlur(img, 5)
bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Original Image', '2D Convolution',
          'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gblur, mblur, bilateralfilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
