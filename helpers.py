from config import output_path, data_path
import os
import pandas as pd

def save_to_excel (df, filename):
    path = os.path.join(data_path, filename)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

def read_from_csv (filename):
    file_path = os.path.join(data_path, filename)
    object = pd.read_csv(file_path)
    return object