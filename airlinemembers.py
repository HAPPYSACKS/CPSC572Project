import json
from typing import Dict
import pandas as pd


data_sheet = 'routes.csv'
airlines_path = 'airlines.json'


codeToAirline: Dict[str, str] = {}
airlineToAlliance: Dict[str, str] = {}

with open(airlines_path, 'r') as airlineFile:
    codeToAirline = json.load(airlineFile)

with open(airlines_path, 'r') as allianceFile:
    airlineToAlliance = json.load(allianceFile)

df = pd.read_csv(data_sheet)


for airlineCode in df['airline']:
    airline = codeToAirline[airlineCode]
    alliance = airlineToAlliance[airline]

    


