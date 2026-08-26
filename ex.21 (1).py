import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

# Laplacian Kernel with diagonal neighbors
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

lap = cv2.filter2D(img, -1, kernel)

# Sharpen image
sharpen = cv2.subtract(img, lap)

cv2.imshow("Original", img)
cv2.imshow("Sharpened", sharpen)

cv2.waitKey(0)
cv2.destroyAllWindows()
