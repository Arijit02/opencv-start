import cv2
import os
import datetime
import random

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
filePath = os.path.dirname(__file__)
number = random.randint(1, 100)
videoPath = os.path.join(filePath, f"../videos/myVideo{number}.mp4")
out = cv2.VideoWriter(videoPath, fourcc, 20.0, (640, 480))


while True:
    check, frame = cap.read()
    if check:
        frame = cv2.rectangle(frame, (10, 430), (250, 470), (0, 0, 0), 2)
        font = cv2.FONT_HERSHEY_COMPLEX
        text = "Width : " + str(cap.get(3)) + " Height : " + str(cap.get(4))
        date_time = (datetime.datetime.now()).strftime("%d-%b-%Y %I:%M:%S%p")
        frame = cv2.putText(frame, date_time, (20, 455), font,
                            0.5, (0, 0, 0), 1, cv2.LINE_AA)
        out.write(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Capturing', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
