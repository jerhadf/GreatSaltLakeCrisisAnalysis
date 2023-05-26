import json 

def remove_empty_strings(d):
    return {k: v for k, v in d.items() if v != ""}

# Load JSON data
with open('data/links.json', 'r') as f:
    data = json.load(f)

# Remove empty strings
data = remove_empty_strings(data)

# Save the cleaned JSON data
with open('data/links.json', 'w') as f:
    json.dump(data, f)