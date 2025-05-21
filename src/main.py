import time

import cv2
import db
from face_processing import get_embedding, recognize_face
import os

test = True
sunglasses = True
name = "oleksy"
IMAGE_DIR = f'../test/{name}/images'
RESULT_PATH = f'../test/{name}/results.txt'
NUM_TESTS = 100
file = open(RESULT_PATH, "w")
i=1
freq = 5
wait_for = 5.0 # seconds
start_time = time.time()
# Real-time face recognition
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if  i > NUM_TESTS*freq:
        break

    embedding, face_image, box = get_embedding(frame)
    result, similarity = recognize_face(embedding)
    # print(result)

    if box:
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    if (time.time() - start_time > wait_for):
        if test and i % freq == 0:
            image_path = os.path.join(IMAGE_DIR, f"{name}-{i // freq}{"_sunglasses" if sunglasses else ""}.jpg")
            cv2.imwrite(image_path, frame)
            line = str(similarity).replace(".",',') + "\n"
            file.write(line)
            print("writing")
        i+=1

    cv2.imshow('Face Recognition', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):     # Q - quit
        break
    elif key == ord('a') and result == "Unknown person":    # A - add person to database
        name = input("Enter name: ")
        db.add_face_to_database(name, embedding, face_image)
    elif key == ord('a'):
        print("Face not detected or already recognized. Cannot add to database.")

file.close()
cap.release()
cv2.destroyAllWindows()