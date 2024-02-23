import requests

import pandas as pd

api_key = 'AIzaSyAJ-57ihz0fENb-TEZF4wWCmKQtSCUdy9w'

df = pd.read_csv('routes.csv')



airport_code = 'JFK'  # example airport code
query = f'{airport_code} airport'

url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}'


response = requests.get(url)
data = response.json()

# Assuming the first result is the airport, extract its location
print(data)
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']

print(f'Latitude: {latitude}, Longitude: {longitude}')

# Append data to routes.csv

