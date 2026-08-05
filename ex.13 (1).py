import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    pts1 = np.float32([[100,100],
                       [w-100,100],
                       [100,h-100],
                       [w-100,h-100]])

    pts2 = np.float32([[0,0],
                       [w,0],
                       [100,h],
                       [w-100,h]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    output = cv2.warpPerspective(frame, M, (w, h))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Video", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
