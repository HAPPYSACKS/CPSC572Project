import pandas as pd

# Script that's used to calculate how many columns of Flight Alliance have `no entry`. For sanity checking purposes

updated_routes_path = 'updated_routes.csv'  
updated_df = pd.read_csv(updated_routes_path)

total_rows = len(updated_df)
no_entry_count = updated_df['Flight Alliance'].isna().sum()
no_entry_percentage = (no_entry_count / total_rows) * 100

print(f"Percentage of 'Flight Alliance' column with no entry: {no_entry_percentage:.2f}%")
