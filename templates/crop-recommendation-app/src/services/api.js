import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Adjust the URL based on your backend configuration

export const predictCrop = async (data) => {
    try {
        const response = await axios.post(`${API_URL}/predict`, data);
        return response.data;
    } catch (error) {
        console.error('Error predicting crop:', error);
        throw error;
    }
};