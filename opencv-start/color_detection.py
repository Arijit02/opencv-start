import cv2
import os
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        mycolorImage = np.zeros([512, 512, 3], np.uint8)

        mycolorImage[:] = [blue, green, red]
        cv2.imshow('color', mycolorImage)


fileDirecPath = os.path.dirname(__file__)
imagePath = os.path.join(fileDirecPath, "../images/lena.jpg")
img = cv2.imread(imagePath, 1)
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
