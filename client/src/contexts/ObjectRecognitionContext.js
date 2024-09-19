import React, { createContext, useContext, useState } from 'react';

const ObjectRecognitionContext = createContext();

export const ObjectRecognitionProvider = ({ children }) => {
    const [recognizedObjects, setRecognizedObjects] = useState([]);

    const addObject = (object) => {
        setRecognizedObjects((prev) => [...prev, object]);
    };

    const clearObjects = () => {
        setRecognizedObjects([]);
    };

    return (
        <ObjectRecognitionContext.Provider value={{ recognizedObjects, addObject, clearObjects }}>
            {children}
        </ObjectRecognitionContext.Provider>
    );
};

export const useObjectRecognition = () => {
    return useContext(ObjectRecognitionContext);
};
