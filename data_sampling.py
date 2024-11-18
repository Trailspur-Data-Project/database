import pandas as pd

# Read the CSV file into a DataFrame (replace 'your_file.csv' with the actual file path)
df = pd.read_csv('cleaned_DFW_properties.csv')

# Sample 50 random rows from the DataFrame
sample_df = df.sample(n=50, random_state=1)

# Optionally, save the sampled data to a new CSV file
sample_df.to_csv('sampled_data.csv', index=False)

# Display the sampled data
print(sample_df.head())
