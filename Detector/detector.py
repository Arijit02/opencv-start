import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

filePath = os.path.dirname(__file__)
imagePath = os.path.join(filePath, "../images/road.png")


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255  # , ) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    img = img.copy()
    blank_image = np.zeros_like(img, np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 4)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def process(img):

    height = img.shape[0]
    width = img.shape[1]

    region_of_interest_vertices = [
        (0, height),
        (width/2, height/2),
        (width, height)
    ]

    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_img = cv2.Canny(gray_image, 100, 120)

    cropped_image = region_of_interest(
        canny_img, np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/60, threshold=50, lines=np.array([]),
                            minLineLength=40, maxLineGap=100)

    img_with_lines = draw_the_lines(img, lines)

    # plt.subplot(1, 2, 1), plt.imshow(img)
    # plt.subplot(1, 2, 2), plt.imshow(cropped_image)
    # plt.imshow(img_with_lines)
    # plt.show()
    return img_with_lines


filePath = os.path.dirname(__file__)
videoPath = os.path.join(filePath, "../videos/lane3.mp4")

cap = cv2.VideoCapture(videoPath)

while cap.isOpened():
    _, frame = cap.read()
    frame_with_lines = process(frame)
    cv2.imshow("Road", frame_with_lines)

    k = cv2.waitKey(40)
    if k == 27:
        break


cap.release()
# img = cv2.imread(imagePath, -1)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = process(img)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
cv2.destroyAllWindows()
