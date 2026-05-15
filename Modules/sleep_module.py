import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh

face_mesh_sleep = mp_face_mesh.FaceMesh(
    refine_landmarks=True,
    max_num_faces=5,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

closed_frames = 0

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def detect_sleep(frame):
    global closed_frames

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh_sleep.process(rgb)

    sleep_detected = 0
    status = "Awake"
    color = (0, 255, 0)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:

            top = face_landmarks.landmark[159]
            bottom = face_landmarks.landmark[145]
            left = face_landmarks.landmark[33]
            right = face_landmarks.landmark[133]

            vertical = distance(top, bottom)
            horizontal = distance(left, right)

            if horizontal == 0:
                continue

            ear = vertical / horizontal

            if ear < 0.25:
                closed_frames += 1
            else:
                closed_frames = 0

            if closed_frames > 10:
                sleep_detected = 1
                status = "DROWSY / SLEEPING"
                color = (0, 0, 255)

            cv2.putText(frame, f"EAR: {ear:.2f}", (30, 210),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    cv2.putText(frame, status, (30, 240),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    return frame, sleep_detected