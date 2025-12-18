import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing import image

def train_model():
    ruta_train = r".\dataset\train"
    ruta_test = r".\dataset\test"

    if not os.path.exists(ruta_train):
        print(f"Dataset path not found: {ruta_train}")
        return

    datagen = ImageDataGenerator(rescale=1/255)

    train = datagen.flow_from_directory(
        ruta_train,
        target_size=(150,150),
        batch_size=32,
        class_mode='categorical'
    )

    test = datagen.flow_from_directory(
        ruta_test,
        target_size=(150,150),
        batch_size=32,
        class_mode='categorical'
    )

    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
        layers.MaxPooling2D(2,2),

        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),

        layers.Conv2D(128, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),

        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(9, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    hist = model.fit(
        train,
        validation_data=test,
        epochs=10
    )

    model.save("clasificador_frutas.h5")
    print("Modelo guardado como clasificador_frutas.h5")
    
    # Save class indices for reference if needed
    print("Clases detectadas:", train.class_indices)

if __name__ == "__main__":
    train_model()