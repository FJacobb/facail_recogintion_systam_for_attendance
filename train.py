from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.optimizers import RMSprop
import tensorflow as tf
from test import Test

class Train():
    def __init__(self):
        student_id =[]
        listd = []

        gpus = tf.config.experimental.list_physical_devices("GPU")
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        model = tf.keras.models.Sequential([ tf.keras.layers.Conv2D(128,(3,3), 1, activation = "relu", input_shape=(256, 256, 3)),
                                            tf.keras.layers.MaxPool2D(),

                                            tf.keras.layers.Conv2D(64,(3,3), 1, activation = "relu"),
                                            tf.keras.layers.MaxPool2D(),

                                            tf.keras.layers.Conv2D(32, (3, 3), 1, activation="relu"),
                                            tf.keras.layers.MaxPool2D(),

                                             tf.keras.layers.Conv2D(16, (3, 3), 1, activation="relu"),
                                             tf.keras.layers.MaxPool2D(),

                                             tf.keras.layers.Flatten(),
                                            tf.keras.layers.Dense(256, activation="relu"),
                                            tf.keras.layers.Dense(1, activation="sigmoid")

        ])

        train = ImageDataGenerator(rescale=1/255)
        validation = ImageDataGenerator(rescale=1/255)
        print(train)
        path = "images/AFIT/CYBER SECURITY/"
        train_dataset = train.flow_from_directory(path, batch_size=3, class_mode="binary", target_size=(256, 256))
        print(train_dataset.class_indices.keys())
        validation_dataset = validation.flow_from_directory(path, batch_size=3, class_mode="binary", target_size=(256, 256))
        print(train_dataset)
        print(train_dataset.class_indices)


        model.compile(loss="binary_crossentropy", optimizer= "adam", metrics=["accuracy"])


        model.fit(train_dataset, epochs=1, validation_data=validation_dataset)
        model.save("trained_data.h5")
        #
        print(validation_dataset.class_indices)

        Test()