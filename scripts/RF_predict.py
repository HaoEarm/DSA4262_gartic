import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

import joblib
import sys
import os

# Loading the pretrained Random Forest Model
dirname = os.path.dirname(__file__) # Path to this predict.py
filename = os.path.join(dirname, '../model/Random_Forest_v2.joblib') # Relative path to model folder
rf = joblib.load(filename)

# Loading scaler used from training
filename2 = os.path.join(dirname, '../model/scaler.joblib') # Relative path to model folder
scaler = joblib.load(filename2)

# Reading in the parsed data
df = pd.read_csv('../Data/test_data_updated.csv') # Edit File name to relevant csv file

# Drop features that are not needed / redundant
X = df.drop(columns=['label','gene_id','transcript_id','Key','ENST_ID'])

# Scale new input data
X_scaled = scaler.transform(X)

# Run model predictions
test_probabilities = rf.predict_proba(X_scaled)[:, 1]

# Create output submission file in required format
# transcript_id, transcript_position, score
output = df[['transcript_id', 'transcript_position']]

# Add in prediction scores as 'score' column
output['score'] = pd.Series(test_probabilities)

# Saving Final output file for submission
output.to_csv('../output/output.csv', index=False)

print("output scores have been generated, predict script has finished running.")
