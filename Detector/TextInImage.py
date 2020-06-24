import cv2
from os import path
import numpy as np
import pytesseract

filePath = path.dirname(__file__)
# imagePath = path.join(filePath, "../images/opencv-logo.png")
# imagePath = path.join(filePath, "../images/forest.jpg")
imagePath = path.join(filePath, "../images/newimage.jpg")
# imagePath = path.join(filePath, "../images/digits-alphabets.jpeg")

img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
kernel = np.ones((2, 2), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
img_gray = cv2.dilate(img_gray, kernel, iterations=1)
img_gray = cv2.erode(img_gray, kernel, iterations=1)
# img_gray = cv2.medianBlur(img_gray, 5)

img_gray = cv2.adaptiveThreshold(img_gray, 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


_, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE,
                                          cv2.CHAIN_APPROX_NONE)

file = open("recogniser.txt", "w")
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img_gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cropped = img_gray[x:x+w, y:y+h]
    result = pytesseract.image_to_string(img_gray)
    file = open("recogniser.txt", "a")
    file.write(result)

file.close()

file = open("recogniser.txt", "r")

if file.readable():
    print(file.read())

file.close()'''

print(pytesseract.image_to_string(img_gray))

'''
# Detecting Characters

hImg, wImg = img_gray.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img_gray, config=conf)
for b in boxes.splitlines():
    b = b.split(" ")
    # print(b)

    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 255, 0), 2)
    cv2.putText(img, b[0], (x, hImg-h-10), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 2)'''

'''
# Detecting Words

hImg, wImg = img_gray.shape
boxes = pytesseract.image_to_data(img_gray)
for i, b in enumerate(boxes.splitlines()):
    if i != 0:
        b = b.split()
        # print(b)

    if len(b) == 12:
        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, b[11], (x, y-10), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 2)'''

'''
# Detecting Digits

hImg, wImg = img_gray.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img_gray, config=conf)
for i, b in enumerate(boxes.splitlines()):
    if i != 0:
        b = b.split()
        print(b)

    if len(b) == 12:
        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, b[11], (x, y-10), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 2)'''

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
