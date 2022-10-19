# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# import matplotlib.pyplot as plt

student_id = []

with open("id of student.txt", mode='r') as file:
    data = file.read()
    for i in data.splitlines():
        student_id.append(i)

print(student_id)
