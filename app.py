from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the trained model using joblib
model = joblib.load('model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        age = float(request.form.get('age'))
        anaemia = float(request.form.get('anaemia'))
        cpk = float(request.form.get('creatinine_phosphokinase'))
        diabetes = float(request.form.get('diabetes'))
        ef = float(request.form.get('ejection_fraction'))
        hbp = float(request.form.get('high_blood_pressure'))
        platelets = float(request.form.get('platelets'))
        sc = float(request.form.get('serum_creatinine'))
        ss = float(request.form.get('serum_sodium'))
        sex = float(request.form.get('sex'))
        smoking = float(request.form.get('smoking'))
        time = float(request.form.get('time'))

        # Make prediction
        features = np.array([[age, anaemia, cpk, diabetes, ef, hbp,
                              platelets, sc, ss, sex, smoking, time]])
        prediction = model.predict(features)
        result = "Patient is likely to die 💔" if prediction[0] == 1 else "Patient is likely to survive 💖"

        return render_template('index.html', prediction_text=result)
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
