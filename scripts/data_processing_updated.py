import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

new_df = pd.read_csv('data/parsed_json.csv')

# Functions to help
def calculate_statistics(values):
    arr = np.array(values)
    stats = {}
    
    # Calculate mean, median, min, max, std for each of the 3 columns (dwelling time, std dev, mean signal)
    stats['mean'] = np.mean(arr, axis=0).tolist()
    stats['median'] = np.median(arr, axis=0).tolist()
    stats['min'] = np.min(arr, axis=0).tolist()
    stats['max'] = np.max(arr, axis=0).tolist()
    stats['std'] = np.std(arr, axis=0).tolist()
    
    return stats

def convert_to_float(value):
    value = eval(value)
    return [[float(elem) for elem in inner] for inner in value]

# Convert from str to float
new_df['Values'] = new_df['Values'].apply(convert_to_float)

# Get the statistics for each transcript_id
new_df['Values'] = new_df['Values'].apply(calculate_statistics)

# Expand the statistics into individual columns
values_expanded = new_df['Values'].apply(pd.Series)

# Expand each statistical measure into its own set of columns
for stat in ['mean', 'median', 'min', 'max', 'std']:
    stat_expanded = pd.DataFrame(values_expanded[stat].to_list(), columns=[f'{stat}_Value_{i+1}' for i in range(9)])
    new_df = pd.concat([new_df, stat_expanded], axis=1)

# Drop the original 'Values' column since it's been expanded
new_df.drop(columns=['Values'], inplace=True)

# Shuffle the entire dataset
new_df = new_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Convert strings to numerical values
label_encoder = LabelEncoder()
new_df['transcript_id_encoded'] = label_encoder.fit_transform(new_df['transcript_id'])
new_df['Key_encoded'] = label_encoder.fit_transform(new_df['Key'])
# new_df['gene_id_encoded'] = label_encoder.fit_transform(new_df['gene_id'])

# Convert to CSV
new_df.to_csv('data/processed_data.csv', index=False)