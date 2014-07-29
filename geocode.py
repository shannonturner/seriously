from geopy.geocoders import GoogleV3
import time

geolocator = GoogleV3()

with open('schools_zero.txt') as schools_file:
    schools = schools_file.read().strip().split('\n')

resources = []

for school in schools:
    print school
    time.sleep(1)
    try:
        address, (latitude, longitude) = geolocator.geocode(school)
    except:
        print "[ERR] FAILED TO GET LOCATION FOR ", school
    else:
        item = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    longitude,
                    latitude
                ]
            },
            "properties": {
                "marker-color": "#3F3040",
                "marker-symbol": "circle",
                "name": school[:-3],
                "address": address,
            }        
        }

        resources.append(item)

geo = {
  "type": "FeatureCollection",
  "features": resources
  }

import json

with open("schools_zero.json", 'w') as json_file:
    json_file.write(json.dumps(geo, indent=4, sort_keys=True))