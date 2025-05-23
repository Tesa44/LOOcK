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

import os
import glob

def remove_person_from_database(name):
    if name in database:
        # Usuń osobę z bazy danych
        del database[name]
        save_database(database)
        print(f"{name} został usunięty z bazy danych.")

        # Usuń wszystkie obrazy tej osoby
        image_pattern = os.path.join(IMAGE_DIR, f"{name}_*.jpg")
        images = glob.glob(image_pattern)
        for img_path in images:
            try:
                os.remove(img_path)
                print(f"Usunięto obraz: {img_path}")
            except OSError as e:
                print(f"Błąd podczas usuwania {img_path}: {e}")
    else:
        print(f"{name} nie znajduje się w bazie danych.")

def display_database_contents():
    if not database:
        print("Baza danych jest pusta.")
        return

    print("Zawartość bazy danych:")
    for name, embeddings in database.items():
        print(f"- {name}: {len(embeddings)} zapisanych twarzy")


database = load_database()