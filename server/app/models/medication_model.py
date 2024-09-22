from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import json

class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="medications")

    def __init__(self, name, dosage, frequency, user_id):
        self.name = name
        self.dosage = dosage
        self.frequency = frequency
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dosage': self.dosage,
            'frequency': self.frequency,
            'user_id': self.user_id
        }

def load_annotations(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def calculate_similarity(detected_pill, annotations):
    similarities = {}
    for annotation in annotations:
        # Initialize similarity score
        similarity_score = 0
        
        # Compare color (weight: 0.2)
        if detected_pill['color'] == annotation['color']:
            similarity_score += 0.2
            
        # Compare shape (weight: 0.3)
        if detected_pill['shape'] == annotation['shape']:
            similarity_score += 0.3
            
        # Compare imprint (weight: 0.5)
        if detected_pill['imprint'] == annotation['imprint']:
            similarity_score += 0.5

        similarities[annotation['name']] = similarity_score

    return similarities

def find_best_match(similarities):
    # Find the medication with the highest similarity score
    best_match = max(similarities.items(), key=lambda x: x[1], default=(None, 0))
    if best_match[1] > 0:
        return best_match[0]  # Return the name of the best match
    return None  # No match found