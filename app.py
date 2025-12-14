import streamlit as st
import pandas as pd
import joblib

# Load artifacts
model = joblib.load("fraud_model.pkl")
encoder = joblib.load("transaction_type_encoder.pkl")

st.set_page_config(page_title="Fraud Detection System", layout="centered")
st.title("💳 Intelligent Fraud Detection System")

st.caption("Hybrid Rule + ML Based Risk Assessment")

# ==========================
# USER INPUTS
# ==========================
time = st.slider("Transaction Time (minutes)", 0, 1440, 120)
amount = st.number_input("Transaction Amount", 0.0, 100000.0, 500.0)

transaction_type = st.selectbox(
    "Transaction Type",
    encoder.classes_
)

is_international = st.selectbox(
    "Is International Transaction?",
    ["No", "Yes"]
)

# ==========================
# FEATURE ENGINEERING
# ==========================
transaction_type_encoded = encoder.transform([transaction_type])[0]
is_international = 1 if is_international == "Yes" else 0

input_df = pd.DataFrame([{
    "Time": time,
    "Amount": amount,
    "Transaction_Type": transaction_type_encoded,
    "Is_International": is_international
}])

# ==========================
# RULE ENGINE (HARD RULES)
# ==========================
rule_flags = []

if amount > 50000:
    rule_flags.append("High transaction amount")

if is_international == 1 and amount > 20000:
    rule_flags.append("High-value international transaction")

# ==========================
# PREDICTION
# ==========================
if st.button("🔍 Analyze Transaction"):
    fraud_prob = model.predict_proba(input_df)[0][1] * 100

    st.subheader("📊 Fraud Risk Analysis")

    st.metric("Fraud Probability", f"{fraud_prob:.2f}%")

    # Risk level
    if fraud_prob < 30:
        risk = "LOW"
        st.success("✅ Low Risk Transaction")
    elif fraud_prob < 70:
        risk = "MEDIUM"
        st.warning("⚠️ Medium Risk – Manual Review Suggested")
    else:
        risk = "HIGH"
        st.error("🚨 High Risk – Transaction Blocked")

    # ==========================
    # RULE-BASED ALERTS
    # ==========================
    if rule_flags:
        st.subheader("🚨 Rule-Based Alerts")
        for rule in rule_flags:
            st.error(rule)

    # ==========================
    # EXPLAINABILITY
    # ==========================
    st.subheader("🧠 Decision Explanation")
    st.write(
        f"""
        - Amount: ₹{amount}
        - International: {'Yes' if is_international else 'No'}
        - Transaction Type: {transaction_type}
        - Risk Level: {risk}
        """
    )
