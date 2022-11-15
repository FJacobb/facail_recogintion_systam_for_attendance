from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from keras.models import load_model
import numpy as np
from convart_to_csv import Csv


# from alexa import alexa
train = ImageDataGenerator(rescale=1/255)
train_dataset = train.flow_from_directory(f"C:/Users/festu/OneDrive/Documents/100days of code/festus_project/images/AFIT/CYBER SECURITY/", batch_size=3, class_mode="binary",
    target_size=(256, 256))
mark = {}
for name, value in train_dataset.class_indices.items():
	mark[name] = 0

class_of_id = train_dataset.class_indices
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(2)
font=cv2.FONT_HERSHEY_COMPLEX


model = load_model('C:/Users/festu/OneDrive/Documents/100days of code/festus_project/trained_data.h5')


def get_className(classNo):
	for name, value in class_of_id.items():
		if classNo == value:
			if mark[name] == 0:
				mark[name] = 1
				return name
			else:
				return name
		else:
			return "unknown"

while True:
	sucess, imgOrignal=cap.read()
	faces = facedetect.detectMultiScale(imgOrignal,1.3,5)
	for x,y,w,h in faces:
		crop_img=imgOrignal[y:y+h,x:x+h]
		img=cv2.resize(crop_img, (256,256))
		img=img.reshape(1, 256, 256, 3)
		prediction=model.predict(img)
		classIndex = np.expand_dims(prediction,axis=0)
		probabilityValue=np.amax(prediction)

		cv2.rectangle(imgOrignal,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.rectangle(imgOrignal, (x,y-40),(x+w, y), (0,255,0),-2)
		cv2.putText(imgOrignal, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)

		cv2.imshow("Pranav's Facial Recognition Model",imgOrignal)


		if cv2.waitKey(1)==ord('q'):
			Csv(mark)
			cap.release()
			cv2.destroyAllWindows()































































# # from keras.preprocessing.image import ImageDataGenerator
# # from keras.preprocessing import image
# # from keras.optimizers import RMSprop
# from keras.preprocessing.image import ImageDataGenerator
# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# import os
# student_id =[]
# with open("id of student.txt", mode='r') as file:
#     data = file.read()
#     for i in data.splitlines():
#         student_id.append(i)
#
# # model = tf.keras.models.load_model('trained_data')
# ims = "testing/"
# train = ImageDataGenerator(rescale=1/255)
# train_dataset = train.flow_from_directory(f"C:/Users/festu/OneDrive/Documents/100days of code/festus_project/images/AFIT/CYBER SECURITY/", batch_size=3, class_mode="binary",
#     target_size=(148, 148))
# class_of_id = train_dataset.class_indices
# ########################################################################
# #Pranav Sai
#
# import cv2
# from keras.models import load_model
# import numpy as np
# # from alexa import alexa
#
# facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# cap=cv2.VideoCapture(2)
# font=cv2.FONT_HERSHEY_COMPLEX
#
#
# model = load_model('trained_data.h5')
#
#
# def get_className(classNo):
# #     for name, value in class_of_id.items():
# #         if classNo == value:
# #
# #             return name
# #         else:
# #             return "unknown"
# 	if classNo==0:
# 		return "Pranav Sai"
# 	elif classNo==1:
# 			return "The Best Dad Ever!"
#
#
# # while True:
# # 	sucess, imgOrignal=cap.read()
# # 	faces = facedetect.detectMultiScale(imgOrignal,2.0,5)
# # 	for x,y,w,h in faces:
# # 		crop_img=imgOrignal[y:y:(y - 32) + (h + 20), x:(x - 32) + (w + 20)]
# # 		img = cv2.resize(crop_img, (148, 148))
# # 		img = img.reshape(1, 148, 148, 3)
# # 		prediction=model.predict(img)
# # 		classIndex = np.argmax(prediction,axis=-1)
# # 		probabilityValue=np.amax(prediction)
# #
# # 		cv2.rectangle(imgOrignal,(x,y),(x+w,y+h),(0,255,0),2)
# # 		cv2.rectangle(imgOrignal, (x,y-40),(x+w, y), (0,255,0),-2)
# # 		cv2.putText(imgOrignal, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
# #
# # 		cv2.imshow("Pranav's Facial Recognition Model",imgOrignal)
# # 		k=cv2.waitKey(1)
# # 		if k==ord('q'):
# # 			cap.release()
# # 			cv2.destroyAllWindows()
# ########################################################################
# class_of_id = train_dataset.class_indices
# print(model.summary())
# print("_______________________")
# for i in os.listdir(ims):
#     imh = tf.keras.preprocessing.image.load_img(ims + i, target_size=(256,256, 3))
#     x = tf.keras.preprocessing.image.img_to_array(imh)
#     x = np.expand_dims(x, axis =0)
#     imf = np.vstack([x])
#     val = float(model.predict(imf))
#     print(f"0000000000000000000000000000000000[]000000000000000000000[{float(val)}]")
#     print(f"***************************{val}***********************{i}**********{class_of_id.items()}")
#     for name, value in class_of_id.items():
#         if val == value:
#             print(name)
#
# print("_________________________")
