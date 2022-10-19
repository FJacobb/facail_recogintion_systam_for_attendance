from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.optimizers import RMSprop
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
os.system("pip install --force-reinstall tensorflow-2.9.1-cp310-cp310-win_amd64.whl")
ims = tf.keras.preprocessing.image.load_img("20220412_122045.jpg", target_size=(157,157,3))
video = cv2.VideoCapture(0)

student_id = []

with open("id of student.txt", mode='r') as file:
    data = file.read()
    for i in data.splitlines():
        student_id.append(i)

# cv2.imread(f"images/{student_id[0]}/1.jpg").shape

train = ImageDataGenerator(rescale=1/255)
validation = ImageDataGenerator(rescale=1/255)
img = student_id[0]
train_dataset = train.flow_from_directory(f"images/AFIT/CYBER SECURITY/", batch_size=3, class_mode="binary")
validation_dataset = validation.flow_from_directory(f"images/AFIT/CYBER SECURITY/", batch_size=3, class_mode="binary")
print(train_dataset.class_indices)
model = tf.keras.models.Sequential([ tf.keras.layers.Conv2D(16,(3,3), activation = "relu"),
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
model_fit = model.fit(train_dataset, epochs=1, validation_data=validation_dataset)
x = tf.keras.preprocessing.image.img_to_array(ims)
x = np.expand_dims(x, axis=0)
imf = np.vstack([x])
print(imf)
val = model.predict(imf)
print(val)
if val == 0:
    print("festus")
else:
    print("jjjjjjjjjjjj")
# # if val == 0:
# #     print("festus")
# # else:
# #     print("gggggggggggggggg")