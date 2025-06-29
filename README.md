# 🩺 Diabetes Prediction Web App

This is a Flask-based machine learning web application that predicts whether a person is likely to have diabetes based on medical parameters like glucose, insulin, BMI, and more.

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

---

## 📊 Dataset

The app uses the **PIMA Indians Diabetes Dataset**, which contains the following features:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome (target: 1 = diabetic, 0 = non-diabetic)

---

## 🚀 Features

- User-friendly web form with medical hints
- Trained using `LogisticRegression`, Decision Tree, SVM & Naive Bayes
- Preprocessing with `StandardScaler`
- Real-time predictions via Flask
- Result opens in a new tab
- Responsive and clean UI

---

## 🛠️ Installation & Setup

### Prerequisites:

- Python 3.x
- Git
- pip

### Clone the repo:

```bash
git clone https://github.com/faisal-16082000/diabetes-prediction.git
cd diabetes-prediction
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python app.py
