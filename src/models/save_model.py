import joblib
import os

# Save the trained model to disk using joblib
def save_model(model, filename):
    os.makedirs("models", exist_ok=True)
    path = f"models/{filename}"
    joblib.dump(model, path)
    print(f"✅ Model saved at {path}")