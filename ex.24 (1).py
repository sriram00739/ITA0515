import cv2

# Read image
img = cv2.imread("image.jpg")

# Blur image
blur = cv2.GaussianBlur(img, (5,5), 0)

# High-Boost Sharpening
highboost = cv2.addWeighted(img, 2.0, blur, -1.0, 0)

cv2.imshow("Original", img)
cv2.imshow("High Boost", highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()
