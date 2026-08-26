import cv2

# Read image
img = cv2.imread("image.jpg")

# Add text watermark
cv2.putText(img,
            "DINESH",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2)

cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
