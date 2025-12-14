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

<img width="277" height="258" alt="Screenshot 2025-12-14 at 11 24 38 PM" src="https://github.com/user-attachments/assets/97b83ad1-17a5-4063-baa5-93df83359db3" />




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

<img width="1470" height="956" alt="Screenshot 2025-12-14 at 11 21 18 PM" src="https://github.com/user-attachments/assets/309bdddd-3144-4ef4-bc3d-3d7fde9f6bc0" />

<img width="1470" height="956" alt="Screenshot 2025-12-14 at 11 21 31 PM" src="https://github.com/user-attachments/assets/ffa16b41-a615-429e-9ce9-2b6d2ea6a8cf" />

<img width="1470" height="956" alt="Screenshot 2025-12-14 at 11 21 46 PM" src="https://github.com/user-attachments/assets/8fe05459-68ff-4181-b7a8-382e1678144e" />

<img width="1470" height="956" alt="Screenshot 2025-12-14 at 11 22 01 PM" src="https://github.com/user-attachments/assets/e82106ca-8386-464d-a8c9-592dfa878877" />

<img width="1470" height="956" alt="Screenshot 2025-12-14 at 11 22 06 PM" src="https://github.com/user-attachments/assets/0567dc17-48d7-48b0-af0c-8b0bbf47ad32" />

##System Architecture Diagram

<img width="1245" height="476" alt="TP7FRXGn3CRlUGfh3mWEM-uSK2lAIfMcekfIJaZ8JRpRY8mJEHxGW91u1zwG9y7PBDe_KayJ-_ly-JV9PLKKdSRaD6eYM0bE0Qv9oMlC3EkvAetmz_SVk1B_55j_4d8ElMQ1XqhYd5WJUMlZYvLaLk800yua2_Zf07mUIsPYXSLQXN1CKU6gbC_y4akvAFEh1M25XnltwoJhTe0Rtf0GUtech-FU2ONOUMzpe6J1zyWXZx3A" src="https://github.com/user-attachments/assets/c9db3214-ed8a-40f9-a05d-5faa160251e9" />





Open browser at: https://fraud-detection-system-cojmzsw6vuktu8dqlvqect.streamlit.app/



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

