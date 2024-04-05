import pandas as pd

# Script that finds any `Airline Name` that has `Unknown`.

updated_routes_path = 'updated_routes.csv'  
updated_df = pd.read_csv(updated_routes_path)


unknown_airlines_df = updated_df[updated_df['Airline Name'] == "Unknown"]


unknown_airlines_list = unknown_airlines_df['airline'].unique()

print("Airline Names marked as 'Unknown':", unknown_airlines_list)
