import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("cleveland heart data.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app title
st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details below to predict the likelihood of heart disease.")

# Create input fields for the features
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=250, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [1, 0])
restecg = st.selectbox("Resting ECG Results (0–2)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [1, 0])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1, value=1.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment (0–2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect, 3 = Unknown)", [0, 1, 2, 3])

# When user clicks Predict
if st.button("🔍 Predict"):
    # Prepare input data for model
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    if prediction == 1:
        st.error("⚠️ The model predicts a high risk of heart disease.")
    else:
        st.success("✅ The model predicts a low risk of heart disease.")

# Footer
st.write("---")
st.caption("Model trained on Cleveland Heart Disease dataset.")
