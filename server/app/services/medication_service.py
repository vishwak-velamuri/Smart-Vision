class MedicationService:
    def __init__(self):
        self.medications = []  # In-memory storage for demonstration

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