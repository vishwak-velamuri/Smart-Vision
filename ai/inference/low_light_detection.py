import cv2
import numpy as np

# Function to calculate the brightness of the image
def calculate_brightness(frame):
    """
    This function calculates the brightness of the frame.
    It averages the pixel intensities across all color channels (for color images).
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the image to HSV color space
    brightness = np.mean(hsv[:, :, 2])  # V channel in HSV represents the brightness
    return brightness

# Function to detect low light conditions
def detect_low_light(frame, threshold=50):
    """
    This function checks if the brightness of the frame is below the given threshold.
    If it's below the threshold, it's considered low light.
    
    Args:
    - frame: The captured image frame (in BGR format).
    - threshold: The brightness threshold (default is 50).
    
    Returns:
    - True if low light is detected, False otherwise.
    """
    brightness = calculate_brightness(frame)
    print(f"Brightness Level: {brightness}")

    if brightness < threshold:
        return True  # Low light detected
    return False  # Sufficient light

# Example function to run low light detection
def run_low_light_detection():
    """
    This function initializes the camera, captures a frame,
    and checks for low light conditions.
    """
    # Initialize the camera (using OpenCV's VideoCapture for webcam)
    camera = cv2.VideoCapture(0)  # 0 for default camera

    if not camera.isOpened():
        print("Error: Unable to access the camera.")
        return

    # Capture a frame from the camera
    ret, frame = camera.read()

    if not ret:
        print("Error: Failed to capture image.")
        return

    # Detect low light conditions
    if detect_low_light(frame):
        print("Low light detected. Consider adjusting lighting or camera settings.")
    else:
        print("Sufficient lighting detected.")

    # Display the captured frame (for debugging purposes)
    cv2.imshow('Captured Frame', frame)

    # Wait for a key press and release the camera
    cv2.waitKey(0)
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_low_light_detection()