import cv2
import pickle
import os
from config import DB_PATH, IMAGE_DIR

# Load or initialize the database
def load_database():
    # Ensure image database directory exists
    os.makedirs(IMAGE_DIR, exist_ok=True)
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as f:
            db = pickle.load(f)
            return {k: v if isinstance(v, list) else [v] for k, v in db.items()}
    return {}

def save_database(db):
    with open(DB_PATH, "wb") as f:
        pickle.dump(db, f)

def add_face_to_database(name, embedding, face_image):
    if embedding is not None and face_image is not None:
        if name in database:
            database[name].append(embedding)  # Adds new face image to person list
        else:
            database[name] = [embedding]  # Generate new list for new person
        save_database(database)
        image_path = os.path.join(IMAGE_DIR, f"{name}_{len(database[name])}.jpg")
        cv2.imwrite(image_path, face_image)
        print(f"Added {name} to database with image saved at {image_path}.")
    else:
        print("No valid face detected to add.")

database = load_database()