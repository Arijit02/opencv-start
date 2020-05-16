import cv2
import os
import numpy as np

# Image loading

filePath = os.path.dirname(__file__)
imagePath1 = os.path.join(filePath, "../images/apple.jpg")
imagePath2 = os.path.join(filePath, "../images/orange.jpg")

apple = cv2.imread(imagePath1, 1)
orange = cv2.imread(imagePath2, 1)

# Gaussian pyramid

layer_apple = apple.copy()
layer_orange = orange.copy()

gp_apple = [layer_apple]
gp_orange = [layer_orange]

for i in range(6):
    layer_apple = cv2.pyrDown(layer_apple)
    gp_apple.append(layer_apple)
    layer_orange = cv2.pyrDown(layer_orange)
    gp_orange.append(layer_orange)

# Laplacian pyramid

apple_copy = gp_apple[5].copy()
orange_copy = gp_orange[5].copy()

lp_apple = [apple_copy]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    gp_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gp_expanded)
    lp_apple.append(laplacian)
    gp_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gp_expanded)
    lp_orange.append(laplacian)

# Stacking

apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    rows, cols, ch = apple_lap.shape
    blend = np.hstack(
        (apple_lap[:, :np.uint8(cols/2)], orange_lap[:, np.uint8(cols/2):]))
    apple_orange_pyramid.append(blend)


# Reconstruct

apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(
        apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("Reconstructed", apple_orange_reconstruct)
cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
# cv2.imshow("Apple-Orange", apple_orange)

cv2.waitKey(0)
cv2.destroyAllWindows()
