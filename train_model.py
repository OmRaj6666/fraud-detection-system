import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("data/transactions.csv")

# Encode categorical feature
encoder = LabelEncoder()
data["Transaction_Type"] = encoder.fit_transform(data["Transaction_Type"])

X = data[["Time", "Amount", "Transaction_Type", "Is_International"]]
y = data["Is_Fraud"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# Evaluation
print("\nClassification Report:\n")
print(classification_report(y_test, model.predict(X_test)))

# Save artifacts
joblib.dump(model, "fraud_model.pkl")
joblib.dump(encoder, "transaction_type_encoder.pkl")

print("✅ Model & encoder saved")
