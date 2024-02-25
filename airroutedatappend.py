import requests
from typing import Dict
import pandas as pd

api_key = 'AIzaSyAJ-57ihz0fENb-TEZF4wWCmKQtSCUdy9w'

df = pd.read_csv('updated_routes.csv')

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
        print("error something went wrong.")
        return None

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
        return None



airport_code = 'JFK'  # example airport code
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
    break
print(airportPosition)






# Assuming the first result is the airport, extract its location





# Append data to routes.csv

