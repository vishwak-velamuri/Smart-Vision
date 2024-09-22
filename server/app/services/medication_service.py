import json
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher

class MedicationService:
    def __init__(self):
        self.medications = []  # In-memory storage for demonstration

    def load_annotations(self, json_file):
        with open(json_file, 'r') as f:
            return json.load(f)

    def calculate_similarity(self, detected_pill, annotations):
        # First check for perfect matches
        perfect_matches = []
        closest_matches = []
        
        for pill in annotations:
            try:
                imprint = pill['imprint']
                shape_code = pill['shape_text']
                color_codes_list = pill['color_text'].split(';')  # Split if multiple colors

                # Check for perfect imprint match
                if detected_pill['imprint'] == imprint:
                    perfect_matches.append((pill['medicine_name'], 1.0))  # Perfect match has a similarity of 1.0
                
                # Create feature vectors for similarity calculation
                shape_vector = 1 if detected_pill['shape'] == shape_code else 0
                color_vector = 1 if detected_pill['color'] in color_codes_list else 0

                # Combine weighted features for closest match
                feature_vector = (0.5 * shape_vector + 0.2 * color_vector)

                # Store in closest matches
                closest_matches.append((pill['medicine_name'], feature_vector))
            
            except KeyError as e:
                print(f"Missing key: {e} in pill entry: {pill}")
                continue  # Skip this entry if there's a missing key

        # Return perfect matches if any
        if perfect_matches:
            return perfect_matches

        # Otherwise, return the best closest match
        if closest_matches:
            # Find the best match based on the highest feature vector value
            best_closest_match = max(closest_matches, key=lambda x: x[1])
            return [best_closest_match]

        return []  # Return an empty list if no matches found

    def find_best_match(self, similarities):
        best_match = max(similarities, key=lambda x: x[1])
        return best_match

    def add_medication(self, data):
        medication_id = len(self.medications) + 1
        medication = {**data, 'id': medication_id}
        self.medications.append(medication)
        return medication

    def get_medication(self, medication_id):
        for medication in self.medications:
            if medication['id'] == medication_id:
                return medication
        return None

    def list_medications(self):
        return self.medications