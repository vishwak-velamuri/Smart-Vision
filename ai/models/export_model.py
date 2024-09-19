import tensorflow as tf
from tensorflow.python.keras.models import load_model

def export_model(model_path, export_path):
    # Load the trained model
    model = load_model(model_path)

    # Save the model in TensorFlow SavedModel format
    tf.saved_model.save(model, export_path)
    print(f"Model exported to: {export_path}")

if __name__ == "__main__":
    # Set the path to your trained model and export directory
    model_path = 'smart_vision_model.h5'
    export_directory = 'exported_model'  # Specify the export directory here
    
    export_model(model_path, export_directory)
