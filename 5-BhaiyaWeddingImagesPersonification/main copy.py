import os
import shutil
import face_recognition
import cv2
import threading


target_folder = "C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/Target/"
target_name = "VandanaPundir"
parent_folder = "C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/"


def train():
    global target_name
    training_data = "C:/Users/adity/Documents/Code-Playground/PythonLab/5-BhaiyaWeddingImagesPersonification/Trainer/"
    training_items = os.listdir(training_data)
    images = []
    for item in training_items:
        images.append(training_data+item)

    encodes = []
    for img in images:
        target = face_recognition.load_image_file(img)
        target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)
        target_encode = face_recognition.face_encodings(target)[0]
        encodes.append(target_encode)
    return encodes


def compare(img_path):
    # New Test Image:
    encodes = train()
    imgTest = face_recognition.load_image_file(img_path)
    imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
    encodeTest = face_recognition.face_encodings(imgTest)
    results = []

    for enc in encodeTest:
        result = face_recognition.compare_faces(encodes, enc, tolerance=0.35)
        results.append(result[0])
    if True in results:
        print(f"{img_path} : {True}")
        return img_path
    else:
        return False


targets = os.listdir(target_folder)

for target in targets:
    print(target)
    t1 = threading.Thread(target=compare, args=(f"{target_folder}{target}",))
    t1.start()
    result = t1.join()
    if result != False:
        if target_name not in os.listdir(parent_folder):
            os.mkdir(parent_folder+target_name)
        shutil.copy(f"{target_folder}{target}", parent_folder+target_name)
