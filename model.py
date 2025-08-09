import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Paths
DATA_PATH = os.path.join("dataset", "fitness_subscription_dataset.csv")
MODEL_PATH = os.path.join("model", "logistic_regression_model.pkl")

# 1. Load dataset
df = pd.read_csv(DATA_PATH)

# 2. Separate features and target
X = df.drop("Will_Buy", axis=1)
y = df["Will_Buy"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Create Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 6. Predictions
y_pred = model.predict(X_test_scaled)

# 7. Evaluation
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# 8. Save model + scaler
os.makedirs("model", exist_ok=True)
with open(MODEL_PATH, "wb") as f:
    pickle.dump({"model": model, "scaler": scaler}, f)

print(f"💾 Model and scaler saved to {MODEL_PATH}")