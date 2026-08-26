import cv2

# Read image
img = cv2.imread("image.jpg", 0)

# Sobel Y
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to displayable image
sobely = cv2.convertScaleAbs(sobely)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
