import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg", 0)

# Boundary detection kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply convolution
boundary = cv2.filter2D(img, -1, kernel)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Boundary Image", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
