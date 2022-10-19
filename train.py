# from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing import image
# from keras.optimizers import RMSprop
# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
import os


student_id = []

with open("id of student.txt", mode='r') as file:
    data = file.read()
    for i in data.splitlines():
        student_id.append(i)
os.system("pip install --force-reinstall tensorflow-2.9.1-cp310-cp310-win_amd64.whl")
# cv2.imread(f"images/{student_id[0]}/1.jpg").shape
#
# train = ImageDataGenerator(rescale=1/255)
# validation = ImageDataGenerator(rescale=1/255)
#
# train_dataset = train.flow_from_directory(f"images/{student_id[0]}", batch_size=3, class_mode="binary")
# print(train_dataset)