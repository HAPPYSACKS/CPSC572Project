import json
from typing import Dict
import pandas as pd


data_sheet = 'routes.csv'
airlines_path = 'airlines.json'
alliance_path = 'airlinetoalliance2012.json'

codeToAirline: Dict[str, str] = {}
airlineToAlliance: Dict[str, str] = {}

with open(airlines_path, 'r') as airlineFile:
    codeToAirline = json.load(airlineFile)

with open(alliance_path, 'r') as allianceFile:
    airlineToAlliance = json.load(allianceFile)

df = pd.read_csv(data_sheet)

airlines = []
alliances = []

for airlineCode in df['airline']:
    airline = codeToAirline.get(airlineCode, "Unknown")
    alliance = airlineToAlliance.get(airline, "None")
    airlines.append(airline)
    alliances.append(alliance)

df['Airline Name'] = airlines
df['Flight Alliance'] = alliances


df.to_csv('updated_routes.csv', index=False)



