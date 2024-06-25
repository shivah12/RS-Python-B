import cv2

myimg = cv2.imread('C:\Users\vivek\OneDrive\Pictures\Camera Roll\WIN_20240616_13_03_58_Pro.jpg',cv2.BGR2GRAYSCALE)
edge = cv2.Canny(O_img, 60, 150)

cv2.imshow('Original', myimg)
cv2.imshow('edge', edge)

cv2.waitKey(0)
cv2.destroyAllWindows()
