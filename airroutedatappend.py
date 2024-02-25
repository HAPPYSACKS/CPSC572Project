import os
import requests
from typing import Dict
import pandas as pd
import json

api_key = 'AIzaSyAJ-57ihz0fENb-TEZF4wWCmKQtSCUdy9w'

df = pd.read_csv('updated_routes.csv', dtype={'Flight Alliance': str})

def getPosition(airport_code: str, api_key: str):
    query = f'{airport_code} airport'
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}'


    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        return (latitude, longitude)
    else:
        error_status = data.get('status', 'UNKNOWN STATUS')
        error_message = data.get('error_message', 'No additional error message provided.')
        print(f"Error: Something went wrong. Status: {error_status}, Message: {error_message}")
        return None, None

def getElevation(lat, lng, api_key):
    url = f"https://maps.googleapis.com/maps/api/elevation/json?locations={lat},{lng}&key={api_key}"

    if not (lat and lng):
        return None

    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        elevation = data['results'][0]['elevation']
        return elevation
    else:
        error_status = data.get('status', 'UNKNOWN STATUS')
        error_message = data.get('error_message', 'No additional error message provided.')
        print(f"Error: Something went wrong. Status: {error_status}, Message: {error_message}")
        return None

airport_position_path = 'airportPosition.json'

if os.path.exists(airport_position_path) and os.path.getsize(airport_position_path) > 0:
    with open(airport_position_path, 'r') as json_file:
        airportPosition = json.load(json_file)
else:


    airportPosition = {} # dictionary that takes (airport_code) -> (lat, lng, elevation)
    airport_codes = set()

for airport_code in df[' source airport']:
    airport_codes.add(airport_code)
for airport_code in df[' destination apirport']:
    airport_codes.add(airport_code)



for airport_code in airport_codes:

    pos = getPosition(airport_code,api_key)
    lat = pos[0] 
    lng = pos[1]

    elevation = getElevation(lat, lng, api_key)
    airportPosition[airport_code] = (lat, lng, elevation)

# iterate through rows and map lat, lng, and elevation

with open(airport_position_path, 'w') as json_file:
    json.dump(airportPosition, json_file, indent=4)


latitudes_source = []
longitudes_source = []
elevations_source = []

latitudes_dest = []
longitudes_dest = []
elevations_dest = []

# first for src airport

for airport_code in df[' source airport']:
    lat_source, lng_source, elev_source = airportPosition[airport_code]
    latitudes_source.append(lat_source)
    longitudes_source.append(lng_source)
    elevations_source.append(elev_source)

# then for dest airport

for airport_code in df[' destination apirport']:
    lat_dest, lng_dest, elev_dest = airportPosition[airport_code]
    latitudes_dest.append(lat_dest)
    longitudes_dest.append(lng_dest)
    elevations_dest.append(elev_dest)

df['lat_src'] = latitudes_source
df['lng_src'] = longitudes_source
df['elevation_src'] = elevations_source

df['lat_dest'] = latitudes_dest
df['lng_dest'] = longitudes_dest
df['elevation_dest'] = elevations_dest

# Assuming the first result is the airport, extract its location




# Append data to routes.csv

