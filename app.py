import streamlit as st
import pandas as pd
import pickle
import os

# -------------------------------
# Page Config (must be first Streamlit command)
# -------------------------------
st.set_page_config(page_title="Churn Prediction", layout="centered")

# -------------------------------
# Debug: Check files (optional)
# -------------------------------
st.write("Files in directory:", os.listdir())

# -------------------------------
# Load Model (ONLY ONCE)
# -------------------------------
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -------------------------------
# Custom CSS (Advanced UI)
# -------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    color: #f1f1f1;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
}

.success-box {
    background-color: #28a745;
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
}

.error-box {
    background-color: #dc3545;
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown('<div class="title">🏦 Bank Churn Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered prediction system</div>', unsafe_allow_html=True)

# -------------------------------
# Input Card
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 900, 600)
    age = st.number_input("Age", 18, 100, 30)
    tenure = st.number_input("Tenure", 0, 10, 3)
    balance = st.number_input("Balance", 0.0, 200000.0, 50000.0)

with col2:
    geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    num_products = st.number_input("Products", 1, 4, 1)
    has_card = st.selectbox("Has Credit Card", [0, 1])
    is_active = st.selectbox("Active Member", [0, 1])

salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Predict Now"):

    input_data = pd.DataFrame({
        "CreditScore": [credit_score],
        "Geography": [geography],
        "Gender": [gender],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_products],
        "HasCrCard": [has_card],
        "IsActiveMember": [is_active],
        "EstimatedSalary": [salary]
    })

    try:
        prediction = model.predict(input_data)

        st.markdown("<br>", unsafe_allow_html=True)

        if prediction[0] == 1:
            st.markdown('<div class="error-box">❌ High Risk: Customer will EXIT</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="success-box">✅ Low Risk: Customer will STAY</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction error: {e}")
