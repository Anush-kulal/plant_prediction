import React, { useState } from 'react';
import CropForm from './components/CropForm';
import Prediction from './components/Prediction';
import './App.css';

function App() {
    const [formData, setFormData] = useState({
        N: '',
        P: '',
        K: '',
        temperature: '',
        humidity: '',
        ph: '',
        rainfall: ''
    });
    const [prediction, setPrediction] = useState('');

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            const data = await response.json();
            setPrediction(data.prediction);
        } catch (error) {
            console.error('Error fetching prediction:', error);
        }
    };

    return (
        <div className="App">
            <h1>Crop Recommendation System</h1>
            <CropForm 
                formData={formData} 
                handleInputChange={handleInputChange} 
                handleSubmit={handleSubmit} 
            />
            <Prediction prediction={prediction} />
        </div>
    );
}

export default App;