import cv2
import numpy as np

cap = cv2.VideoCapture(0)

yello_lower = np.array([22, 93, 0])
yello_upper = np.array([45, 255, 255])

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yello_lower, yello_upper)
    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)

    if cv2.waitKey(10) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
