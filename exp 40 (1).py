import cv2

# Read image
img = cv2.imread("image.jpg")

# Select object using mouse
x, y, w, h = cv2.selectROI(
    "Select Object",
    img,
    False
)

# Extract object
object_img = img[y:y+h, x:x+w]

# Draw rectangle
cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

# Display original with rectangle
cv2.imshow("Selected Object", img)

# Display extracted object
cv2.imshow("Extracted Object", object_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
