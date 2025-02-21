import cv2
import numpy as np

def detect_shape(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    shape = "Unknown"

    for contour in contours:
        # Ignore small noise
        if cv2.contourArea(contour) < 500:
            continue

        # Fit an ellipse
        if len(contour) >= 5:  # fitEllipse requires at least 5 points
            ellipse = cv2.fitEllipse(contour)
            (x, y), (major_axis, minor_axis), angle = ellipse  # Get ellipse parameters

            ratio = major_axis / minor_axis  # Aspect ratio

            if ratio < 1.2:  # If nearly equal axes, it's round
                shape = "Round"
            elif 1.2 <= ratio < 2.5:  # If moderately elongated, it's oval
                shape = "Oval"
            else:
                # For capsule, check if the contour is elongated but has rounded ends
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.intp(box)
                
                width, height = rect[1]
                rect_ratio = max(width, height) / min(width, height)
                
                if rect_ratio > 2.5:  # More elongated than an oval
                    shape = "Capsule"

        # Draw detected shape on image (optional)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    return image, shape

# Example usage
image = cv2.imread("pill_image.jpg")  # Replace with actual image path
processed_image, detected_shape = detect_shape(image)

cv2.imshow("Detected Shape", processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()