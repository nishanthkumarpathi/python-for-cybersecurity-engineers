import requests

url = "https://www.virustotal.com/api/v3/ip_addresses/179.42.225.154"

headers = {
    "accept": "application/json",
    "x-apikey": ""
}

response = requests.get(url, headers=headers)

print(response.text)