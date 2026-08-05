import cv2

# Open the built-in webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("Press:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

delay = 30  # Normal speed

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Display the webcam video
    cv2.imshow("Webcam Video Processing", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('n'):
        delay = 30      # Normal speed

    elif key == ord('s'):
        delay = 100     # Slow motion

    elif key == ord('f'):
        delay = 5       # Fast motion

    elif key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
