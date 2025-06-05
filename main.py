from data_loading_pipeline import load_all_data

# load the data
raw, cleaned = load_all_data()
print(raw.head())
print(cleaned.head())