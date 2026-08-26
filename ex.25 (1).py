import cv2

# Read image
img = cv2.imread("image.jpg", 0)

# Compute gradients
grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine gradients
gradient = cv2.addWeighted(cv2.convertScaleAbs(grad_x), 0.5,
                           cv2.convertScaleAbs(grad_y), 0.5, 0)

cv2.imshow("Original", img)
cv2.imshow("Gradient Sharpening", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
