from helpers import read_from_csv, save_to_csv
from data_loading_pipeline import load_all_data
import pandas as pd

pd.set_option('display.max_columns', None)  # Show all columns in DataFrame output

raw, cleaned = load_all_data()

# List of component columns as strings
component_cols = [str(i) for i in range(8)]

for col in component_cols:
    if col in cleaned.columns:
        q3 = cleaned[col].quantile(0.75)
        top_quartile = cleaned[cleaned[col] > q3]
        stats_df = top_quartile.describe(include="all")
        stats_filename = f"component_{col}_statistics.csv"
        save_to_csv(stats_df, stats_filename, folder_path=output_path)
