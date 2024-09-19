import { useState } from 'react';

const useRecognition = (model) => {
    const [recognitionResults, setRecognitionResults] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const recognize = async (image) => {
        setIsLoading(true);
        try {
            const results = await model.predict(image);
            setRecognitionResults(results);
        } catch (error) {
            console.error("Error during recognition:", error);
        } finally {
            setIsLoading(false);
        }
    };

    return { recognitionResults, isLoading, recognize };
};

export default useRecognition;
