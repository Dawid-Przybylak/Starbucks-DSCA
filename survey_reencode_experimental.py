from helpers import read_from_csv, save_to_csv
from data_loading_pipeline import load_all_data
import pandas as pd

raw, cleaned = load_all_data()

# Rename column if present
if 'itempurchaseCold' in cleaned.columns:
    cleaned = cleaned.rename(columns={'itempurchaseCold': 'itemPurchaseCold'})

# List of purchase columns
purchase_cols = [
    'itemPurchaseCoffee',
    'itemPurchaseCold',
    'itemPurchasePastries',
    'itemPurchaseJuices',
    'itemPurchaseSandwiches',
    'itemPurchaseOthers'
]

# Set all purchase columns to 0
for col in purchase_cols:
    if col in cleaned.columns:
        cleaned[col] = 0

# Derive purchase info from the survey response column
purchase_map = {
    'Coffee': 'itemPurchaseCoffee',
    'Cold drinks': 'itemPurchaseCold',
    'Pastries': 'itemPurchasePastries',
    'Juices': 'itemPurchaseJuices',
    'Sandwiches': 'itemPurchaseSandwiches',
    'Others': 'itemPurchaseOthers'
}

# Find the column with the question text (case-insensitive, strip whitespace)
purchase_col = None
for col in cleaned.columns:
    if 'most frequently purchase' in col.lower():
        purchase_col = col
        break

if purchase_col:
    for key, target_col in purchase_map.items():
        mask = cleaned[purchase_col].astype(str).str.contains(key, case=False, na=False)
        cleaned.loc[mask, target_col] = 1

save_to_csv(cleaned, "mod_survey_data.csv")