import cv2

image = cv2.imread('image.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)

cv2.imshow('Original Image', image)
cv2.imshow('Detected Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
