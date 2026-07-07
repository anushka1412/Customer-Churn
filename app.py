
import streamlit as st
import pickle
import numpy as np

# Load model
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Iris Flower Classifier")

st.write("Enter the features below:")
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.2)

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

if st.button("Predict"):
    prediction = model.predict(features)
    class_names=['Setosa', 'Veriscolor', 'Virginica']
    st.success(f"The predicted iris species is: {class_names[prediction[0]]}")
