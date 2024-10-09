import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('../Data/parsed_json.csv')
new_df = df.drop(columns=['ENST_ID', 'Position'])
new_df = new_df[['gene_id', 'transcript_id', 'transcript_position', 'Key', 'Values', 'label']]

#functions to help
def calculate_average(values):
    arr = np.array(values)
    return arr.mean(axis=0).tolist()

def convert_to_float(value):
        value = eval(value)
        return [[float(elem) for elem in inner] for inner in value]

#convert from str to float
new_df['Values'] = new_df['Values'].apply(convert_to_float)
#get the avg
new_df['Values'] = new_df['Values'].apply(calculate_average)

#split into individual columns
values_expanded = new_df['Values'].apply(pd.Series)
values_expanded.columns = [f'Value_{i+1}' for i in range(values_expanded.shape[1])]
clean_df = pd.concat([new_df, values_expanded], axis=1)

clean_df.drop(columns=['Values'], inplace=True)

# Shuffle the entire dataset
clean_df = clean_df.sample(frac=1, random_state=42).reset_index(drop=True)

#convert strings to numerical value
label_encoder = LabelEncoder()
clean_df['transcript_id_encoded'] = label_encoder.fit_transform(clean_df['transcript_id'])
clean_df['Key_encoded'] = label_encoder.fit_transform(clean_df['Key'])
clean_df['gene_id_encoded'] = label_encoder.fit_transform(clean_df['gene_id'])

clean_df = clean_df.drop(columns='label').join(clean_df['label'])

#convert to csv
clean_df.to_csv('../Data/processed_data.csv', index=False)
