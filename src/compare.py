from face_processing import get_embedding, recognize_face
import cv2



def compare(name, sunglasses, num_tests, num_patterns=False):
    image_folder_path = f'../test/{name}/images'
    result_path = f'../test/{name}/results{"_sunglasses" if sunglasses else ""}{"-"+str(num_patterns) if num_patterns else ""}.txt'
    file = open(result_path, "w")
    for i in range(num_tests):
        frame = cv2.imread(f'{image_folder_path}/{name}-{i+1}{"_sunglasses" if sunglasses else ""}.jpg')
        embedding, face_image, box = get_embedding(frame)
        result, similarity = recognize_face(embedding)
        print(f"Test {i+1}  |  Result: {similarity}")
    
        line = str(similarity).replace(".",',') + "\n"
        file.write(line)
    
    file.close()