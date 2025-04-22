import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# App title
st.title('🚗 Car Price Prediction App')

# Sidebar input form
st.sidebar.header("Input Car Details")

def user_input():
    present_price = st.sidebar.slider("Present Price (in lakhs)", 0.0, 50.0, 5.0)
    driven_kms = st.sidebar.number_input("Kilometers Driven", 100, 1000000, 50000)
    owner = st.sidebar.selectbox("Number of Previous Owners", [0, 1, 2, 3])
    fuel_type = st.sidebar.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])
    transmission = st.sidebar.selectbox("Transmission Type", ['Manual', 'Automatic'])
    selling_type = st.sidebar.selectbox("Selling Type", ['Dealer', 'Individual'])
    car_age = st.sidebar.slider("Age of Car (years)", 0, 25, 5)

    data = {
        'Present_Price': present_price,
        'Driven_kms': driven_kms,
        'Owner': owner,
        'Fuel_Type': fuel_type,
        'Transmission': transmission,
        'Selling_type': selling_type,
        'Car_Age': car_age
    }
    return pd.DataFrame([data])

# Get user input
input_df = user_input()

# Display the input
st.subheader("Input Summary")
st.write(input_df)

# Make prediction
if st.button("Predict Selling Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Selling Price: ₹ {prediction[0]:.2f} lakhs")
