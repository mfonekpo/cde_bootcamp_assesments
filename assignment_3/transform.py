import pandas as pd
import numpy as np
from pathlib import Path


def rename_col(data: str):
    df = pd.read_csv(data)
    df.rename(columns={"Variable_code": "variable_code"}, inplace=True)


def save_selected_columns(
        data: str,
        output_path: str = "Transformed"
    ):

    df = pd.read_csv(data)
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / "2023_year_finance.csv"

    tr_data = df[["Year", "Value", "Units", "variable_code"]]
    tr_data.to_csv(file_path, index=False)
    print("Column selection complete")


def transform_data():
    data_path = Path("data/survey_data.csv")
    rename_col(data_path)
    save_selected_columns(data_path)


def main():
    transform_data()
    print("Data transformation complete")


if __name__ == "__main__":
    main()