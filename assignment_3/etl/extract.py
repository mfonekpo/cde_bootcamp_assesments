import pandas as pd

def extract_data(file_path):
    print("Extracting data from:", file_path)
    df = pd.read_csv(file_path)
    print("Extracted data:\n", df)
    return df