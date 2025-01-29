# Medicine App Backend

This is the backend for the Medicine Recommendation App, built with Flask. It includes the following features:

- **Add Patient**: Allows adding patient data to the database.
- **Train Model**: Triggers the model training process (this can be extended to include model training scripts).
- **Get Medication Recommendation**: Given patient symptoms and data, it provides medication recommendations using a trained machine learning model.

### Setup and Running:

1. **Install Dependencies**:
   - Ensure you have Python 3.7+ installed.
   - Install the necessary Python dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Initialize Database**:
   - Run the Flask app with the following command:
     ```bash
     python app.py
     ```
   - The app will automatically create the `patients.db` SQLite database.

3. **Endpoints**:
   - `/add_patient`: `POST` request to add patient data (age, gender, symptoms).
   - `/train_model`: `POST` request to trigger model training.
   - `/get_recommendation`: `POST` request to get medication recommendation based on patient data.

4. **Running the App**:
   - To start the Flask app:
     ```bash
     python app.py
     ```

5. **Testing the API**:
   - Use Postman or cURL to send requests to the API.
   - Example `POST` request for adding a patient:
     ```json
     {
       "age": 45,
       "gender": "female",
       "symptoms": "fever, cough"
     }
     ```
   - Example `POST` request for getting a recommendation:
     ```json
     {
       "age": 45,
       "gender": "female",
       "symptoms": "fever, cough"
     }
     ```

### License:
This project is licensed under the MIT License.
