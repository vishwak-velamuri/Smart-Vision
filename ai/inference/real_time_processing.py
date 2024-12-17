import cv2
import numpy as np
from low_light_detection import detect_low_light
from medication_recognition import recognize_medication

# Path to the annotations JSON file
ANNOTATIONS_FILE = '/ai/data/annotations.json'

def process_frame(frame, detected_shape, detected_color, detected_imprint):
    """
    This function processes each frame captured from the camera.
    It can be modified to include different image processing tasks.
    
    Args:
    - frame: The current frame from the video feed.
    - detected_shape: The detected shape of the pill from the frame.
    - detected_color: The detected color of the pill from the frame.
    - detected_imprint: The detected imprint on the pill from the frame.
    
    Returns:
    - processed_frame: The processed frame with any results drawn on it.
    """
    # Detect low light in the frame
    if detect_low_light(frame):
        cv2.putText(frame, "Low Light Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Sufficient Light", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Recognize the pill using detected attributes (shape, color, imprint)
    best_match = recognize_medication(detected_shape, detected_color, detected_imprint, ANNOTATIONS_FILE)

    if best_match:
        cv2.putText(frame, f"Match: {best_match[0]}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.putText(frame, f"Score: {best_match[1]:.2f}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    else:
        cv2.putText(frame, "No Match Found", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return frame

def run_real_time_processing():
    """
    This function continuously captures frames from the camera,
    processes them in real time, and displays the results.
    """
    # Initialize the camera (using OpenCV's VideoCapture for webcam)
    camera = cv2.VideoCapture(0)  # 0 for default camera

    if not camera.isOpened():
        print("Error: Unable to access the camera.")
        return

    # Placeholder for actual detection from object recognition model
    detected_shape = "round"  # Placeholder: Replace with real detected shape
    detected_color = "white"  # Placeholder: Replace with real detected color
    detected_imprint = "ACC123"  # Placeholder: Replace with real detected imprint

    # Continuously process frames from the camera
    while True:
        # Capture a frame from the camera
        ret, frame = camera.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Process the frame (e.g., detect low light, recognize medication)
        processed_frame = process_frame(frame, detected_shape, detected_color, detected_imprint)

        # Display the processed frame
        cv2.imshow('Real-Time Processing', processed_frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_real_time_processing()