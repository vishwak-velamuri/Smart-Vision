export const formatPillData = (pill) => {
    return {
        name: pill.name,
        type: pill.type,
        imageUrl: pill.imageUrl,
    };
};

export const calculateResponseTime = (startTime, endTime) => {
    return (endTime - startTime) / 1000; // Convert to seconds
};
