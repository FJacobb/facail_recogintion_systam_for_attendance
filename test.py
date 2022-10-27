# from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing import image
# from keras.optimizers import RMSprop
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
student_id =[]
with open("id of student.txt", mode='r') as file:
    data = file.read()
    for i in data.splitlines():
        student_id.append(i)

model = tf.keras.models.load_model('trained_data')
ims = "images/AFIT/CYBER SECURITY/AFIT-CYS-18-0027/"
for i in os.listdir(ims):
    imh = tf.keras.preprocessing.image.load_img(ims + i, target_size=(148,148, 3))
    x = tf.keras.preprocessing.image.img_to_array(imh)
    x = np.expand_dims(x, axis =0)
    imf = np.vstack([x])
    val = model.predict(imf)
    print("_______________________")
    if val == 1:
        print("festus")
    elif val == 0:
        print("great")
    else:
        print("jjjjjjjjjjjj")
    print("_________________________")
