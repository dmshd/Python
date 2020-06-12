import json

with open("data_file.json", "r") as read_file:
  data = json.load(read_file)

print(data)

# {'food': {'appel': 'Granny Smith', 'pear': 'Conférence'}}

json_string = """
{
  "teachers": {
    "name": "Carole",
    "type": "Mathematics",
    "workdays_start": [
      {
      "monday": "8am",
      "friday": "2pm"
      }
    ]
  }
}
"""

data = json.loads(json_string)

print(data)

# {'teachers': {'name': 'Carole', 'type': 'Mathematics', 'workdays_start': [{'monday': '8am', 'friday': '2pm'}]}}