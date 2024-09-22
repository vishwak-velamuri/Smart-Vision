import React from 'react';

const MedicationRecognition = ({ detectedMedications, detectedColor, detectedShape, detectedImprint }) => {
    return (
        <div className="medication-recognition">
            <h2>Recognized Medications</h2>
            <ul>
                {detectedMedications.map((med, index) => (
                    <li key={index}>
                        {med} - Color: {detectedColor} - Shape: {detectedShape} - Imprint: {detectedImprint}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MedicationRecognition;