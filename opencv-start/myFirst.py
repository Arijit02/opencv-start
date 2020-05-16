import cv2
import os

fileDirecPath = os.path.dirname(__file__)
imagePath = os.path.join(fileDirecPath, "../images/lena.jpg")

img = cv2.imread(imagePath, 1)
img = cv2.line(img, (0, 0), (300, 300), (255, 0, 0), 15)
img = cv2.line(img, (0, 300), (300, 0), (255, 0, 0), 15)
img = cv2.rectangle(img, (0, 0), (300, 300), (255, 0, 0), 15)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "OpenCV", (10, 500), font, 4, (0, 255, 255), 10)
cv2.imshow('image', img)
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite(os.path.join(fileDirecPath, "../images/lena_copy.png"), img)
    cv2.destroyAllWindows()
