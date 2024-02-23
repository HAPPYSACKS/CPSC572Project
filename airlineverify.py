import pandas as pd


updated_routes_path = 'updated_routes.csv'  
updated_df = pd.read_csv(updated_routes_path)

# find rows where the 'Airline Name' is "Unknown"
unknown_airlines_df = updated_df[updated_df['Airline Name'] == "Unknown"]

# get unique airline names marked as "Unknown"
unknown_airlines_list = unknown_airlines_df['airline'].unique()

print("Airline Names marked as 'Unknown':", unknown_airlines_list)
