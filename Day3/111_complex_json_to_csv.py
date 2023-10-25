import json
import csv

# Open the JSON file
with open("supercomplex.json", "r") as json_file:
    # Read the JSON data
    json_data_org = json.load(json_file)

json_data = json_data_org["users"][0]

# Create a CSV file
with open("output.csv", "w", newline="") as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["name", "age", "occupation", "street", "city", "state", "zip", "mobile_number", "home_number", "skills"])

    # Write the data row
    writer.writerow([
        json_data["name"],
        json_data["age"],
        json_data["occupation"],
        json_data["address"]["street"],
        json_data["address"]["city"],
        json_data["address"]["state"],
        json_data["address"]["zip"],
        json_data["phone_numbers"][0]["number"],
        json_data["phone_numbers"][1]["number"],
        ", ".join(json_data["skills"])
    ])
