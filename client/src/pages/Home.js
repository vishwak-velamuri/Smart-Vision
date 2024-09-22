import React from 'react';
import Header from 'client/components/Header';
import Camera from 'client/components/Camera';
import MedicationRecognition from 'client/components/MedicationRecognition';

const Home = () => {
    const recognizedMedications = []; // Placeholder for recognized medications

    const handleCapture = () => {
        // Logic to capture image and process it
    };

    return (
        <div className="home">
            <Header />
            <Camera onCapture={handleCapture} />
            <MedicationRecognition recognizedMedications={recognizedMedications} />
        </div>
    );
};

export default Home;