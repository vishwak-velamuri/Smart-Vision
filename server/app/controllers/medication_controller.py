from flask import Blueprint, request, jsonify
from services.medication_service import MedicationService

medication_controller = Blueprint('medication', __name__)
medication_service = MedicationService()

@medication_controller.route('/medications', methods=['POST'])
def add_medication():
    data = request.json
    medication = medication_service.add_medication(data)
    return jsonify(medication), 201

@medication_controller.route('/medications/<int:medication_id>', methods=['GET'])
def get_medication(medication_id):
    medication = medication_service.get_medication(medication_id)
    if medication:
        return jsonify(medication), 200
    return jsonify({'error': 'Medication not found'}), 404

@medication_controller.route('/medications', methods=['GET'])
def list_medications():
    medications = medication_service.list_medications()
    return jsonify(medications), 200
