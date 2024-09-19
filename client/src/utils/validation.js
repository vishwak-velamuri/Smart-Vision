export const validateEmail = (email) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
};

export const validateFormFields = (fields) => {
    return Object.values(fields).every(field => field.trim() !== '');
};
