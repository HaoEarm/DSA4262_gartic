import pandas as pd
from sklearn.model_selection import train_test_split

# Load your data
data = pd.read_csv('data/parsed_json.csv')

# Features (X) and labels (y)
X = data.drop(columns=['label'])
y = data['label']

# Shuffle the entire dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Split into train and temporary sets (70% train, 30% temp)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)

# Now split the temporary set into validation and test sets (50% val, 50% test)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Combine features and labels back for exporting
train_data = pd.concat([X_train, y_train], axis=1)
val_data = pd.concat([X_val, y_val], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# Save to CSV
train_data.to_csv('data/train_data.csv', index=False)
val_data.to_csv('data/val_data.csv', index=False)
test_data.to_csv('data/test_data.csv', index=False)
