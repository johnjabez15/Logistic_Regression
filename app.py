from flask import Flask, request, render_template
import pickle
import numpy as np
import os

# Paths
MODEL_PATH = os.path.join("model", "logistic_regression_model.pkl")

# Load model and scaler
with open(MODEL_PATH, "rb") as f:
    data = pickle.load(f)
    model = data["model"]
    scaler = data["scaler"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        age = float(request.form["age"])
        income = float(request.form["income"])
        exercise = float(request.form["exercise"])
        bmi = float(request.form["bmi"])
        diet = float(request.form["diet"])

        # Prepare features
        features = np.array([[age, income, exercise, bmi, diet]])
        features_scaled = scaler.transform(features)

        # Prediction
        prediction = model.predict(features_scaled)[0]
        result = "Will Buy Subscription" if prediction == 1 else "Will Not Buy Subscription"

        return render_template("result.html", prediction_text=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
