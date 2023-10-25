# Sample Log Files
# https://github.com/logpai/loghub

# Path to the original log file
original_log_file_path = "Linux_2k.log"

# Dictionary of condition names and output file paths
output_file_paths = {
    "authentication failure": "100_auth_failure_logs.txt",
    "session opened": "100_session_opened_logs.txt",
    "session closed": "100_session_closed_logs.txt",
    "ftpd": "100_ftpd_logs.txt",
}

# Open the original log file
with open(original_log_file_path, "r") as original_log_file:
    # Open all output files
    output_files = {}
    for condition_name, output_file_path in output_file_paths.items():
        output_files[condition_name] = open(output_file_path, "w")

    # Iterate through each line in the original log file
    for line in original_log_file:
        # Check the line against every condition
        for condition_name, output_file in output_files.items():
            if condition_name in line:
                output_file.write(line)

    # Close all output files
    for output_file in output_files.values():
        output_file.close()