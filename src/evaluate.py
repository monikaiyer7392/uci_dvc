import json
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

# Load test data (optional: split original dataset)
df = pd.read_excel('data/default of credit card clients.xls', header=1)
X = df.drop('default payment next month', axis=1)
y = df['default payment next month']

# Load model
model = joblib.load('models/model.pkl')

# Evaluate
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)

# Write metrics
metrics = {"accuracy": accuracy}
with open('metrics.json', 'w') as f:
    json.dump(metrics, f)