import pandas as pd
import yaml
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

# Load data
df = pd.read_excel('data/default of credit card clients.xls', header=1)
X = df.drop('default payment next month', axis=1)
y = df['default payment next month']

# Load params
with open('params.yaml') as f:
    params = yaml.safe_load(f)

model_type = 'random_forest'  # Change manually or via CLI

if model_type == 'random_forest':
    model = RandomForestClassifier(
        n_estimators=params['random_forest']['n_estimators'],
        max_depth=params['random_forest']['max_depth'],
        min_samples_split=params['random_forest']['min_samples_split']
    )
elif model_type == 'logistic_regression':
    model = LogisticRegression(
        C=params['logistic_regression']['C'],
        max_iter=params['logistic_regression']['max_iter']
    )
else:
    model = XGBClassifier(
        n_estimators=params['xgboost']['n_estimators'],
        learning_rate=params['xgboost']['learning_rate'],
        max_depth=params['xgboost']['max_depth'],
        subsample=params['xgboost']['subsample']
    )

model.fit(X, y)
joblib.dump(model, 'models/model.pkl')