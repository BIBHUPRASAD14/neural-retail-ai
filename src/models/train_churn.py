from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Train a churn prediction model using RFM features
def train_churn_model(rfm):
    print("🔹 Training churn model...")

    # Create a simple churn label based on Recency (e.g., churn if not purchased in last 90 days)
    rfm["Churn"] = rfm["Recency"].apply(lambda x: 1 if x > 90 else 0)

    X = rfm[["Recency", "Frequency", "Monetary"]]
    y = rfm["Churn"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model Accuracy: {acc:.2f}")

    return model, rfm