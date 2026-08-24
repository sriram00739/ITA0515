import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg", 0)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply opening
opening = cv2.morphologyEx(
    img,
    cv2.MORPH_OPEN,
    kernel
)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Opening", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
