import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/lena.jpg")
img = cv2.imread(imagePath, 0)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# b, g, r = cv2.split(img)

# img = np.zeros([200, 200], np.uint8)
# cv2.imshow("Image", img)
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)

# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
