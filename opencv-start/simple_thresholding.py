import cv2
import os
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/gradient.png")

img = cv2.imread(imagePath, 0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'Binary',
          'Binary_Inv', 'Trunc', 'Tozero', 'Tozero_Inv']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# cv2.imshow('Image', img)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)
# cv2.imshow('th4', th4)
# cv2.imshow('th5', th5)

plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
