import json

# Open the JSON file
with open("supercomplex.json", "r") as json_file:
    # Read the JSON data
    json_data = json.load(json_file)

# Extract the users data
users_data = json_data["users"]

# Create a list to store the names of the software engineers
software_engineer_names = []

# Iterate over the users data
for user_data in users_data:
    # Extract the user's occupation
    user_occupation = user_data["occupation"]

    # If the user is a software engineer, add their name to the list
    if user_occupation == "Software Engineer":
        software_engineer_names.append(user_data["name"])

# Print the names of the software engineers
print("Software Engineer Names:")
for software_engineer_name in software_engineer_names:
    print(f"- {software_engineer_name}")
