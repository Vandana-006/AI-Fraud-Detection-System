import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("fraud_model.pkl", "rb"))

st.title("💳 AI Fraud Detection System")

amount = st.number_input("Transaction Amount")

if st.button("Predict"):

    features = np.array([[amount]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected")
    else:
        st.success("✅ Transaction is Safe")