import tensorflow as tf
from tensorflow import keras
from  tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from model import create_model

def train_model(train_dir, val_dir, input_shape=(224, 224, 3), num_classes=1000, batch_size=32, epochs=10):
    # Data augmentation
    datagen = ImageDataGenerator(
        rescale=1.0/255.0,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    train_generator = datagen.flow_from_directory(
        train_dir,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='categorical'
    )

    val_generator = datagen.flow_from_directory(
        val_dir,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='categorical'
    )

    # Create and compile the model
    model = create_model(input_shape=input_shape, num_classes=num_classes)

    # Train the model
    model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // batch_size,
        validation_data=val_generator,
        validation_steps=val_generator.samples // batch_size,
        epochs=epochs
    )

    # Save the model
    model.save('smart_vision_model.h5')

    return model

if __name__ == "__main__":
    # Set paths to your training and validation directories
    train_directory = 'path/to/train_data'
    validation_directory = 'path/to/val_data'
    
    model = train_model(train_directory, validation_directory)