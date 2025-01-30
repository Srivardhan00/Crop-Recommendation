from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load the trained model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['Nitrogen in kg/ha'], data['Phosphorus in kg/ha'], data['Potassium in kg/ha'],
                data['temperature in C'], data['humidity'], data['ph'], data['rainfall in mm']]
    prediction = model.predict([features])
    return jsonify({'crop': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
