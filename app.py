from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pickle
import traceback
#Aditya Rahangdale @vitbhopal 
app = Flask(__name__,template_folder="template")

def load_model():
    try:
        # Ensure the path to your model file is correct
        model_path = 'C:/Users/aditya rahangdale/Desktop/Water Quality Prediction/model.pkl'  # Path to your model file
        model = joblib.load(model_path)
        print(f"Model loaded: {type(model)}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        traceback.print_exc()
        return None
loaded_model = load_model()

@app.route('/')
def index():
    return render_template('predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    if loaded_model is None:
        return jsonify({'error': 'Model is not loaded properly'})

    try:
        data = request.form

        # Convert input values to floats and handle errors
        features = []
        try:
            features.append(float(data['ph']))
            features.append(float(data['Hardness']))
            features.append(float(data['Solids']))
            features.append(float(data['Chloramines']))
            features.append(float(data['Sulfate']))
            features.append(float(data['Conductivity']))
            features.append(float(data['Organic_carbon']))
            features.append(float(data['Trihalomethanes']))
            features.append(float(data['Turbidity']))
        except ValueError as ve:
            return jsonify({'error': f'ValueError: {str(ve)}'})

        # Ensure the correct length of features
        if len(features) != 9:
            return jsonify({'error': 'Incorrect number of features'})

        # Make prediction
        prediction = loaded_model.predict([features])[0]
        # Convert NumPy int32 to Python int for JSON serialization
        prediction = int(prediction)

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/page_0')
def page_0():
 return render_template('page_0.html')

@app.route('/page_1')
def page_1():
   return render_template('page_1.html')

if __name__ == '__main__':
    app.run(debug=True)