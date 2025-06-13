import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('customer_churn_model.pkl')

# Streamlit app title
st.title('Kachex.Model Customer Churn Prediction')

# User input for features
def user_input_features():
    # Define input fields for features
    payment_method = st.selectbox('Payment Method', options=['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card'])
    # Add more input fields as necessary
    data = {
        'PaymentMethod': payment_method,
        # Add other features here
    }
    return pd.DataFrame(data, index=[0])

input_data = user_input_features()

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write('Churn Prediction:', 'Yes' if prediction[0] == 1 else 'No') 