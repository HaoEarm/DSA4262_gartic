# Importing Libraries
import pandas as pd
import numpy as np
import ast

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

import os
import joblib

# Reading in the parsed data
df = pd.read_csv('../Data/processed_data.csv')
train_data  = pd.read_csv('../Data/train_data.csv')
test_data  = pd.read_csv('../Data/test_data.csv')
val_data  = pd.read_csv('../Data/val_data.csv')

X_train = train_data.drop(columns=['label','gene_id','transcript_id','Key','gene_id_encoded'])
y_train = train_data['label']

X_val = val_data.drop(columns=['label','gene_id','transcript_id','Key','gene_id_encoded'])
y_val = val_data['label']

X_test = test_data.drop(columns=['label','gene_id','transcript_id','Key','gene_id_encoded'])
y_test = test_data['label']

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)
model4 = LogisticRegression(class_weight='balanced', max_iter=1000)
model4.fit(X_train_resampled, y_train_resampled)
print("LogisticRegression Model has finished training")

val_predictions = model4.predict(X_val_scaled)
val_probabilities = model4.predict_proba(X_val_scaled)[:, 1]
val_accuracy = accuracy_score(y_val, val_predictions)
val_roc_auc = roc_auc_score(y_val, val_probabilities)

print(f'Validation ROC AUC Score: {val_roc_auc:.2f}')
print(f'Validation Accuracy Score: {val_accuracy:.2f}')

test_predictions = model4.predict(X_test_scaled)
test_probabilities = model4.predict_proba(X_test_scaled)[:, 1]
test_accuracy = accuracy_score(y_test, test_predictions)
test_roc_auc = roc_auc_score(y_test, test_probabilities)

print(f'Test Accuracy: {test_accuracy:.2f}')
print(f'Test ROC AUC: {test_roc_auc:.2f}')

joblib.dump(model4, '../model/LogisticRegression.joblib', compress=9)
joblib.dump(scaler, '../model/LogisticRegression_scalar.joblib')