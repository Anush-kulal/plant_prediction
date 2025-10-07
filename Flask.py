from flask import Flask, request, render_template, jsonify
from functools import wraps
import pickle
import numpy as np
import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Constants
MODEL_PATH = "crop_recommendation_model.pkl"
FEATURE_NAMES = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
FEATURE_RANGES = {
    'N': (0, 140),    # kg/ha
    'P': (5, 145),    # kg/ha
    'K': (5, 205),    # kg/ha
    'temperature': (8.83, 43.7),  # °C
    'humidity': (14.3, 99.98),    # %
    'ph': (3.5, 9.94),           # pH scale
    'rainfall': (20.21, 298.56)   # mm
}

def load_model():
    """Load the machine learning model from pickle file."""
    try:
        with open(MODEL_PATH, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        raise

def validate_input(data):
    """Validate input data against defined ranges."""
    errors = []
    for feature, (min_val, max_val) in FEATURE_RANGES.items():
        value = data.get(feature)
        if value is None:
            errors.append(f"Missing value for {feature}")
        elif not isinstance(value, (int, float)):
            errors.append(f"Invalid type for {feature}")
        elif value < min_val or value > max_val:
            errors.append(f"{feature} should be between {min_val} and {max_val}")
    return errors

# Load model at startup
try:
    model = load_model()
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    model = None

@app.route('/', methods=['GET', 'POST'])
def home():
    """Handle both GET and POST requests for the home page."""
    prediction_result = None
    if request.method == 'POST':
        try:
            # Extract and validate inputs
            inputs = {feature: float(request.form.get(feature, 0)) for feature in FEATURE_NAMES}
            validation_errors = validate_input(inputs)
            
            if validation_errors:
                prediction_result = f"Validation errors: {', '.join(validation_errors)}"
            else:
                # Make prediction
                input_df = pd.DataFrame([list(inputs.values())], columns=FEATURE_NAMES)
                prediction = model.predict(input_df)[0]
                prediction_result = f"The recommended crop is: {prediction.capitalize()}"
                
                # Log successful prediction
                logger.info(f"Successful prediction: {prediction} for inputs: {inputs}")
                
        except ValueError as ve:
            prediction_result = "Invalid input: Please ensure all fields contain valid numbers"
            logger.warning(f"Invalid input received: {str(ve)}")
        except Exception as e:
            prediction_result = "An error occurred during prediction"
            logger.error(f"Prediction error: {str(e)}")
    
    return render_template('index.html', prediction=prediction_result)

@app.route('/api/predict', methods=['POST'])
def predict_api():
    """API endpoint for predictions."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Validate inputs
        inputs = {feature: float(data.get(feature, 0)) for feature in FEATURE_NAMES}
        validation_errors = validate_input(inputs)
        
        if validation_errors:
            return jsonify({"error": "Validation failed", "details": validation_errors}), 400
            
        # Make prediction
        input_df = pd.DataFrame([list(inputs.values())], columns=FEATURE_NAMES)
        prediction = model.predict(input_df)[0]
        
        return jsonify({
            "success": True,
            "prediction": prediction.capitalize(),
            "timestamp": datetime.now().isoformat()
        })
        
    except ValueError as ve:
        return jsonify({"error": "Invalid input format"}), 400
    except Exception as e:
        logger.error(f"API prediction error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return render_template('index.html', prediction="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('index.html', prediction="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True)
