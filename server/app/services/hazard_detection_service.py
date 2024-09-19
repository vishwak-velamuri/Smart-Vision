class HazardDetectionService:
    def detect_hazard(self, data):
        # Placeholder logic for detecting hazards
        hazards = []
        if 'obstacle' in data:
            hazards.append({'type': 'obstacle', 'location': data['obstacle']})
        return hazards