import cv2

# Read image
img = cv2.imread("image.jpg", 0)

# Sobel X
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Convert to displayable image
sobelx = cv2.convertScaleAbs(sobelx)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sobelx)

cv2.waitKey(0)
cv2.destroyAllWindows()
