import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# Load model and preprocessing objects
model = tf.keras.models.load_model("customer_churn_model.keras")
sc = joblib.load("sc.pkl")
gender_encoder = joblib.load("gender_encoder.pkl")
ct = joblib.load("ct.pkl")

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

st.title("🏦 Customer Churn Prediction")

st.write("Enter the customer details below to predict whether the customer is likely to leave the bank.")

credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

age = st.number_input("Age", min_value=18, max_value=100, value=35)

tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)

balance = st.number_input("Balance", min_value=0.0, value=50000.0)

num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)

has_card = st.selectbox(
    "Has Credit Card?",
    [0, 1]
)

active_member = st.selectbox(
    "Is Active Member?",
    [0, 1]
)

salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)
if st.button("Predict"):

    # Encode gender
    gender_encoded = gender_encoder.transform([gender])[0]

    # Create input in the same order used during training
    input_data = np.array([[
        credit_score,
        geography,
        gender_encoded,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        active_member,
        salary
    ]], dtype=object)

    # Apply the saved OneHotEncoder
    input_data = ct.transform(input_data)

    # Scale the input
    input_data = sc.transform(input_data)

    # Predict
    prediction = model.predict(input_data)

    probability = prediction[0][0]
        st.subheader("Prediction Result")

    st.write(f"Churn Probability: {probability:.2%}")

    if probability >= 0.5:
        st.error("❌ Customer is likely to leave the bank.")
    else:
        st.success("✅ Customer is likely to stay with the bank.")
