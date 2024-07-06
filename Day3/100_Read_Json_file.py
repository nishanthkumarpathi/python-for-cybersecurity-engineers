import json

# Open the JSON file
with open("sample.json", "r") as json_file:
    # Read the JSON data
    json_data = json.load(json_file)

# Print the JSON data
print(json.dumps(json_data, indent=4))

# Print the name and age of the person
print(f"Name: {json_data['name']}")
print(f"Age: {json_data['age']}")

