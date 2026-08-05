import cv2
import numpy as np

img = cv2.imread("image.jpg")

rows, cols = img.shape[:2]

src = np.float32([[50,50],
                  [300,50],
                  [50,300],
                  [300,300]])

dst = np.float32([[10,100],
                  [250,50],
                  [100,300],
                  [280,280]])

# Homography Matrix
H, status = cv2.findHomography(src, dst)

result = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Homography", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
