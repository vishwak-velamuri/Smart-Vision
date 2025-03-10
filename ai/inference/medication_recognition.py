import json
import numpy as np
from difflib import SequenceMatcher
from math import sqrt

# Load annotations from JSON file
def load_annotations(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

# Create mappings for shapes and colors
shape_codes = {
    "C48336": "CAPSULE",
    "C48345": "OVAL",
    "C48348": "ROUND",
}

color_codes = {
    "C48323": "BLACK",
    "C48324": "GRAY",
    "C48325": "WHITE",
    "C48326": "RED",
    "C48327": "PURPLE",
    "C48328": "PINK",
    "C48329": "GREEN",
    "C48330": "YELLOW",
    "C48331": "ORANGE",
    "C48332": "BROWN",
    "C48333": "BLUE",
    "C48334": "TURQUOISE",
    "C483352": "PALE"
}

color_hexes = {
    "BLACK": (0, 0, 0),
    "GRAY": (128, 128, 128),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "PURPLE": (128, 0, 128),
    "PINK": (255, 192, 203),
    "GREEN": (0, 255, 0),
    "YELLOW": (255, 255, 0),
    "ORANGE": (255, 165, 0),
    "BROWN": (165, 42, 42),
    "BLUE": (0, 0, 255),
    "TURQUOISE": (64, 224, 208),
    "PALE": (250, 250, 210)
}

# Find detected color based on hex code from camera
def extract_color(detected_color):
    def euclidean_distance(color1, color2):
        return sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))
    
    color_tuple = min(color_hexes.items(), key=lambda item: euclidean_distance(detected_color, item[1]))
    return color_tuple[0]

# Convert detected color to color code
def convert_color_to_code(detected_color_name):
    for code, name in color_codes.items():
        if name.lower() == detected_color_name.lower():
            return code
    return None

# Convert detected shape to shape code
def convert_shape_to_code(detected_shape_name):
    for code, name in shape_codes.items():
        if name.lower() == detected_shape_name.lower():
            return code
    return None

# Calculate similarity score for imprint using SequenceMatcher
def similarity_ratio(a, b):
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio()

# Calculate weighted similarity
def calculate_similarity(detected_pill, annotations):
    matches = []
    
    for pill in annotations:
        try:
            imprint = pill.get('imprint', '')
            shape_code = pill.get('shape_text', '')
            color_codes_str = pill.get('color_text', '')
            color_codes_list = color_codes_str.split(';') if color_codes_str else []
            
            # Calculate individual feature scores
            imprint_score = similarity_ratio(detected_pill['imprint'], imprint)
            shape_score = 1.0 if detected_pill['shape'] == shape_code else 0.0
            color_score = 1.0 if detected_pill['color'] in color_codes_list else 0.0
            
            # Calculate weighted total score
            total_score = (0.5 * imprint_score + 0.3 * shape_score + 0.2 * color_score)
            
            # Add to matches - just include name and score (removing the details dictionary)
            matches.append((pill.get('medicine_name', 'Unknown'), total_score))
        
        except Exception as e:
            print(f"Error processing pill entry: {e}")
            continue

    # Sort by score
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:5]  # Return top 5 matches

# Find the best match
def find_best_match(similarities):
    if not similarities:
        return None
    return similarities[0]

# Main function for recognizing pills
def recognize_medication(detected_shape, detected_color, detected_imprint, json_file):
    try:
        annotations = load_annotations(json_file)
        
        # If color is a RGB tuple, extract the closest color name
        if isinstance(detected_color, tuple) and len(detected_color) == 3:
            detected_color = extract_color(detected_color)
        
        detected_pill = {
            'shape': convert_shape_to_code(detected_shape),
            'imprint': detected_imprint,
            'color': convert_color_to_code(detected_color)
        }
        
        print(f"Looking for pill with shape: {detected_shape} ({detected_pill['shape']}), "
              f"color: {detected_color} ({detected_pill['color']}), "
              f"imprint: {detected_imprint}")
        
        similarities = calculate_similarity(detected_pill, annotations)
        return similarities
    
    except Exception as e:
        print(f"Error in medication recognition: {e}")
        return []