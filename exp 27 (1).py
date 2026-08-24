import cv2

# Read image
img = cv2.imread("image.jpg")

# Crop a portion of the image
crop = img[50:200, 50:200]

# Copy and paste the cropped portion
img[250:400, 250:400] = crop

# Display
cv2.imshow("Original and Pasted Image", img)
cv2.imshow("Cropped Image", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
