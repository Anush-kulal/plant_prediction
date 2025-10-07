import React from 'react';

const Prediction = ({ prediction }) => {
    return (
        <div className="prediction">
            {prediction ? (
                <h2>Predicted Crop: {prediction}</h2>
            ) : (
                <h2>No prediction available</h2>
            )}
        </div>
    );
};

export default Prediction;