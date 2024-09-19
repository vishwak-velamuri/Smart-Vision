import React from 'react';
import Header from '../components/Header';
import Camera from '../components/Camera';
import ObjectRecognition from '../components/ObjectRecognition';
import MedicationRecognition from '../components/MedicationRecognition';
import HazardDetection from '../components/HazardDetection';

const Home = () => {
    const recognizedObjects = []; // Placeholder for recognized objects
    const recognizedMedications = []; // Placeholder for recognized medications
    const hazards = []; // Placeholder for detected hazards

    const handleCapture = () => {
        // Logic to capture image and process it
    };

    return (
        <div className="home">
            <Header />
            <Camera onCapture={handleCapture} />
            <ObjectRecognition recognizedObjects={recognizedObjects} />
            <MedicationRecognition recognizedMedications={recognizedMedications} />
            <HazardDetection hazards={hazards} />
        </div>
    );
};

export default Home;