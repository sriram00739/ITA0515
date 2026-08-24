import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Read the image
img = cv2.imread("watch.jpg")

# Check image
if img is None:
    print("ERROR: watch.jpg not found!")
    exit()

# Perform object detection
results = model(img)

# Draw detected objects
for result in results:
    for box in result.boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        name = model.names[class_id]

        print("Detected:", name)
        print("Confidence:", confidence)

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        cv2.rectangle(
            img,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            name,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

# Display result
cv2.imshow("Object Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
