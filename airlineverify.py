import pandas as pd

# Load the updated routes CSV file
updated_routes_path = 'updated_routes.csv'  # Make sure to replace this with the actual path to your file
updated_df = pd.read_csv(updated_routes_path)

# Find rows where the 'Airline Name' is "Unknown"
unknown_airlines_df = updated_df[updated_df['Airline Name'] == "Unknown"]

# Get unique airline names marked as "Unknown"
unknown_airlines_list = unknown_airlines_df['airline'].unique()

print("Airline Names marked as 'Unknown':", unknown_airlines_list)
