import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    refine_landmarks=True,
    max_num_faces=5,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def detect_attention(frame):
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    total_students = 0
    attentive_students = 0
    not_attentive_students = 0

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            total_students += 1

            # ---------------- FACE WIDTH ----------------
            left_face = face_landmarks.landmark[234]
            right_face = face_landmarks.landmark[454]

            left_x = int(left_face.x * w)
            right_x = int(right_face.x * w)

            face_center = (left_x + right_x) // 2

            # ---------------- NOSE ----------------
            nose = face_landmarks.landmark[1]
            nose_x = int(nose.x * w)
            nose_y = int(nose.y * h)

            # ---------------- EYE ----------------
            left_eye_outer = face_landmarks.landmark[33]
            left_eye_inner = face_landmarks.landmark[133]
            iris = face_landmarks.landmark[468]

            outer_x = int(left_eye_outer.x * w)
            inner_x = int(left_eye_inner.x * w)
            iris_x = int(iris.x * w)
            iris_y = int(iris.y * h)

            eye_center = (outer_x + inner_x) // 2

            # ---------------- DRAW POINTS ----------------
            cv2.circle(frame, (nose_x, nose_y), 4, (0, 255, 0), -1)
            cv2.circle(frame, (iris_x, iris_y), 3, (0, 255, 255), -1)

            # ---------------- ATTENTION LOGIC ----------------
            head_offset = abs(nose_x - face_center)
            eye_offset = abs(iris_x - eye_center)

            head_ok = head_offset < 30
            eye_ok = eye_offset < 5

            # ---------------- EYE VISIBILITY CHECK ----------------
            y1 = max(0, iris_y - 5)
            y2 = min(h, iris_y + 5)
            x1 = max(0, iris_x - 5)
            x2 = min(w, iris_x + 5)

            eye_region = frame[y1:y2, x1:x2]

            if eye_region.size != 0:
                avg_intensity = eye_region.mean()
            else:
                avg_intensity = 255

            eye_visible = avg_intensity >= 60

            # ---------------- FINAL DECISION ----------------
            if not eye_visible:
                if head_ok:
                    status = "Eyes Not Visible"
                    color = (0, 255, 255)
                else:
                    status = "Not Attentive"
                    color = (0, 0, 255)
                    not_attentive_students += 1
            else:
                if head_ok and eye_ok:
                    status = "Attentive"
                    color = (0, 255, 0)
                    attentive_students += 1
                else:
                    status = "Not Attentive"
                    color = (0, 0, 255)
                    not_attentive_students += 1

            # ---------------- STATUS PER STUDENT ----------------
            cv2.putText(
                frame,
                status,
                (max(10, nose_x - 80), max(30, nose_y - 40)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

        # ---------------- CLASSROOM ANALYTICS ----------------
        if total_students > 0:
            attention_score = int((attentive_students / total_students) * 100)
        else:
            attention_score = 0

        cv2.putText(frame, f"Students: {total_students}", (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

        cv2.putText(frame, f"Attentive: {attentive_students}", (30, 110),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.putText(frame, f"Not Attentive: {not_attentive_students}", (30, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        cv2.putText(frame, f"Attention Score: {attention_score}%", (30, 170),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

    else:
        cv2.putText(frame, "No Face", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    return frame, total_students, attentive_students, not_attentive_students