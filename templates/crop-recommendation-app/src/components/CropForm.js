import React, { useState } from 'react';
import axios from 'axios';

const CropForm = ({ onPrediction }) => {
    const [formData, setFormData] = useState({
        N: '',
        P: '',
        K: '',
        temperature: '',
        humidity: '',
        ph: '',
        rainfall: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/predict', formData);
            onPrediction(response.data.prediction);
        } catch (error) {
            console.error('Error fetching prediction:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="N">Nitrogen (N) in soil (kg/ha):</label>
                <input type="number" step="any" id="N" name="N" value={formData.N} onChange={handleChange} required />
            </div>
            <div className="form-group">
                <label htmlFor="P">Phosphorus (P) in soil (kg/ha):</label>
                <input type="number" step="any" id="P" name="P" value={formData.P} onChange={handleChange} required />
            </div>
            <div className="form-group">
                <label htmlFor="K">Potassium (K) in soil (kg/ha):</label>
                <input type="number" step="any" id="K" name="K" value={formData.K} onChange={handleChange} required />
            </div>
            <div className="form-group">
                <label htmlFor="temperature">Temperature (°C):</label>
                <input type="number" step="any" id="temperature" name="temperature" value={formData.temperature} onChange={handleChange} required />
            </div>
            <div className="form-group">
                <label htmlFor="humidity">Humidity (%):</label>
                <input type="number" step="any" id="humidity" name="humidity" value={formData.humidity} onChange={handleChange} required />
            </div>
            <div className="form-group">
                <label htmlFor="ph">Soil pH:</label>
                <input type="number" step="any" id="ph" name="ph" value={formData.ph} onChange={handleChange} required />
            </div>
            <div className="form-group">
                <label htmlFor="rainfall">Rainfall (mm):</label>
                <input type="number" step="any" id="rainfall" name="rainfall" value={formData.rainfall} onChange={handleChange} required />
            </div>
            <button type="submit" className="btn">Predict Crop</button>
        </form>
    );
};

export default CropForm;