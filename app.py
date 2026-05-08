from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load your trained machine learning model
# Uncomment the line below and ensure 'model.pkl' is in the same directory
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the 13 features based on the UCI dataset format
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]
        
        final_features = [np.array(features)]
        
        # prediction = model.predict(final_features)
        
        # Placeholder prediction (remove once model is loaded)
        prediction = [1] 
        
        if prediction[0] == 1:
            result = "Disease Present (High Risk)" 
        else:
            result = "No Disease (Low Risk)"
            
        return render_template('index.html', prediction_text=result)
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error processing input: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)