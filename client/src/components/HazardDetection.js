import React from 'react';

const HazardDetection = ({ hazards }) => {
    return (
        <div className="hazard-detection">
            <h2>Detected Hazards</h2>
            <ul>
                {hazards.map((hazard, index) => (
                    <li key={index}>{hazard}</li>
                ))}
            </ul>
        </div>
    );
};

export default HazardDetection;
