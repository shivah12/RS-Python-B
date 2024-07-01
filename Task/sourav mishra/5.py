import cv2


image_path = 'One Drive/desktop/logo/logo.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

if image is None:
    print("Error: Could not read image.")
    exit()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)


edges = cv2.Canny(blurred, 100, 200)


cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)


cv2.waitKey(0)
cv2.destroyAllWindows()