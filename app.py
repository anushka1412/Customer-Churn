import streamlit as st
import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("customer_churn_model.keras")

st.set_page_config(page_title="Customer Churn Prediction")

st.title("🏦 Customer Churn Prediction")

st.write("Enter the customer details below:")

# Inputs
credit_score = st.number_input("Credit Score", 300, 900, 600)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

age = st.number_input("Age", 18, 100, 40)

tenure = st.number_input("Tenure", 0, 10, 3)

balance = st.number_input("Balance", 0.0, 300000.0, 60000.0)

num_products = st.number_input(
    "Number of Products",
    1,
    4,
    2
)

has_card = st.selectbox(
    "Has Credit Card",
    ["No", "Yes"]
)

is_active = st.selectbox(
    "Is Active Member",
    ["No", "Yes"]
)

salary = st.number_input(
    "Estimated Salary",
    0.0,
    300000.0,
    50000.0
)

# Prediction
if st.button("Predict"):

    # One-Hot Encoding
    germany = 1 if geography == "Germany" else 0
    spain = 1 if geography == "Spain" else 0

    # Label Encoding
    gender = 1 if gender == "Male" else 0
    has_card = 1 if has_card == "Yes" else 0
    is_active = 1 if is_active == "Yes" else 0

    # Feature vector
    features = np.array([[
        credit_score,
        germany,
        spain,
        gender,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        is_active,
        salary
    ]])

    prediction = model.predict(features)

    probability = prediction[0][0]

    st.write(f"Churn Probability: **{probability:.2f}**")

    if probability > 0.5:
        st.error("❌ Customer is likely to leave the bank.")
    else:
        st.success("✅ Customer is likely to stay with the bank.")
