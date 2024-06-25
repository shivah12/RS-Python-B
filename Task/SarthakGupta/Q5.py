import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0);

while True:
    _,frame = cap.read();
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame = cv.Canny(frame,80,150)
    cv.imshow('WebCam',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
