#!/usr/bin/env python3

"""
I wanna get all cps of a city in my terminal
using http://geoservices.wallonie.be/geolocalisation/rest/searchLocalites/namur
(namur for example)
"""

import sys
import requests


url = 'http://geoservices.wallonie.be/geolocalisation/rest/searchLocalites/' + sys.argv[1]

response = requests.get(url)

# print(dir(response))
"""
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__',
'__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__',
'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__',
'__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding',
'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers',
'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines',
'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request',
'status_code', 'text', 'url']
"""

print(response.text)
"""
{"localites":[{"cps":[5000,5002,5004,5020],"nom":"NAMUR","commune":"NAMUR",
"xMin":182925.533299997,"xMax":187142.338699996,"yMin":125133.079700001,
"yMax":130759.7755,"errorCode":0,"errorMsg":null}],"errorCode":0,"errorMsg":null}
"""

json = response.json()

print(json.get('localites')[0].get('cps'))
