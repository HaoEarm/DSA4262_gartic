import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

# Load your data
data = pd.read_csv('../Data/processed_data.csv')

# Features (X) and labels (y)
X = data.drop(columns=['label'])
y = data['label']
groups = data['gene_id']  # Use gene_id as groups

# Create GroupShuffleSplit instance
gss = GroupShuffleSplit(n_splits=1, train_size=0.7, test_size=0.3, random_state=42)

# Split into train and temporary sets (70% train, 30% temp)
for train_idx, temp_idx in gss.split(X, y, groups):
    X_train, X_temp = X.iloc[train_idx], X.iloc[temp_idx]
    y_train, y_temp = y.iloc[train_idx], y.iloc[temp_idx]
    groups_temp = groups.iloc[temp_idx]

# Further split the temporary set into validation and test sets (50% val, 50% test)
gss_val_test = GroupShuffleSplit(n_splits=1, train_size=0.5, test_size=0.5, random_state=42)

for val_idx, test_idx in gss_val_test.split(X_temp, y_temp, groups_temp):
    X_val, X_test = X_temp.iloc[val_idx], X_temp.iloc[test_idx]
    y_val, y_test = y_temp.iloc[val_idx], y_temp.iloc[test_idx]

# Combine features and labels back for exporting
train_data = pd.concat([X_train, y_train], axis=1)
val_data = pd.concat([X_val, y_val], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# Save to CSV
train_data.to_csv('../Data/train_data.csv', index=False)
val_data.to_csv('../Data/val_data.csv', index=False)
test_data.to_csv('../Data/test_data.csv', index=False)
