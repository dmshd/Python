#!/usr/bin/env python3

"""
I found that for Charleroi, using 01-get_gestomers_postal_codes.py only
returns 6000 but it's not correct since there's a lot more cps for charleroi
Let's extract all the data via another geoservices endpoint.
"""

# http://geoservices.wallonie.be/geolocalisation/rest/getListeLocalites/

import requests

response = requests.get('http://geoservices.wallonie.be/geolocalisation/rest/getListeLocalites/')

json = response.json()
localites = json.get('localites')

# print(localites)

for element in localites:
    print('commune:', element.get('commune'))
    print('nom:', element.get('nom'))
    print('cps:', element.get('cps'))
