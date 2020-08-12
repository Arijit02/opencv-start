import cv2
import numpy as np
from pynput.mouse import Button, Controller
import wx

mouse = Controller()

app = wx.App(False)
(sx, sy) = wx.GetDisplaySize()
(camx, camy) = (320, 240)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, camx)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, camy)

lowerBound = np.array([32, 80, 40])
upperBound = np.array([102, 255, 255])

kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

pinchFlag = 0

openx, openy, openw, openh = (0, 0, 0, 0)

mLocOld = np.array([0, 0])
mouseLoc = np.array([0, 0])
DampingFactor = 2

while True:

    _, frame = cam.read()
    # frame = cv2.resize(frame, (340, 220))

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)

    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelClose)

    maskFinal = maskClose

    cnts, _ = cv2.findContours(
        maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(cnts) == 2:
        if pinchFlag == 1:
            pinchFlag = 0
            mouse.release(Button.left)
        x1, y1, w1, h1 = cv2.boundingRect(cnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(cnts[1])
        cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5)
        cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 5)
        cx1 = x1 + int(w1/2)
        cy1 = y1 + int(h1/2)
        cx2 = x2 + int(w2/2)
        cy2 = y2 + int(h2/2)
        cx = int((cx1 + cx2)/2)
        cy = int((cy1 + cy2)/2)
        cv2.line(frame, (cx1, cy1), (cx2, cy2), (255, 0, 0), 5)
        cv2.circle(frame, (cx, cy), 2, (0, 0, 255), 5)
        mouseLoc = mLocOld + ((cx, cy) - mLocOld) / DampingFactor
        mouse.position = (sx-(mouseLoc[0]*sx/camx), mouseLoc[1]*sy/camy)
        mLocOld = mouseLoc
        openx, openy, openw, openh = cv2.boundingRect(
            np.array([[x1, y1], [x1 + w1, y1 + h1], [x2, y2], [x2 + w2, y2 + h2]]))

    if len(cnts) == 1:
        x, y, w, h = cv2.boundingRect(cnts[0])
        if pinchFlag == 0:
            if abs((w*h - openw*openh)/(w*h)) < 30:
                pinchFlag = 1
                mouse.press(Button.left)
                openx, openy, openw, openh = (0, 0, 0, 0)
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
                cx = x + int(w/2)
                cy = y + int(h/2)
                cv2.circle(frame, (cx, cy), int((w + h)/4), (0, 0, 255), 5)
                mouseLoc = mLocOld + ((cx, cy) - mLocOld) / DampingFactor
                mouse.position = (
                    sx-(mouseLoc[0]*sx/camx), mouseLoc[1]*sy/camy)
                mLocOld = mouseLoc

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", maskFinal)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
