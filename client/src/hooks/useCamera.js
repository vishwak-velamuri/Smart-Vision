import { useState, useEffect } from 'react';

const useCamera = (videoRef) => {
    const [isCameraActive, setIsCameraActive] = useState(false);

    useEffect(() => {
        const startCamera = async () => {
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                videoRef.current.srcObject = stream;
                setIsCameraActive(true);
            }
        };

        startCamera();

        return () => {
            if (videoRef.current && videoRef.current.srcObject) {
                const tracks = videoRef.current.srcObject.getTracks();
                tracks.forEach((track) => track.stop());
            }
        };
    }, [videoRef]);

    return { isCameraActive };
};

export default useCamera;
