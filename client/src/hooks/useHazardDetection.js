import { useState, useEffect } from 'react';

const useHazardDetection = (hazardModel) => {
    const [hazardDetected, setHazardDetected] = useState(false);

    const detectHazard = async (image) => {
        try {
            const detectionResult = await hazardModel.predict(image);
            setHazardDetected(detectionResult);
        } catch (error) {
            console.error("Error during hazard detection:", error);
        }
    };

    return { hazardDetected, detectHazard };
};

export default useHazardDetection;
