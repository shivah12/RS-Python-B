#Write a Python script to capture video image from a webcam and differentiate objects of black and white colors by drawing bounding boxes around them using OpenCV.

import cv2
import numpy as np

def checkColour(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 168])
    upper_white = np.array([172, 111, 255])

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([360, 255, 50])

    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    mask_black = cv2.inRange(hsv, lower_black, upper_black)

    return mask_white, mask_black


cap = cv2.VideoCapture(0)

while True:
    flag, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if(flag==False):
        print("No webcam connected!")
        break

    white_mask, black_mask = checkColour(frame)

    contours_white = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_black = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours_white[0]:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 2)

    for contour in contours_black[0]:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 2)

    cv2.imshow('Video Output', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
