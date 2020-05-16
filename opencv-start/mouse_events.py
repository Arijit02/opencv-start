import cv2
import os
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        strXY = f"{x}, {y}"
        cv2.putText(img, strXY, (x, y), font, 1,
                    (255, 255, 0), 2, cv2.LINE_4)
        cv2.imshow('Image', img)
    if event == cv2.EVENT_FLAG_RBUTTON:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        strBGR = f"{red}, {green}, {blue}"
        cv2.putText(img, strBGR, (x, y), font, 1,
                    (0, 255, 255), 2, cv2.LINE_4)
        cv2.imshow('Image', img)


fileDirecPath = os.path.dirname(__file__)
imagePath = os.path.join(fileDirecPath, "../images/lena.jpg")
img = cv2.imread(imagePath, 1)
# img = np.zeros([512, 512, 3], np.uint8)
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
