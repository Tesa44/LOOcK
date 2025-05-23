from add_test_img import add_test_img
from add_pattern_img import add_pattern_img
from compare import compare
from db import remove_person_from_database, display_database_contents
from face_processing import get_embedding
import cv2
import db

name = input("Enter name: ")
name = name.lower()
choice = -1
NUM_PATTERN_IMG = [1, 3, 5, 10]
NUM_TESTS = 100

while choice != 0:
    # Menu
    print("1. Add test photos")
    print("2. Add pattern photos")
    print("3. Import pattern image from file")
    print("4. Delete all pattern photos")
    print("5. Single test")
    print("6. Full test")
    print("0. Exit")
    choice = int(input())
    if choice == 1:
        add_test_img(name, False)
        input("Now put on your glasses and hit enter when you are ready")
        add_test_img(name, True)

    elif choice == 2:
        add_pattern_img(name, int(input("How much images do you want to add?: ")))

    elif choice == 3:
            file_path = input("File path: ")
            pattern_img = cv2.imread(file_path)
            embedding, face_image, box = get_embedding(pattern_img)
            db.add_face_to_database(name, embedding, face_image)

    elif choice == 4:
        remove_person_from_database(name)
        display_database_contents()

    elif choice == 5:
        num_pattern_img = int(input("How much pattern images do you have: "))
        compare(name, False, NUM_TESTS,num_pattern_img,test=True)
        compare(name, True, NUM_TESTS,num_pattern_img ,test=True)

    elif choice == 6:
        # Add test images
        add_test_img(name, False)
        input("Now put on your glasses and hit enter when you are ready")
        add_test_img(name, True)
        for i in range(len(NUM_PATTERN_IMG)):
            cur_num_pattern_img = NUM_PATTERN_IMG[i]
            num_images = cur_num_pattern_img - NUM_PATTERN_IMG[i-1] if i > 0 else cur_num_pattern_img
            print(f"Test with {cur_num_pattern_img} pattern images \n Add {num_images} pattern imagaes")
            add_pattern_img(name,num_images)
            for sunglasses in [False, True]:
                compare(name,sunglasses, NUM_TESTS, cur_num_pattern_img, test=True)
