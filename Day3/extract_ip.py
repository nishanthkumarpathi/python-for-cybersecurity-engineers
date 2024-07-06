import re

# Define a function to extract IP addresses from a log file
def extract_ips_from_log(log_file_path):
    # Open the log file and read its content
    with open(log_file_path, 'r') as file:
        log_data = file.read()

    # Use a regular expression to find all IP addresses in the log data
    ip_addresses = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', log_data)

    # Return the list of extracted IP addresses
    return ip_addresses

# Call the function and print the extracted IP addresses
ips = extract_ips_from_log('ip_log.txt')
print("Extracted IP Addresses:")
for ip in ips:
    print(ip)

# COunt each ip from the ip_addresses array and print the count
ip_count = {}
for ip in ips:
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

print("\nIP Counts:")