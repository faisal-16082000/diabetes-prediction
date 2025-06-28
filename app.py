from flask import Flask, request, render_template
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load scaler and model
model_path = os.path.join('models', 'modelForRegression.pkl')
scaler_path = os.path.join('models', 'standard_scaler.pkl')

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(scaler_path, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs from form
        features = [float(request.form.get(field)) for field in [
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
        ]]

        # Transform and predict
        input_scaled = scaler.transform([features])
        prediction = model.predict(input_scaled)[0]

        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        return render_template('result.html', prediction_text=f"Prediction: {result}")

    except Exception as e:
        return render_template('result.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
