import json

# Open the JSON file
with open("supercomplex.json", "r") as json_file:
    # Read the JSON data
    json_data = json.load(json_file)

# Extract the users data
users_data = json_data["users"]

# Iterate over the users data
for user_data in users_data:
    # Extract the user's name
    user_name = user_data["name"]

    # Extract the user's age
    user_age = user_data["age"]

    # Extract the user's occupation
    user_occupation = user_data["occupation"]

    # Print the user's information
    print(f"User Name: {user_name}")
    print(f"User Age: {user_age}")
    print(f"User Occupation: {user_occupation}")

    # Extract the user's skills
    user_skills = user_data["skills"]

    # Print the user's skills
    print("User Skills:")
    for user_skill in user_skills:
        print(f"- {user_skill}")
