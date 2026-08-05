import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

# Get image size
rows, cols = img.shape[:2]

# Move image (Right = 100 pixels, Down = 50 pixels)
M = np.float32([[1, 0, 100],
                [0, 1, 50]])

translated = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
