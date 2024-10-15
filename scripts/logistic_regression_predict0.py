import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
import joblib
import sys
import os

model = joblib.load('../model/LogisticRegression.joblib')
scaler = joblib.load('../model/LogisticRegression_scalar.joblib')

# Reading in the parsed data
df = pd.read_csv('../data/processed_data.csv')

# Drop features that are not needed / redundant
X = df.drop(columns=['label','gene_id','transcript_id','Key','gene_id_encoded'])

# Scale new input data
X_scaled = scaler.transform(X)

# Run model predictions
test_probabilities = model.predict_proba(X_scaled)[:, 1]

# Create output submission file in required format
# transcript_id, transcript_position, score
output = df[['transcript_id', 'transcript_position']]

# Add in prediction scores as 'score' column
output['score'] = pd.Series(test_probabilities)

# Saving Final output file for submission
output.to_csv('../output/LogisticRegression_predict0.csv', index=False)

