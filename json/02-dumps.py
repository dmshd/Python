import json

data = {
  "animes": {
    "title": "final space",
    "duration": 20,
  }
}

json_string = json.dumps(data)

print(json_string)

# {"animes": {"title": "final space", "duration": 20}}

data2 = {
  "movies": {
    "starring": "Tom Hanks",
    "ratings": 4.5
  }
}

json_string = json.dumps(data2, indent=4)

print(json_string)

"""
{
    "movies": {
        "starring": "Tom Hanks",
        "ratings": 4.5
    }
}
"""

