import cv2

# Read image
img = cv2.imread("image.jpg")

# Blur image
blur = cv2.GaussianBlur(img, (5,5), 0)

# Unsharp Masking
sharp = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

cv2.imshow("Original", img)
cv2.imshow("Unsharp Masking", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
