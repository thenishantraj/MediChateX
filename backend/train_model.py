import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load your dataset here (Example dataset)
data = pd.read_csv('patient_data.csv')

# Assume dataset has columns: 'symptoms', 'medication'
X = data['symptoms']
y = data['medication']

# Encode the target labels (medications)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Model training (Random Forest Classifier as an example)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model and the label encoder
pickle.dump(model, open('medicine_model.pkl', 'wb'))
pickle.dump(label_encoder, open('label_encoder.pkl', 'wb'))

print("Model training complete and saved!")
