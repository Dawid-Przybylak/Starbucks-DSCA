from helpers import read_from_csv
import os

def load_all_data():
    raw = read_from_csv(filename = "survey.csv")
    cleaned = read_from_csv(filename = "survey_encode_cleaned.csv")
    return raw, cleaned