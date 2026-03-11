import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/churn_model.pkl")
columns = joblib.load("model/model_columns.pkl")

st.title("CUSTORMER CHURN PREDICTION APPLICATION")

st.write("Enter Customer Information")

SeniorCitizen = st.selectbox("Senior Citizen", [0,1])
Tenure = st.number_input("Tenure (Months)", 0, 100)
MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

Gender = st.selectbox("Gender", ["Male","Female"])
Partner = st.selectbox("Partner", ["Yes","No"])
Dependents = st.selectbox("Dependents", ["Yes","No"])
PhoneService = st.selectbox("Phone Service", ["Yes","No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes","No"])
InternetService = st.selectbox("Internet Service", ["DSL","Fiber optic","No"])
Contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes","No"])
PaymentMethod = st.selectbox("Payment Method",
["Electronic check","Mailed check","Bank transfer","Credit card"])

input_dict = {
"SeniorCitizen":SeniorCitizen,
"Tenure":Tenure,
"MonthlyCharges":MonthlyCharges,
"TotalCharges":TotalCharges,
"Gender_Male":1 if Gender=="Male" else 0,
"Partner_Yes":1 if Partner=="Yes" else 0,
"Dependents_Yes":1 if Dependents=="Yes" else 0,
"PhoneService_Yes":1 if PhoneService=="Yes" else 0,
"MultipleLines_Yes":1 if MultipleLines=="Yes" else 0,
"InternetService_Fiber optic":1 if InternetService=="Fiber optic" else 0,
"InternetService_No":1 if InternetService=="No" else 0,
"OnlineSecurity_Yes":0,
"OnlineBackup_Yes":0,
"DeviceProtection_Yes":0,
"TechSupport_Yes":0,
"StreamingTV_Yes":0,
"StreamingMovies_Yes":0,
"Contract_One year":1 if Contract=="One year" else 0,
"Contract_Two year":1 if Contract=="Two year" else 0,
"PaperlessBilling_Yes":1 if PaperlessBilling=="Yes" else 0,
"PaymentMethod_Credit card":1 if PaymentMethod=="Credit card" else 0,
"PaymentMethod_Electronic check":1 if PaymentMethod=="Electronic check" else 0,
"PaymentMethod_Mailed check":1 if PaymentMethod=="Mailed check" else 0
}

input_df = pd.DataFrame([input_dict])

# Align columns
input_df = input_df.reindex(columns=columns, fill_value=0)

if st.button("Predict Churn"):

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("Customer is likely to CHURN")
    else:

        st.success("Customer will likely STAY")

