#Implement a program to detect edges in an image using the Canny edge detector in OpenCV.

#Prototype
import cv2

img = cv2.imread('mango.jpg', 1) #Demo image for testing
img = cv2.resize(img, (800, 600)) #Resizing our image for convenience

canny = cv2.Canny(img, 100, 200)

cv2.imshow('Image',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
