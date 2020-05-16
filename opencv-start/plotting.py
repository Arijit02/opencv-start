import os
import cv2
from matplotlib import pyplot as plt

fileDirecPath = os.path.dirname(__file__)
imagePath = os.path.join(fileDirecPath, "../images/lena.jpg")

img = cv2.imread(imagePath, 1)
cv2.imshow('OpenCV Image', img)

img_new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_new)
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
