import pandas as pd
import numpy as np

def csv_to_array(file_path):
    df = pd.read_csv(file_path)
    # Replace NaN values with None
    df = df.where(pd.notnull(df), None)
    # Convert DataFrame to list of dictionaries
    array_of_objects = df.to_dict(orient='records')
    return array_of_objects

file_path = './medicines.csv'
array_of_objects = csv_to_array(file_path)

for obj in array_of_objects:
    print(obj)

