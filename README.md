# Plant Prediction Web Application

This project is a web application built with Flask that uses a pre-trained Scikit-learn model to make predictions about plants based on user input.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- A web interface to input data for prediction.
- A machine learning model to process the input and return a prediction.
- Built on a lightweight and robust Flask backend.

## Technologies Used

This project relies on several open-source libraries:

- **Backend:**
  - [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework.
  - [Werkzeug](https://werkzeug.palletsprojects.com/): A comprehensive WSGI web application library.
  - [Jinja2](https://jinja.palletsprojects.com/): A modern and designer-friendly templating language for Python.

- **Machine Learning & Data Handling:**
  - [Scikit-learn](https://scikit-learn.org/): Machine learning library for Python.
  - [Pandas](https://pandas.pydata.org/): Data analysis and manipulation tool.
  - [NumPy](https://numpy.org/): The fundamental package for scientific computing with Python.
  - [Joblib](https://joblib.readthedocs.io/): Used for saving and loading the trained model.

## Setup and Installation

Follow these steps to get the project running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd plant_prediction
    ```

2.  **Create and activate a virtual environment:**
    - On Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    flask run
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
├── app.py              # Main Flask application logic
├── model.pkl           # Pre-trained machine learning model
├── requirements.txt    # List of project dependencies
├── static/             # Static files (CSS, JavaScript, images)
└── templates/          # HTML templates for the web pages
```