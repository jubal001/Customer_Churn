# Customer_Churn
Two machine learning models were trained: Logistic Regression and Random Forest. Random Forest was selected as the final model because it achieved a higher F1-score and recall, meaning it was better at identifying customers likely to churn.
# Customer Churn Prediction Using Machine Learning

# Project Overview

Customer churn prediction is an important task for businesses because retaining existing customers is often cheaper than acquiring new ones.

This project uses Machine Learning techniques to predict whether a telecom customer is likely to churn (leave the service) or stay.

The project includes Exploratory Data Analysis (EDA), data preprocessing, model training, evaluation, and deployment using Streamlit.

# Dataset

Dataset used: Telco Customer Churn Dataset

The dataset contains information about telecom customers such as:

Demographics
Account information
Services subscribed
Billing information

Target variable:

Churn

Yes - Customer leaves
No - Customer stays

# Project Structure

customer-churn-ml/
data/
- Custormer_churn.csv

model/
- churn_model.pkl
- model_columns.pkl

app.py
train_model.py
requirements.txt
README.md

# Exploratory Data Analysis (EDA)

The dataset was explored to understand patterns and relationships between features and customer churn.

Key steps performed:

Checked dataset structure and data types
Identified missing values
Analyzed churn distribution
Explored relationships between:

Contract type and churn
Internet service and churn
Monthly charges and churn

Important observations:

Customers with Month-to-month contracts tend to churn more.
Fiber optic users show higher churn rates.
Customers with higher monthly charges are more likely to churn.

# Data Preprocessing

Several preprocessing techniques were applied before training the models:

1. Handling Missing Values

 `TotalCharges` column converted to numeric
Rows with missing values were removed.

2. Feature Cleaning

Removed unnecessary column: `CustomerID`

3. Target Encoding

Converted Churn values:

    Yes - 1
    No - 0

4. Categorical Encoding

Used One-Hot Encoding (`pd.get_dummies`) to convert categorical variables into numeric features.

5. Train-Test Split

80% training data
20% testing data

# Machine Learning Models

Two classification models were trained:

# 1. Logistic Regression

Logistic Regression is a simple and interpretable model commonly used for binary classification problems.

# 2. Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

# Model Evaluation

The models were evaluated using the following metrics:

Recall
F1-Score

These metrics are important for churn prediction because we want to correctly identify customers who are likely to leave.

Example results:

| Model               | Recall | F1 Score |
| ------------------- | ------ | -------- |
| Logistic Regression | 0.78   | 0.74     |
| Random Forest       | 0.84   | 0.80     |

# Final Model Selection

The Random Forest model was selected as the final model because:

It achieved higher Recall and F1-score
It captured complex relationships in the data better than Logistic Regression.

Feature Importance

Feature importance analysis showed that the most influential features for predicting churn include:

MonthlyCharges
TotalCharges
Contract type
InternetService
Tenure

These factors strongly influence whether customers remain with the telecom provider.

# Streamlit Deployment

The final model was deployed using Streamlit to create an interactive web application where users can input customer information and receive a churn prediction.

Run the application using:

streamlit run app.py

# Live App

Streamlit Deployment Link:

Add your Streamlit app link here

Example:

https://CUSTORMER-CHURN-PREDICTION-APPLICATION.streamlit.app

# Installation

Install the required dependencies:

pip install -r requirements.txt

# Technologies Used

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit
Joblib

# Author

Machine Learning Project
Customer Churn Prediction Assignment
Jay Tech
