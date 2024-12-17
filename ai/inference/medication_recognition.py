import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher
from math import sqrt

# Load annotations from JSON file
def load_annotations(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

# Create mappings for shapes and colors
shape_codes = {
    "C48335": "BULLET",
    "C48336": "CAPSULE",
    "C48338": "DIAMOND",
    "C48339": "DOUBLE CIRCLE",
    "C48340": "FREEFORM",
    "C48343": "HEXAGON (6 SIDED)",
    "C48344": "OCTAGON (8 SIDED)",
    "C48345": "OVAL",
    "C48346": "PENTAGON (5 SIDED)",
    "C48347": "RECTANGLE",
    "C48348": "ROUND",
    "C48349": "SEMI-CIRCLE",
    "C48350": "SQUARE",
    "C48351": "TEAR",
    "C48353": "TRIANGLE",
    "C48352": "TRAPEZOID"
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

# Find deteced color based on hex code from camera
def extract_color(color):
    def euclidean_distance(color1, color2):
        return sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))
    color_tuple = min(color_hexes.items(), key=lambda item: euclidean_distance(detected_color, item[1]))
    detected_color = color_tuple[0]
    return detected_color

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
    return SequenceMatcher(None, a, b).ratio()

# Calculate weighted cosine similarity
def calculate_similarity(detected_pill, annotations):
    perfect_matches = []
    closest_matches = []
    
    for pill in annotations:
        try:
            imprint = pill['imprint']
            shape_code = pill['shape_text']
            color_codes_list = pill['color_text'].split(';')
            
            if detected_pill['imprint'] == imprint:
                perfect_matches.append((pill['medicine_name'], 1.0))
            
            shape_vector = 1 if detected_pill['shape'] == shape_code else 0
            color_vector = 1 if detected_pill['color'] in color_codes_list else 0
            
            feature_vector = (0.3 * shape_vector + 0.2 * color_vector)
            closest_matches.append((pill['medicine_name'], feature_vector))
        
        except KeyError as e:
            print(f"Missing key: {e} in pill entry: {pill}")
            continue

    if perfect_matches:
        return perfect_matches

    if closest_matches:
        best_closest_match = max(closest_matches, key=lambda x: x[1])
        return [best_closest_match]

    return []

# Find the best match
def find_best_match(similarities):
    best_match = max(similarities, key=lambda x: x[1])
    return best_match

# Main function for recognizing pills
def recognize_medication(detected_shape, detected_color, detected_imprint, json_file):
    annotations = load_annotations(json_file)
    
    detected_pill = {
        'shape': convert_shape_to_code(detected_shape),
        'imprint': detected_imprint,
        'color': convert_color_to_code(detected_color)
    }
    
    similarities = calculate_similarity(detected_pill, annotations)
    if similarities:
        best_match = find_best_match(similarities)
        return best_match
    return None