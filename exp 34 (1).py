import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg", 0)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Top Hat
tophat = cv2.morphologyEx(
    img,
    cv2.MORPH_TOPHAT,
    kernel
)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
