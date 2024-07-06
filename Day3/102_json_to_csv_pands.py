import pandas as pd

# Read the JSON file
df = pd.read_json("sample.json")

# Convert the DataFrame to a CSV file
df.to_csv("output.csv", index=False)
