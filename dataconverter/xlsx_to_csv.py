import pandas as pd
import os

# Load the Excel file
excel_file_path = './drug_recipe_comp_1720169090.xlsx'
excel_data = pd.read_excel(excel_file_path, sheet_name=None)  # Read all sheets

# Directory to save CSV files
csv_directory = './'

# Create the directory if it doesn't exist
if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)

# Save each sheet as a separate CSV file
for sheet_name, data in excel_data.items():
    csv_file_path = os.path.join(csv_directory, f'{sheet_name}.csv')
    data.to_csv(csv_file_path, index=False)

print("Conversion completed successfully!")
