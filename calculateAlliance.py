import pandas as pd

# Load the updated routes CSV file
updated_routes_path = 'updated_routes.csv'  # Adjust this to the actual path of your file
updated_df = pd.read_csv(updated_routes_path)

# Calculate the total number of rows
total_rows = len(updated_df)

# Calculate the number of rows where 'Flight Alliance' has no entry
# If "no entry" means NaN or None
no_entry_count = updated_df['Flight Alliance'].isna().sum()

# Alternatively, if "no entry" means an empty string
# no_entry_count = (updated_df['Flight Alliance'] == "").sum()

# Calculate the percentage of rows with no entry in 'Flight Alliance'
no_entry_percentage = (no_entry_count / total_rows) * 100

print(f"Percentage of 'Flight Alliance' column with no entry: {no_entry_percentage:.2f}%")
