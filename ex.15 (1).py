import cv2
import numpy as np

img = cv2.imread("image.jpg")

rows, cols = img.shape[:2]

src = np.float32([[50,50],
                  [300,50],
                  [50,300],
                  [300,300]])

dst = np.float32([[0,0],
                  [250,20],
                  [50,300],
                  [300,280]])

# DLT estimates the homography from point correspondences
H, status = cv2.findHomography(src, dst, method=0)

result = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("DLT Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
