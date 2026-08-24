import cv2

# Open video
cap = cv2.VideoCapture("video.mp4")

frames = []

# Read all frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Display frames in reverse
for frame in reversed(frames):

    cv2.imshow("Reverse Video", frame)

    # Press Q to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
