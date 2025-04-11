import cv2
import db
from face_processing import get_embedding, recognize_face

# Real-time face recognition
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    embedding, face_image, box = get_embedding(frame)
    result = recognize_face(embedding)
    print(result)

    if box:
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):     # Q - quit
        break
    elif key == ord('a') and result == "Unknown person":    # A - add person to database
        name = input("Enter name: ")
        db.add_face_to_database(name, embedding, face_image)
    elif key == ord('a'):
        print("Face not detected or already recognized. Cannot add to database.")

cap.release()
cv2.destroyAllWindows()