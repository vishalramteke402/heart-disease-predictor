import streamlit as st
import pandas as pd
import pickle
import numpy as np

# -----------------------------
# Load the trained model
# -----------------------------
model = pickle.load(open('heart disease predictor.pkl', 'rb'))

# -----------------------------
# App title
# -----------------------------
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

st.title("❤️ Heart Disease Prediction App")
st.markdown("""
This app predicts the likelihood of **heart disease** based on patient data.
Fill in the details below and click **Predict**.
""")

# -----------------------------
# Input fields
# -----------------------------
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=250, value=120)
chol = st.number_input("Serum Cholestoral in mg/dl (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict"):
    # Collect all inputs into an array
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error("⚠️ The model predicts that this person **may have heart disease.**")
    else:
        st.success("✅ The model predicts that this person **is unlikely to have heart disease.**")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
