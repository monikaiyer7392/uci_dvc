
# 🚀 Machine Learning Experiment Tracking using DVC  
**Project:** Credit Card Default Prediction

## 📌 Overview
This project demonstrates an end-to-end **Machine Learning Experiment Tracking Pipeline** using **DVC (Data Version Control)**, structured with a Python Virtual Environment.

We use the **UCI Credit Card Default Dataset** to predict whether a customer will default on their credit card payment.  
The entire ML workflow, including dataset versioning, model training, evaluation, metrics logging, hyperparameter tuning, and experiment comparison, is automated using DVC.

## 📂 Project Structure
```
uci_dvc/
├── data/
│   └── default of credit card clients.xls
├── models/
│   └── model.pkl
├── src/
│   ├── train.py
│   └── evaluate.py
├── plots/
│   └── accuracy.csv (optional)
├── params.yaml
├── metrics.json
├── dvc.yaml
├── dvc.lock
├── requirements.txt
├── venv/
└── README.md
```

## 🔥 Features
✅ Dataset Versioning using DVC  
✅ Model Tracking  
✅ Hyperparameter Tuning using `params.yaml`  
✅ Metrics Logging & Visualization  
✅ Experiment Comparison  
✅ CI/CD Ready  
✅ Fully Windows + PowerShell Compatible

## 📝 Dataset
**UCI Credit Card Default Dataset**  
🔗 [Download Link](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)

## 🚀 Setup Instructions
### 1. Create Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.env\Scripts\Activate
```
**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Initialize DVC
```powershell
git init
dvc init
```

### 4. Add Dataset to DVC
```powershell
dvc add "data/default of credit card clients.xls"
git add "data/default of credit card clients.xls.dvc" .gitignore
git commit -m "Add dataset and DVC setup"
```

## ⚙️ DVC Pipeline
### 1. Define Hyperparameters in `params.yaml`
```yaml
logistic_regression:
  C: 1.0
  max_iter: 200

random_forest:
  n_estimators: 100
  max_depth: 10
  min_samples_split: 2

xgboost:
  n_estimators: 100
  learning_rate: 0.1
  max_depth: 6
  subsample: 0.8
```

### 2. Add DVC Pipeline Stages
**Train Stage:**
```powershell
dvc stage add -n train_model `
  -d src/train.py `
  -d "data/default of credit card clients.xls" `
  -p logistic_regression.C,logistic_regression.max_iter,random_forest.n_estimators,random_forest.max_depth,xgboost.n_estimators,xgboost.learning_rate `
  -o models/model.pkl `
  python src/train.py
```

**Evaluate Stage:**
```powershell
dvc stage add -n evaluate_model `
  -d src/evaluate.py `
  -d models/model.pkl `
  -M metrics.json `
  python src/evaluate.py
```
**Commit:**
```powershell
git add dvc.yaml dvc.lock
git commit -m "Add training & evaluation pipeline"
```

## 🚀 Running Experiments
### Run Default Pipeline
```powershell
dvc repro
```

### Run Hyperparameter Experiments
```powershell
dvc exp run -S random_forest.n_estimators=200
dvc exp run -S logistic_regression.C=0.5
dvc exp run -S xgboost.learning_rate=0.05
```

### Compare Experiments
```powershell
dvc exp show
```

### Show Evaluation Metrics
```powershell
dvc metrics show
```
