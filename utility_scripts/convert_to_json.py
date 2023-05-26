import json

# Initialize the source
source = None
data = {}

# Read the links.txt file
with open("links.txt", "r") as file:
    for line in file:
        line = line.strip()  # Remove newline characters
        if line.startswith('# '):
            source = line[2:].lower()  # Remove '# ' and convert to lowercase
            data[source] = []  # Initialize a new list for this source
        else:
            data[source].append(line)  # Add the URL to the current source

# Write the data to a JSON file
with open("links.json", "w") as file:
    json.dump(data, file)
