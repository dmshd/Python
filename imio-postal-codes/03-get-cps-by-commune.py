#!/usr/bin/env python3

"""
I found that for Charleroi, using 01-get_gestomers_postal_codes.py only
returns 6000 but it's not correct since there's a lot more cps for charleroi
Let's extract all the data via another geoservices endpoint.

How to use (example):

python3 03-get-cps-by-commune.py arlon

"""

#  http://geoservices.wallonie.be/geolocalisation/rest/getListeLocalites/

import json
import requests
import sys

response = requests.get('http://geoservices.wallonie.be/geolocalisation/rest/getListeLocalites/')
response = response.json()
response_backup = json.dumps(response, indent=4)
#  I'm saving a copy preventing the API goes private
fhand = open('localites.json', 'w')
fhand.write(response_backup)
fhand.close()

localites = response.get('localites')


#  print(localites)

cps = []
#  print(dir(cps))
prcity = sys.argv[1].upper()

for element in localites:
    if element.get('commune') == prcity:
        cps.append(element.get('cps'))

print(cps)
# result with arlon and charleroi
"""
imac2020@iMac imio-postal-codes % python3 03-get-cps-by-commune.py arlon
[[6704], [6700], [6700], [6700], [6700], [6700], [6700], [6700], [6700], [6700],
[6700], [6706], [6706], [6700], [6700], [6706], [6700]]
imac2020@iMac imio-postal-codes % python3 03-get-cps-by-commune.py charleroi
[[6030], [6001], [6031], [6061], [6000], [6010], [6020], [6060], [6041], [6030],
[6040], [6042], [6032], [6043], [6044]]
"""
