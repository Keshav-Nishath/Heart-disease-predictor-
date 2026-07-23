import pandas as pd
import streamlit as st
import pickle as pk
from sklearn.model_selection import train_test_split as TTS
from sklearn.naive_bayes import GaussianNB
import numpy as np
st.title("heart disease predictor")
st.header("Input details")
st.markdown(
    """
    <style>
     background-image: url('file:///C:/Users/kesha/OneDrive/Desktop/code/vs code/pic.png');
     background-size:cover;
    </style>
    """,
    unsafe_allow_html=True
)



model=pk.load(open("heart_model.pkl","rb"))
age=st.number_input("age",1,120)
sexstr=st.selectbox("Gender",["Male","female"])

sex=1 if sexstr=="Male" else 0
cp=st.number_input("chest pain",1,4)
trestbps = st.number_input("Resting blood pressure (mm Hg on admission)", 80, 200)

chol = st.number_input("Serum cholesterol (mg/dl)", 100, 600)

fbstext = st.selectbox("Do you have fasting blood sugar > 120 mg/dl?", ["Yes", "No"])
fbs = 1 if fbstext == "Yes" else 0

restecg = st.number_input("Resting ECG results (0=normal, 1=ST-T abnormality, 2=LVH)", 0, 2)

thalach = st.number_input("Maximum heart rate achieved", 60, 220)

exang_text = st.selectbox("Exercise induced angina?", ["Yes", "No"])
exang = 1 if exang_text == "Yes" else 0

oldpeak = st.number_input("ST depression induced by exercise (oldpeak)", 0.0, 10.0, step=0.1)

slope = st.number_input("Slope of the peak exercise ST segment (0–2)", 0, 2)

ca = st.number_input("Number of major vessels colored by fluoroscopy (0–3)", 0, 3)

thal = st.number_input("Thalassemia (1=normal, 2=fixed defect, 3=reversible defect)", 1, 3)

if st.button("predict"):
     features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,thalach, exang, oldpeak, slope, ca, thal]])
     prediction = model.predict(features)
    
     if prediction[0] == 1:
        st.error("⚠️ You may have a risk of heart disease. Please consult a doctor.")
     else:
        st.success("✅ No heart disease detected. Stay healthy!")