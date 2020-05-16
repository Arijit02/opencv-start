import cv2
import os
import numpy as np

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/lena.jpg")

img = cv2.imread(imagePath, 1)
gp_lr1 = cv2.pyrDown(img)
gp_lr2 = cv2.pyrDown(gp_lr1)

gp_expanded = cv2.pyrUp(gp_lr2)

lp_1 = cv2.subtract(gp_lr1, gp_expanded)

cv2.imshow("Original Image", img)
cv2.imshow("First LR", gp_lr1)
cv2.imshow("Second LR", gp_lr2)
cv2.imshow("Second LR expanded", gp_expanded)
cv2.imshow("First Laplacian", lp_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
