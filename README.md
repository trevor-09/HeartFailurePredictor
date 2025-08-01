# 🫀 Heart Failure Risk Predictor

This is a Flask-based web application that predicts the risk of heart failure based on clinical parameters. It uses a Random Forest classifier trained on real-world medical data.

---

## 🚀 Features

* Predicts risk of heart failure based on 12 medical inputs
* Shows probability-based risk level with an animated bar chart
* Clean, responsive UI with background image
* Retains input values after submission
* Fully deployed and accessible online

---

## 📦 Technologies Used

* Python 3.13
* Flask
* Scikit-learn (RandomForestClassifier)
* HTML/CSS + Jinja2
* Render (for deployment)

---

## 🌐 Live Demo

🔗 [View Deployed App on Render](https://heartfailurepredictor-s60w.onrender.com/)

---

## 🧪 Sample Inputs

You can test the app with the following values:

```plaintext
Age: 60
Anaemia: 0
CPK: 582
Diabetes: 1
Ejection Fraction: 38
High BP: 1
Platelets: 265000
Serum Creatinine: 1.2
Serum Sodium: 138
Sex: 1
Smoking: 0
Follow-up Time: 150
```

---

## 🛠 How to Run Locally

```bash
# Clone this repository
$ git clone https://github.com/your-username/HeartFailurePredictor.git
$ cd HeartFailurePredictor

# (Optional) Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python app.py
```

Then open your browser at `http://localhost:5000`

---

## 📁 Project Structure

```
HeartFailurePredictor/
├── app.py                  # Flask backend
├── model.pkl              # Trained ML model
├── model_training.py      # Model training script
├── session.log            # Request log
├── templates/
│   └── index.html         # Frontend page
├── static/
│   └── bg.jpg             # Background image
└── heart_failure_clinical_records_dataset.csv
```

---

## 👨‍⚕️ Dataset

The dataset used is from Kaggle, containing medical records of 299 patients with 13 clinical features.

---

## 📄 License

MIT License. Free to use and modify.

---
