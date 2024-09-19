from flask import Blueprint, request, jsonify
from services.hazard_detection_service import HazardDetectionService

hazard_detection_controller = Blueprint('hazard_detection', __name__)
hazard_detection_service = HazardDetectionService()

@hazard_detection_controller.route('/hazards', methods=['POST'])
def detect_hazard():
    data = request.json
    hazards = hazard_detection_service.detect_hazard(data)
    return jsonify(hazards), 200