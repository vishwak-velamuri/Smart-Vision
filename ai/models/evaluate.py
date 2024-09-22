import tensorflow as tf
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import numpy as np

def evaluate_model(model_path, test_dir, input_shape=(224, 224, 3), batch_size=32):
    # Load the model
    model = load_model(model_path)

    # Data generator for test dataset
    test_datagen = ImageDataGenerator(rescale=1.0/255.0)

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False  # Important for evaluation
    )

    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(test_generator, steps=test_generator.samples // batch_size)

    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")

    return test_loss, test_accuracy

if __name__ == "__main__":
    # Set the path to your trained model and test directory
    model_path = 'smart_vision_model.h5'
    test_directory = 'ai/data/dataset/test'
    
    evaluate_model(model_path, test_directory)