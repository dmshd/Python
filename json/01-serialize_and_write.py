import json

# a simple serialization example

data = {
  "food": {
    "appel": "Granny Smith",
    "pear": "Conférence"
  }
}

with open("data_file.json", "w") as write_file:
  json.dump(data, write_file)

