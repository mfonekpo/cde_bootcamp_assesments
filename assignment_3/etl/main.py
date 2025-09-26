from extract import extract_file
from transform import transform_data
from load import load_data_to_db
import pandas as pd
# from pathlib import Path



def main(data_path: str = "./Transformed/2023_year_finance.csv"):
    extract_file()
    transform_data()
    data = pd.read_csv(data_path)
    load_data_to_db(data)

if __name__ == "__main__":
    main()

