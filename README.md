❤️ Heart Disease Prediction App

This Streamlit web app predicts the likelihood of heart disease based on patient health parameters using a trained machine learning model (Cleveland Heart Disease dataset).

🚀 Overview

The app uses 13 clinical input features such as age, sex, chest pain type, blood pressure, cholesterol levels, and others to predict whether a person is likely to have heart disease.

The prediction is powered by a pre-trained model saved in the file cleveland heart data.pkl.

🧠 Features Used for Prediction
Feature	Description
age	Age of the patient
sex	Sex (1 = male, 0 = female)
cp	Chest pain type (0–3)
trestbps	Resting blood pressure (mm Hg)
chol	Serum cholesterol (mg/dl)
fbs	Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
restecg	Resting ECG results (0–2)
thalach	Maximum heart rate achieved
exang	Exercise induced angina (1 = yes, 0 = no)
oldpeak	ST depression induced by exercise
slope	Slope of the peak exercise ST segment (0–2)
ca	Number of major vessels (0–4)
thal	Thalassemia type (0–3)
🧩 Installation

Clone this repository

git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py

🖥️ Usage

Enter the patient's details in the sidebar input fields.

Click on "Predict".

The app will display either:

✅ Low Risk of Heart Disease

⚠️ High Risk of Heart Disease

📦 Project Structure
📁 heart-disease-prediction/
│
├── app.py                      # Streamlit application file
├── cleveland heart data.pkl    # Trained ML model
├── requirements.txt            # Dependencies
└── README.md                   # Documentation

🌐 Deployment

You can deploy this app easily on Streamlit Cloud:

Push your project to a GitHub repository.

Visit https://streamlit.io/cloud
.

Connect your GitHub repo and deploy — Streamlit will auto-detect app.py.



🧑‍💻 Author

Vishal Ramteke
Built using Python, Streamlit, and Scikit-learn.
