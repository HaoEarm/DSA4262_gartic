# Importing Libraries
import pandas as pd
import numpy as np
import ast

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score
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

# Drop features that are not needed / redundant
# Split into X and y (Features and Label)
X_train = train_data.drop(columns=['label','gene_id','transcript_id','Key','gene_id_encoded'])
y_train = train_data['label']

X_val = val_data.drop(columns=['label','gene_id','transcript_id','Key','gene_id_encoded'])
y_val = val_data['label']

X_test = test_data.drop(columns=['label','gene_id','transcript_id','Key','gene_id_encoded'])
y_test = test_data['label']

# Addressing class imbalance in the Dataset using SMOTE + class weight + scale
# More Positive cases than Negative Cases

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

# Begin Training the Model
rf = RandomForestClassifier(class_weight='balanced')
rf.fit(X_train_resampled, y_train_resampled)
print("Random Forest Model has finished training")

# Running on validation data
val_predictions = rf.predict(X_val_scaled)
val_probabilities = rf.predict_proba(X_val_scaled)[:, 1]
val_accuracy = accuracy_score(y_val, val_predictions)
val_roc_auc = roc_auc_score(y_val, val_probabilities)

print(f'Validation ROC AUC Score: {val_roc_auc:.2f}')
print(f'Validation Accuracy Score: {val_accuracy:.2f}')

# Running on test data
test_predictions = rf.predict(X_test_scaled)
test_probabilities = rf.predict_proba(X_test_scaled)[:, 1]
test_accuracy = accuracy_score(y_test, test_predictions)
test_roc_auc = roc_auc_score(y_test, test_probabilities)

print(f"Test ROC AUC: {test_roc_auc:.2f}")
print(f"Test Accuracy: {test_accuracy:.2f}")

# Saving the trained Model
dirname = os.path.dirname(__file__) # Path to this train.py
filename = os.path.join(dirname, '../model/random_forest.joblib') # Relative path to model folder
joblib.dump(rf, filename, compress=9)

# Saving Standard Scaler for future Predictions
filename2 = os.path.join(dirname, '../model/scaler.joblib') # Relative path to model folder
joblib.dump(scaler, filename2)

print("Random Forest Model has been saved, training script has finished running.")
