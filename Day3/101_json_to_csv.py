import json
import csv

# Open the JSON file
with open("sample.json", "r") as json_file:
    # Read the JSON data
    json_data = json.load(json_file)

# Create a CSV file
with open("output.csv", "w", newline="") as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["name", "age", "occupation"])

    # Write the data row
    writer.writerow([json_data["name"], json_data["age"], json_data["occupation"]])
