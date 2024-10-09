import pandas as pd
import json


# Load the JSON data
json_file_path = '../Data/dataset0.json'
data = []

with open(json_file_path, 'r') as json_file:
	for line in json_file:
        	if line.strip():  # Skip empty lines
            		data.append(json.loads(line))

# Prepare a list to store the flattened data
flattened_data = []

# Iterate through the loaded data
for entry in data:
	for enst_id, positions in entry.items():
        	for position, sub_dict in positions.items():
            		for key, values in sub_dict.items():
                	# Store the entire list of values as a string
                		row = {
                    			'ENST_ID': enst_id,
                    			'Position': position,
                    			'Key': key,
                    			'Values': str(values)  # Store the list as a string
                		}
                		flattened_data.append(row)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(flattened_data)

 #Save the DataFrame to a CSV file
csv_file_path = '../Data/output.csv'
df.to_csv(csv_file_path, index=False)

print(f"Data successfully saved to {csv_file_path}")

# Step 1: Read the CSV files
df1 = pd.read_csv('../Data/output.csv')
df2 = pd.read_csv('../Data/data_info_labelled.csv')

# Step 2: Merge the DataFrames
merged_df = pd.merge(
    df1,
    df2,
    left_on=['ENST_ID', 'Position'],  # Columns from df1
    right_on=['transcript_id', 'transcript_position'], # Columns from df2
    how='inner'
)
# Optional: View the merged DataFrame
print(merged_df)

# Step 3: Save the merged DataFrame to a new CSV file
merged_df.to_csv('../Data/parsed_json.csv', index=False)
