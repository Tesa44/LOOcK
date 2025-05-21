import time

import cv2
import db
from face_processing import get_embedding, recognize_face


def add_pattern_img(name, max_num_photos=1):
    num_photos = 0
    # Real-time face recognition
    cap = cv2.VideoCapture(0)
    print("Press A key to add pattern image")
    while num_photos < max_num_photos:
        ret, frame = cap.read()
        if not ret:
            break

        embedding, face_image, box = get_embedding(frame)

        if box:
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow('Face Recognition', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):     # Q - quit
            break
        elif key == ord('a'):    # A - add person to database
            db.add_face_to_database(name, embedding, face_image)
            num_photos += 1
            time.sleep(3)

    cap.release()
    cv2.destroyAllWindows()