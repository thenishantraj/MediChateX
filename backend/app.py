from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pickle
import os

# Initialize the Flask app and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'  # SQLite database for storing patient info
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Patient model for the database
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    symptoms = db.Column(db.String(200), nullable=False)
    medications = db.Column(db.String(100), nullable=True)

# Load the trained model and label encoder
model = pickle.load(open('medicine_model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

@app.route('/add_patient', methods=['POST'])
def add_patient():
    # Extract patient data from the request
    data = request.get_json()
    age = data['age']
    gender = data['gender']
    symptoms = data['symptoms']
    
    # Create a new patient instance
    patient = Patient(age=age, gender=gender, symptoms=symptoms)
    
    # Add the patient to the database
    db.session.add(patient)
    db.session.commit()
    
    return jsonify({'message': 'Patient added successfully'}), 201

@app.route('/train_model', methods=['POST'])
def train_model():
    # This endpoint triggers the training of the model (not implemented here)
    # You can call your training script and save the model
    
    # For now, assume model training happens here
    return jsonify({'message': 'Model training triggered'}), 200

@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    # Extract patient data from the request for prediction
    data = request.get_json()
    age = data['age']
    gender = data['gender']
    symptoms = data['symptoms']
    
    # Preprocess symptoms and make predictions
    processed_input = [symptoms]  # Use appropriate preprocessing here
    predicted_medication = model.predict(processed_input)
    
    # Decode the prediction
    medication = label_encoder.inverse_transform(predicted_medication)
    
    # Return the predicted medication
    return jsonify({'recommended_medication': medication[0]}), 200

if __name__ == '__main__':
    # Initialize the database (if needed)
    with app.app_context():
        db.create_all()
    
    # Run the Flask app
    app.run(debug=True)
