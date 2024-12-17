import cv2
import numpy as np
import math

def classify_pill_shape(input_image):
    # Step 1: Image Preprocessing
    # Convert to grayscale
    grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
    # Thresholding to create a binary image
    _, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY_INV)

    # Step 2: Contour Detection
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Select the largest contour
    pill_contour = max(contours, key=cv2.contourArea)
    
    # Step 3: Shape Approximation
    # Approximate the contour
    epsilon = 0.02 * cv2.arcLength(pill_contour, True)
    approx = cv2.approxPolyDP(pill_contour, epsilon, True)
    
    # Calculate contour properties
    area = cv2.contourArea(pill_contour)
    perimeter = cv2.arcLength(pill_contour, True)
    x, y, w, h = cv2.boundingRect(approx)
    aspect_ratio = float(w) / h if h != 0 else 0
    circularity = (4 * np.pi * area) / (perimeter ** 2) if perimeter > 0 else 0

    # Step 4: Classification Logic
    def is_semi_circle(approx):
        # Logic for semi-circle detection
        # A semi-circle has a circularity close to 1 and an aspect ratio close to 1
        circularity_threshold = 0.7
        aspect_ratio_threshold = 0.8
        return circularity > circularity_threshold and aspect_ratio > aspect_ratio_threshold

    def is_trapezoid(approx):
        # Logic for trapezoid detection
        # A trapezoid has a number of sides close to 4 and an aspect ratio close to 1
        num_sides_threshold = 3.5
        aspect_ratio_threshold = 0.8
        return len(approx) > num_sides_threshold and aspect_ratio > aspect_ratio_threshold

    def is_bullet(approx):
        # Logic for bullet shape detection
        # A bullet shape has a circularity close to 1 and an aspect ratio close to 2
        circularity_threshold = 0.7
        aspect_ratio_threshold = 1.5
        return circularity > circularity_threshold and aspect_ratio > aspect_ratio_threshold

    def is_clover(approx):
        # Logic for clover shape detection
        # A clover shape has a number of sides close to 4 and an aspect ratio close to 1
        num_sides_threshold = 3.5
        aspect_ratio_threshold = 0.8
        return len(approx) > num_sides_threshold and aspect_ratio > aspect_ratio_threshold

    def is_diamond(approx):
        # Logic for diamond shape detection
        # A diamond shape has a number of sides close to 4 and an aspect ratio close to 1
        num_sides_threshold = 3.5
        aspect_ratio_threshold = 0.8
        return len(approx) > num_sides_threshold and aspect_ratio > aspect_ratio_threshold

    def is_double_circle(approx):
        # Logic for double circle detection
        # A double circle has a circularity close to 1 and an aspect ratio close to 1
        circularity_threshold = 0.7
        aspect_ratio_threshold = 0.8
        return circularity > circularity_threshold and aspect_ratio > aspect_ratio_threshold

    def is_tear(approx):
        # Logic for tear shape detection
        # A tear shape has a circularity close to 1 and an aspect ratio close to 2
        circularity_threshold = 0.7
        aspect_ratio_threshold = 1.5
        return circularity > circularity_threshold and aspect_ratio > aspect_ratio_threshold

    # Shape classifications
    for contour in contours:
        approx = cv2.approxPolyDP(contour, epsilon, True)
        circularity = 4 * math.pi * cv2.contourArea(contour) / (cv2.arcLength(contour, True) ** 2)
        aspect_ratio = cv2.contourArea(contour) / (cv2.boundingRect(contour).width * cv2.boundingRect(contour).height)

        if is_semi_circle(approx):
            shape = "Semi-circle"
        elif is_trapezoid(approx):
            shape = "Trapezoid"
        elif is_bullet(approx):
            shape = "Bullet"
        elif is_clover(approx):
            shape = "Clover"
        elif is_diamond(approx):
            shape = "Diamond"
        elif is_double_circle(approx):
            shape = "Double circle"
        elif is_tear(approx):
            shape = "Tear"
        elif len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            if aspect_ratio > 0.9:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif len(approx) == 5:
            shape = "Pentagon"
        elif len(approx) == 6:
            shape = "Hexagon"
        elif circularity > 0.7:
            shape = "Circle"
        else:
            shape = "Unknown"

        print(f"Detected shape: {shape}")