import cv2

from modules.attention_module import detect_attention
from modules.sleep_module import detect_sleep
from modules.phone_module import detect_phone
from modules.analytics_module import save_data


def generate_feedback(
    total_students,
    attentive_students,
    not_attentive_students,
    sleep_detected,
    phone_detected
):
    if total_students == 0:
        return "Feedback: No students detected"

    attention_score = (attentive_students / total_students) * 100

    if phone_detected == 1:
        return "Feedback: Phone usage detected. Ask students to keep phones away."

    if sleep_detected == 1:
        return "Feedback: Drowsiness detected. Take a short interactive break."

    if attention_score < 50:
        return "Feedback: Low attention. Ask a question or change teaching method."

    if attention_score < 75:
        return "Feedback: Moderate attention. Increase student interaction."

    return "Feedback: Good engagement. Continue the lecture."


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    frame, total_students, attentive_students, not_attentive_students = detect_attention(frame)

    frame, sleep_detected = detect_sleep(frame)

    frame, phone_detected = detect_phone(frame)

    feedback = generate_feedback(
        total_students,
        attentive_students,
        not_attentive_students,
        sleep_detected,
        phone_detected
    )

    cv2.putText(
        frame,
        feedback,
        (30, 450),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 0),
        2
    )

    save_data(
        1 if attentive_students > 0 else 0,
        sleep_detected,
        phone_detected,
        total_students,
        attentive_students,
        not_attentive_students,
        feedback
    )

    cv2.imshow("AI Smart Classroom Monitoring System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()