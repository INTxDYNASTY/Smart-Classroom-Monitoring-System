from deepface import DeepFace
import cv2
import csv
import time
import os

emotion_file = "emotion_data.csv"

# Create CSV with header if it does not exist
if not os.path.exists(emotion_file):
    with open(emotion_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "emotion"])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        emotion = result[0]["dominant_emotion"]

        # Save emotion data
        with open(emotion_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                time.strftime("%H:%M:%S"),
                emotion
            ])

        cv2.putText(
            frame,
            f"Emotion: {emotion}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    except Exception as e:
        print("Emotion detection error:", e)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()