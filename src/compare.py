from face_processing import get_embedding, recognize_face
import cv2

name = "oleksy"
IMAGE_DIR = f'../test/{name}/images'
RESULT_PATH = f'../test/{name}/results.txt'
file = open(RESULT_PATH, "w")

images = IMAGE_DIR

for i in range(1,11):
    frame = cv2.imread(f'{IMAGE_DIR}/{name}-{i}.png')
    embedding, face_image, box = get_embedding(frame)
    result, similarity = recognize_face(embedding)
    print(result, i)

    line = str(similarity).replace(".",',') + "\n"
    file.write(line)
