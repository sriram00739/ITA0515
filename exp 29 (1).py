import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg", 0)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
