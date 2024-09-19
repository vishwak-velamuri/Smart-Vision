import React from 'react';

const ObjectRecognition = ({ recognizedObjects }) => {
    return (
        <div className="object-recognition">
            <h2>Recognized Objects</h2>
            <ul>
                {recognizedObjects.map((obj, index) => (
                    <li key={index}>{obj}</li>
                ))}
            </ul>
        </div>
    );
};

export default ObjectRecognition;
