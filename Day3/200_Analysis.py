import json

# Open the JSON file
with open("200_output.json", "r") as json_file:
    # Read the JSON data
    json_data = json.load(json_file)

# Print type from json_data
print(json_data["data"]["type"])

def extract_whois_info(data):
    return data["data"]["attributes"]["whois"]

def extract_geographical_info(data):
    attributes = data["data"]["attributes"]
    return {
        "Country": attributes["country"],
        "Continent": attributes["continent"],
        "Regional Internet Registry": attributes["regional_internet_registry"]
    }

def analyze_reputation(data):
    reputation = data["data"]["attributes"]["reputation"]
    if reputation == 0:
        return "Neutral or Unknown"
    elif reputation > 0:
        return "Likely Safe"
    else:
        return "Likely Malicious"


print(extract_whois_info(json_data))
print(extract_geographical_info(json_data))
print(analyze_reputation(json_data))