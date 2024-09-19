import React from 'react';

const MedicationRecognition = ({ recognizedMedications }) => {
    return (
        <div className="medication-recognition">
            <h2>Recognized Medications</h2>
            <ul>
                {recognizedMedications.map((med, index) => (
                    <li key={index}>{med}</li>
                ))}
            </ul>
        </div>
    );
};

export default MedicationRecognition;
