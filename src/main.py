import cv2
import db
from face_processing import get_embedding, recognize_face
from ui import show_controls, showText
from config import font, fontScale, thickness, lineType, bottomLeftCornerOfText, fontColor
from services import unlockLock

is_authorized = False
has_unlocked = False
similarity = 0

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    ##MODEL
    embedding, face_image, box = get_embedding(frame)
    if not is_authorized:
        match, similarity = recognize_face(embedding)
        if match != "" and match != "unknown":
            is_authorized = True

    ##UI
    if has_unlocked:
        fontColor = (255, 255, 0)
        showText(frame, "unlocked!", 10, 30, fontColor)
    elif is_authorized:
        fontColor = (0, 255, 0)
        showText(frame, f"recognized as {match}", 10, 30, fontColor)
    else:
        showText(frame, f"{similarity}", 10, 30, fontColor)

    show_controls(frame, fontColor)

    if box:
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), fontColor, 2)
        showText(frame, match, x1, y2+20, fontColor)

    ##FUNCTIONALITY
    cv2.imshow('face recognition', frame)
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