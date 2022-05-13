import os
import shutil
import face_recognition
import cv2


target_folder = "C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/Target/"
trainer_folder = "C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/Trainer/"


def encode_faces(folder):
    known_encodings = []
    for filename in os.listdir(folder):
        known_image = face_recognition.load_image_file(folder+filename)
        known_encoding = face_recognition.face_encodings(known_image)[0]

        known_encodings.append((known_encoding, filename))
    return known_encodings


def find_target_face(target_image, target_encoding):
    global trainer_folder, target_folder
    face_location = face_recognition.face_locations(target_image)

    for person in encode_faces(trainer_folder):
        encoded_face = person[0]
        filename = person[1]
        is_target_face = face_recognition.compare_faces(
            encoded_face, target_encoding, tolerance=0.3)
        if filename.split(".")[0] not in os.listdir("C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/"):
            os.mkdir(
                f"""C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/{filename.split(".")[0]}""")
        if True in is_target_face:
            shutil.copy("C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/Target/bill-gates.jpg",
                        f"C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/{filename.split('.')[0]}/")
        print(f"{is_target_face}{filename}")

        # if face_location:
        #     face_number = 0
        #     for location in face_location:
        #         if is_target_face[face_number]:
        #             label = filename
        #             print(label)
        #         face_number += 1


targets = os.listdir(target_folder)

for target in targets:
    target_image = face_recognition.load_image_file(
        target_folder+target)
    target_encoding = face_recognition.face_encodings(target_image)
    find_target_face(target_image, target_encoding)
