from ultralytics import YOLO
import cv2

# LOAD YOLO MODEL
model = YOLO("yolov8n.pt")

def detect_phone(frame):

    phone_detected = 0

    results = model(frame)

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            # CELL PHONE DETECTION
            if label == "cell phone":

                phone_detected = 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # DRAW BOX
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    2
                )

                # DISPLAY LABEL
                cv2.putText(
                    frame,
                    "PHONE DETECTED",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

    return frame, phone_detected