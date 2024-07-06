with open("Linux_2k.log", "r") as original_file:
    with open("auth_failure_logs.txt", "w") as auth_failure_file:
        for line in original_file:
            if "authentication failure" in line:
                auth_failure_file.write(line)

# Close both files
original_file.close()
auth_failure_file.close()

# Sample Log Files
# https://github.com/logpai/loghub