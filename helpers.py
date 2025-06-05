from config import output_path, data_path
import os
import pandas as pd

def save_to_csv (df, filename, folder_path=output_path):
    path = os.path.join(folder_path, filename)
    df.to_csv(path, index=False)
    print(f"{path} saved")

def read_from_csv (filename, folder_path=data_path):
    file_path = os.path.join(folder_path, filename)
    object = pd.read_csv(file_path)
    return object