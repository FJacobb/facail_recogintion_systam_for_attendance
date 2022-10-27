from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.optimizers import RMSprop
import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# import os
class Train():
    def __init__(self):

        student_id =[]
        with open("id of student.txt", mode='r') as file:
            data = file.read()
            for i in data.splitlines():
                student_id.append(i)

        # cv2.imread(f"images/{student_id[0]}/1.jpg").shape

        train = ImageDataGenerator(rescale=1/255)
        validation = ImageDataGenerator(rescale=1/255)
        img = student_id[0]
        train_dataset = train.flow_from_directory(f"images/AFIT/CYBER SECURITY/", batch_size=3, class_mode="binary", target_size=(148, 148))
        validation_dataset = validation.flow_from_directory(f"images/AFIT/CYBER SECURITY/", batch_size=3, class_mode="binary", target_size=(148, 148))
        print(train_dataset.class_indices)
        model = tf.keras.models.Sequential([ tf.keras.layers.Conv2D(16,(3,3), activation = "relu", input_shape=(148, 148, 3)),
                                            tf.keras.layers.MaxPool2D(2,2),

                                            tf.keras.layers.Conv2D(32,(3,3), activation = "relu"),
                                            tf.keras.layers.MaxPool2D(2,2),

                                            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
                                            tf.keras.layers.MaxPool2D(2, 2),

                                            tf.keras.layers.Flatten(),

                                            tf.keras.layers.Dense(512, activation="relu"),
                                            tf.keras.layers.Dense(1, activation="sigmoid"),

        ])

        model.compile(loss="binary_crossentropy", optimizer= RMSprop(lr=0.001), metrics=["accuracy"])
        model.fit(train_dataset, epochs=10, validation_data=validation_dataset)
        model.save("trained_data")

        print(validation_dataset.class_indices)
