import cv2

# Read image
img = cv2.imread("image.jpg", 0)

# Apply Canny Edge Detection
edges = cv2.Canny(img, 100, 200)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
