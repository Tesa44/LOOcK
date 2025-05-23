import cv2
import db
from face_processing import get_embedding, recognize_face
from services import unlockLock

# Real-time face recognition
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,30)
fontScale              = 1
fontColor              = (0,0,255)
thickness              = 1
lineType               = 2

is_authorized = False
has_unlocked = False
similarity = 0

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if not is_authorized:
        embedding, face_image, box = get_embedding(frame)
        match, similarity = recognize_face(embedding)
        if match != "" and match != "unknown":
            is_authorized = True

    if has_unlocked:
        fontColor = (255, 255, 0)
        cv2.putText(frame, f"unlocked!",
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness + 1,
                    lineType)
    elif is_authorized:
        fontColor = (0, 255, 0)
        cv2.putText(frame, f"recognized as {match}",
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness + 1,
                    lineType)
    else:
        cv2.putText(frame, f"{similarity}",
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness + 1,
                    lineType)

    cv2.putText(frame, "[a] to add reference",
                (10, 350),
                font,
                fontScale,
                fontColor,
                thickness + 1,
                lineType)

    cv2.putText(frame, "[u] to unlock lock",
                (10, 400),
                font,
                fontScale,
                fontColor,
                thickness + 1,
                lineType)

    cv2.putText(frame, "[q] to quit",
                (10, 450),
                font,
                fontScale,
                fontColor,
                thickness + 1,
                lineType)

    if not is_authorized:
        if box:
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), fontColor, 2)
            cv2.putText(frame, match,
                        (x1, y2 + 20),
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)

    cv2.imshow('Face Recognition', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):     # Q - quit
        break
    elif key == ord('a') and is_authorized is False:    # A - add person to database
        name = input("Enter name: ")
        db.add_face_to_database(name, embedding, face_image)
    elif key == ord('u') and is_authorized is True and not has_unlocked:
        has_unlocked = True
        # unlockLock()

cap.release()
cv2.destroyAllWindows()