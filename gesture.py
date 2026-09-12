import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

def finger_up(lm, tip, pip):
    return lm[tip].y < lm[pip].y

def recognize_gesture(lm):
    index = finger_up(lm, 8, 6)
    middle = finger_up(lm, 12, 10)
    ring = finger_up(lm, 16, 14)
    pinky = finger_up(lm, 20, 18)

    thumb_up = (
        lm[4].y < lm[3].y and
        lm[4].y < lm[2].y and
        lm[4].y < lm[5].y
    )

    if thumb_up and not index and not middle and not ring and not pinky:
        return "THUMBS UP"

    if index and middle and ring and pinky:
        return "OPEN HAND"

    if index and middle and not ring and not pinky:
        return "VICTORY"

    if not index and not middle and not ring and not pinky:
        return "FIST"

    return "UNKNOWN"


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    gesture = "NO HAND"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            gesture = recognize_gesture(
                hand_landmarks.landmark
            )

    cv2.putText(
        frame,
        gesture,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Real-Time Hand Gesture Recognition",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
