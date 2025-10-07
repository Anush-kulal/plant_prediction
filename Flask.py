from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Define the path to your model and the feature names it expects
MODEL_PATH = "crop_recommendation_model.pkl"
feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Load the machine learning model from the pickle file
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            inputs = [float(request.form.get(feature, 0)) for feature in feature_names]
            input_df = pd.DataFrame([inputs], columns=feature_names)
            prediction = model.predict(input_df)[0]
            # Assuming the model returns the crop name as a string.
            prediction_result = f"The recommended crop is: {prediction.capitalize()}"
        except Exception as e:
            prediction_result = f"Error during prediction: {str(e)}"
    
    return render_template('index.html', prediction=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
