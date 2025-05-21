import time
import cv2
import db
from face_processing import get_embedding, recognize_face
import os
from pathlib import Path

FREQ = 5  # Frequency of taking frames from camera
WAIT_FOR = 5.0  # seconds

def add_test_img(name, sunglasses, num_tests=100):
    folder_path = Path(f'../test/{name}/images')

    if not folder_path.exists():
        folder_path.mkdir(parents=True)
        print(f"Created folder: {folder_path}")

    i=1     # Image iterator
    start_time = time.time()
    # Real-time face recognition
    cap = cv2.VideoCapture(0)

    while i <= num_tests*FREQ:
        ret, frame = cap.read()
        if not ret:
            break

        elapsed_time = time.time() - start_time
        if elapsed_time <= WAIT_FOR:
            print(f"Saving starts in {round(WAIT_FOR - elapsed_time, 2)} seconds")
        else:
            if i % FREQ == 0:
                image_path = os.path.join(folder_path, f"{name}-{i // FREQ}{"_sunglasses" if sunglasses else ""}.jpg")
                cv2.imwrite(image_path, frame)
                print(f"Saved {i // FREQ} images")
            i+=1

        cv2.imshow('Face Recognition', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):     # Q - quit
            break
    cap.release()
    cv2.destroyAllWindows()
