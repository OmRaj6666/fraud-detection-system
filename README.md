💳 Fraud Detection System (Machine Learning)
📌 Overview

The Fraud Detection System is a machine learning–based application designed to identify potentially fraudulent financial transactions in real time.
It simulates how banks and fintech companies assess transaction risk using historical transaction data and predictive analytics.

This project demonstrates end-to-end ML workflow including data preprocessing, model training, evaluation, and deployment via an interactive web interface.

🎯 Objectives

Detect fraudulent transactions using supervised machine learning

Minimize false positives while maintaining high detection accuracy

Provide an interactive interface for real-time fraud prediction

Demonstrate industry-level ML deployment practices

🧠 Machine Learning Approach

Algorithm Used: Random Forest Classifier

Why Random Forest?

Handles non-linear relationships well

Robust against overfitting

Widely used in financial fraud detection

📊 Dataset Description

The dataset (transactions.csv) contains simulated transaction records with the following features:

Feature	Description
Time	Transaction time in minutes
Amount	Transaction amount
Transaction_Type	Mode of transaction (Online, POS, ATM)
Is_International	Whether transaction is international (0/1)
Is_Fraud	Target variable (0 = Legitimate, 1 = Fraud)
⚙️ System Workflow

Transaction data is loaded and preprocessed

Categorical features are encoded

Model is trained using historical data

Model is saved for reuse

User inputs transaction details via web UI

Model predicts fraud risk instantly

🖥️ Application Features

Interactive web interface using Streamlit

Real-time fraud prediction

Encoded categorical handling

Model persistence using joblib

Clear fraud / non-fraud alerts

📁 Project Structure




🚀 How to Run the Project
1️⃣ Create Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model
python3 train_model.py


This will generate:

fraud_model.pkl

transaction_type_encoder.pkl

4️⃣ Run the Web Application
streamlit run app.py

🖥️ Application Screenshots:



Open browser at:



📈 Model Evaluation

The model is evaluated using:

Precision

Recall

F1-Score

Accuracy

Example output:

Accuracy:   88%
Precision:  0.84
Recall:     0.81
F1-Score:   0.82


(High accuracy due to small demo dataset; scalable to real datasets)

🔐 Real-World Use Cases

Banking transaction monitoring

Credit card fraud detection

E-commerce payment security

Fintech risk assessment systems

🧩 Limitations

Uses simulated dataset

Small dataset size

Does not include real customer behavior patterns

🚀 Future Enhancements

Large-scale real transaction dataset

Feature engineering (location, device change, velocity checks)

Imbalanced data handling (SMOTE)

Model explainability (SHAP)

REST API deployment

Cloud hosting

🎓 Skills Demonstrated

Machine Learning

Data Preprocessing

Model Training & Evaluation

Feature Encoding

Streamlit Deployment

End-to-End ML Pipeline

