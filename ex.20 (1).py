import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

# Laplacian Kernel (Negative Center)
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

# Apply Filter
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen Image
sharpened = cv2.subtract(img, laplacian)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
