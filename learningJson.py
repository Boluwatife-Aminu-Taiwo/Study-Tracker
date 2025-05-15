import json

# Python dict
data = {
    "name": "Gamma",
    "level": "final year",
    "courses": ["Python", "Reservoir Engineering"],
    "hours_studied": 15
}

# Save to file
with open("study.json", "w") as f:
    json.dump(data, f, indent=4)

# Load from file
with open("study.json", "r") as f:
    loaded = json.load(f)

print(loaded["courses"])  # → Gamma
