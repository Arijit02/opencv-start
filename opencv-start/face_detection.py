import cv2 as cv
import os
import numpy as np

filePath = os.path.dirname(__file__)


def detector(img):

    # imagePath = os.path.join(filePath, "../images/messi5.jpg")
    haarcascadePathFace = os.path.join(
        filePath, "../haarcascades/haarcascade_frontalface_default.xml")
    haarcascadePathEye = os.path.join(
        filePath, "../haarcascades/haarcascade_eye_tree_eyeglasses.xml")

    face_cascade = cv.CascadeClassifier(haarcascadePathFace)
    eye_cascade = cv.CascadeClassifier(haarcascadePathEye)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = gray[x:x+w, y:y+h]
        roi_img = img[x:x+w, y:y+h]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    return img


cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    frame = detector(frame)
    cv.imshow("Face", frame)

    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
