import cv2

# Read image
img = cv2.imread("image.jpg")

# Rotate Clockwise (90°)
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotate Counter Clockwise (90°)
counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter)

cv2.waitKey(0)
cv2.destroyAllWindows()
