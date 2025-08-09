## Logistic Regression Project – Diabetes Prediction
### 📌 Overview
This project implements a Logistic Regression model to predict whether a person is likely to have diabetes based on medical diagnostic measurements.
It uses scikit-learn for model training and a simple Flask web application to allow user input and real-time predictions.

___

### 📂 Project Structure

DataScience/
│
├── Logistic Regression/
│   ├── dataset/
│   │   └── fitness-subscription-prediction.csv
│   ├── model/
│   │   └── logistic_model.pkl
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── model.py
│   ├── app.py
│   ├── requirements.txt
│   └── README.md

___

## ⚙️ Installation & Setup
**1️⃣ Clone the repository**

git clone <your-repo-url>
cd "DataScience/Logistic Regression"

**2️⃣ Create a virtual environment (recommended)**

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

**3️⃣ Install dependencies**

pip install -r requirements.txt

**📊 Dataset**
**The dataset includes:**

- Age (int)
- Gender (Male/Female)
- Annual Income (USD) (float)
- BMI (float)
- Workout Frequency (days/week) (int)
- Subscription Duration (months) (int)
- Membership Type (Basic/Standard/Premium)
- Renewed (Target: 0 = No, 1 = Yes)
- 

**🚀 How to Run**
**1️⃣ Train the Model**

python model.py
This will create a trained logistic_model.pkl file inside the model/ folder.

**2️⃣ Run the Flask App**

python app.py
Visit http://127.0.0.1:5000/ in your browser.


📌 Future Scope
🔹 Deploy the model on Heroku or Render for public access.

🔹 Improve accuracy by hyperparameter tuning and testing different algorithms.

🔹 Add data visualization dashboard using Plotly or Matplotlib.

🔹 Implement real-time data collection from wearable health devices.

🔹 Create a REST API for integration with other applications.

🔹 Enhance UI/UX for better accessibility and user interaction.

📜 License
This project is licensed under the MIT License.

## Screenshots

### Input 1
<img width="1920" height="1080" alt="Home 1" src="https://github.com/user-attachments/assets/9a6f913e-c46b-43b7-9c79-b1ba7d5de0b1" />

<img width="1920" height="1080" alt="Result 1" src="https://github.com/user-attachments/assets/da59db8a-dcc8-40f2-8013-c00ea0cbe758" />



### Input 2
<img width="1920" height="1080" alt="Home 2" src="https://github.com/user-attachments/assets/bbcc406b-7de0-461f-acb5-ced848a842bc" />
<img width="1920" height="1080" alt="Result 2" src="https://github.com/user-attachments/assets/9bdd3fa1-e389-4f5f-a640-f3d9915200b3" />

