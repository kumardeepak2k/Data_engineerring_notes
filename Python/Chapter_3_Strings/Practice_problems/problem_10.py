# Input list of strings
input_list = [
    "/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/",
    "/server/192.168.1.1/config/file",
    "/usr/local/10.168.155.2/data/file",
    "/home/user/192.168.1.1/logs/data"
]

# Set to store unique IP addresses
unique_ips = set()

# Loop through each string in the list
for path in input_list:
    # Split the string by '/' to isolate potential IP addresses
    segments = path.split('/')
    
    # Loop through each segment
    for segment in segments:
        # Check if the segment has 4 parts when split by '.'
        parts = segment.split('.')
        
        # Check if there are exactly 4 parts and each part is a valid number (0-255)
        if len(parts) == 4:
            is_valid = True
            for part in parts:
                if not part.isdigit():  # Check if part is a number
                    is_valid = False
                    break
                num = int(part)
                if num < 0 or num > 255:  # Check if number is within valid range
                    is_valid = False
                    break

            # If the segment is a valid IP, add it to the set
            if is_valid:
                unique_ips.add(segment)

# Print the unique IP addresses
print(list(unique_ips))
