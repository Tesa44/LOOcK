import torch
from torchvision import transforms
import numpy as np
from numpy.linalg import norm
from models import detector, resnet
from db import database
from config import SIMILARITY_THRESHOLD
from services import unlockLock

canFetch = False

def preprocess_image(face):
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((160, 160)),
        transforms.ToTensor()
    ])
    return transform(face).unsqueeze(0)

def get_embedding(frame):
    faces, _ = detector.detect(frame)
    if faces is not None:
        for box in faces:
            x1, y1, x2, y2 = map(int, box)
            x1, y1, x2, y2 = max(0, x1), max(0, y1), min(frame.shape[1], x2), min(frame.shape[0], y2)
            face = frame[y1:y2, x1:x2]
            if face is not None and face.size > 0:
                face_tensor = preprocess_image(face)
                with torch.no_grad():
                    embedding = resnet(face_tensor)
                return embedding.squeeze().numpy(), face, (x1, y1, x2, y2)
    return None, None, None

def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))

def recognize_face(embedding):
    global canFetch

    if embedding is None:
        return "No face detected"
    best_match = None
    best_similarity = -1
    for name, stored_embeddings in database.items():
        for stored_embedding in stored_embeddings:
            similarity = cosine_similarity(stored_embedding, embedding)
            print(f"Tried {name}, similarity: {similarity:.4f}")
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = name
    if best_similarity > SIMILARITY_THRESHOLD:
        print(f"Recognized {best_match} with similarity: {best_similarity:.4f}")
        if(canFetch):
            isUnlocked = unlockLock()
            if(isUnlocked): print("Lock successfully unlocked! It can be done only once during the lifecycle of an application")
            else: print("Cannot unlock the lock due to api connection! Please restart an app and try again later")

            canFetch = False

        return f"Recognized: {best_match}"
    print(f"Unknown person. Best match: {best_match}, similarity: {best_similarity:.4f}")
    return "Unknown person"
