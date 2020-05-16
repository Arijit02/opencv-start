import cv2
import os
import numpy as np

filePath = os.path.dirname(__file__)
videoPath = os.path.join(filePath, "../videos/vtest.avi")

cap = cv2.VideoCapture(videoPath)
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg = cv2.createBackgroundSubtractorKNN()
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
# print(kernel)

while cap.isOpened():
    _, frame = cap.read()
    if frame is None:
        break

    fgmask = fgbg.apply(frame)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Frame', fgmask)

    k = cv2.waitKey(30)
    if k == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
