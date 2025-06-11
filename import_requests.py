import requests
import json

# Fetch the file
response = requests.get('https://raw.githubusercontent.com/JPCodeCraft/ao-bin-dumps/master/formatted/items.txt')

# Split the file into lines
lines = response.text.split('\n')

# Initialize an empty dictionary to hold the mappings
mappings = {}

# Iterate over the lines
for line in lines:
    # Split the line into parts
    parts = line.split(':')
    # If the line has at least 3 parts and the third part is not empty
    if len(parts) >= 3 and parts[2].strip():
        # The key is the second part, stripped of leading/trailing whitespace
        key = parts[1].strip()
        # The value is the third part, stripped of leading/trailing whitespace
        value = parts[2].strip()
        # Add the mapping to the dictionary
        mappings[key] = value

# Write the mappings to a JSON file
with open('us_name_mappings.json', 'w') as f:
    json.dump(mappings, f)