import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

closed_frames = 0

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

while True:
    ret, frame = cap.read()
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    status = "Awake"
    color = (0,255,0)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:

            # LEFT EYE LANDMARKS
            top = face_landmarks.landmark[159]
            bottom = face_landmarks.landmark[145]

            left = face_landmarks.landmark[33]
            right = face_landmarks.landmark[133]

            # Eye distances
            vertical = distance(top, bottom)
            horizontal = distance(left, right)

            # Eye Aspect Ratio
            ear = vertical / horizontal

            # Draw eye points
            for idx in [159,145,33,133]:
                pt = face_landmarks.landmark[idx]
                cv2.circle(frame,
                           (int(pt.x*w), int(pt.y*h)),
                           2,
                           (0,255,255),
                           -1)

            # Drowsiness logic
            if ear < 0.18:
                closed_frames += 1
            else:
                closed_frames = 0

            if closed_frames > 15:
                status = "DROWSY / SLEEPING"
                color = (0,0,255)

            cv2.putText(frame,
                        f"EAR: {ear:.2f}",
                        (30,80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255,255,255),
                        2)

    cv2.putText(frame,
                status,
                (30,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                2)

    cv2.imshow("Sleep Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()