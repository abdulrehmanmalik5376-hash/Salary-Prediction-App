import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.set_page_config(page_title="Salary Prediction", page_icon="💰")

st.title("💰 Salary Prediction App")
st.write("Predict salary based on years of experience.")

experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.1
)

if st.button("Predict Salary"):
    prediction = model.predict(np.array([[experience]]))
    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")