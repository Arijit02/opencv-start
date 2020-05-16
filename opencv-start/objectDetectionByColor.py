import cv2
import os
import numpy as np


def nothing(x):
    pass


# filePath = os.path.dirname(__file__)
# imagePath = os.path.join(filePath, "../images/smarties.png")

# UPPER = np.zeros([128, 128, 3], np.uint8)
# LOWER = np.zeros([128, 128, 3], np.uint8)

cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
# switch = "0: Lower\n1: Upper"

cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)


while True:

    # img = cv2.imread(imagePath, 1)
    _, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    LH = cv2.getTrackbarPos('LH', 'Tracking')
    LS = cv2.getTrackbarPos('LS', 'Tracking')
    LV = cv2.getTrackbarPos('LV', 'Tracking')
    UH = cv2.getTrackbarPos('UH', 'Tracking')
    US = cv2.getTrackbarPos('US', 'Tracking')
    UV = cv2.getTrackbarPos('UV', 'Tracking')

    # LOWER[:] = [LH, LS, LV]
    # UPPER[:] = [UH, US, UV]

    l_b = np.array([LH, LS, LV])
    u_b = np.array([UH, US, UV])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Image', img)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)
    # cv2.imshow('Upper', UPPER)
    # cv2.imshow('Lower', LOWER)

    k = cv2.waitKey(1)

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
