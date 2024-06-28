import cv2

image_path = 'apple.jpg' 
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not read image from path.")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 1.4)
edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()