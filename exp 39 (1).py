import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open video
cap = cv2.VideoCapture("traffic.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects
    results = model.predict(source=frame, verbose=False)

    # Process detections
    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            name = model.names[class_id]

            # Vehicle classes
            if name in ["car", "motorcycle", "bus", "truck"]:

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                # Draw rectangle
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # Display vehicle name
                cv2.putText(
                    frame,
                    name,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

    # Display video
    cv2.imshow("Vehicle Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
