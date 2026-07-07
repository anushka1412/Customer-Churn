import streamlit as st
import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("customer_churn_model.keras")

st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score", 300, 900, 600)
age = st.number_input("Age", 18, 100, 40)
tenure = st.number_input("Tenure", 0, 10, 3)
balance = st.number_input("Balance", 0.0, 300000.0, 60000.0)
products = st.number_input("Number of Products", 1, 4, 2)

credit_card = st.selectbox("Has Credit Card", ["No", "Yes"])
active = st.selectbox("Is Active Member", ["No", "Yes"])
gender = st.selectbox("Gender", ["Female", "Male"])
country = st.selectbox("Country", ["France", "Germany", "Spain"])
salary = st.number_input("Estimated Salary", 0.0, 300000.0, 50000.0)

# One-hot encoding
geo_france = 1 if country == "France" else 0
geo_germany = 1 if country == "Germany" else 0
geo_spain = 1 if country == "Spain" else 0

gender = 1 if gender == "Male" else 0
credit_card = 1 if credit_card == "Yes" else 0
active = 1 if active == "Yes" else 0

if st.button("Predict"):

    data = np.array([[geo_france,
                      geo_germany,
                      geo_spain,
                      credit_score,
                      gender,
                      age,
                      tenure,
                      balance,
                      products,
                      credit_card,
                      active,
                      salary]])

    prediction = model.predict(data)

    if prediction[0][0] > 0.5:
        st.error("Customer is likely to leave the bank.")
    else:
        st.success("Customer is likely to stay with the bank.")
