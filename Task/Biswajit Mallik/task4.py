import cv2
import numpy as np

def detect_black_white_objects(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, black_thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    _, white_thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    black_contours, _ = cv2.findContours(black_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in black_contours:
        if cv2.contourArea(contour) > 100: 
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) 
    
    white_contours, _ = cv2.findContours(white_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in white_contours:
        if cv2.contourArea(contour) > 100:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) 
    
    return frame

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video stream from webcam.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame from webcam.")
        break
    
    frame_with_boxes = detect_black_white_objects(frame)
    cv2.imshow('Black and White Object Detection', frame_with_boxes)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
