import cv2

O_img = cv2.imread('D:\Python Programming\Miles-Morales-Falling-Spider-Man-Across-the-Spider-Verse-4K-Wallpaper.jpg', cv2.IMREAD_GRAYSCALE)
canny = cv2.Canny(O_img, 90, 180)

cv2.imshow('Original', O_img)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()