import pandas as pd
from pathlib import Path


def rename_col(data: str) -> pd.DataFrame:
    """
    Reads a CSV file at the given path, renames its columns to match
    the database schema, and returns the resulting DataFrame.

    Args:
        data (str): The path of the CSV file to read.

    Returns:
        pd.DataFrame: The DataFrame with the renamed columns.
    """
    df = pd.read_csv(data)
    df.rename(
        columns={
            "Variable_code": "variable_code",
            "Value": "survey_value",
            "Year": "survey_year",
            "Units": "units"
        },
        inplace=True
    )
    return df


def save_selected_columns(
        data: str,
        output_path: str = "Transformed"
    ):

    """
    Saves a DataFrame with only the selected columns to a CSV file at the given output path.

    Args:
        data (str): The path of the CSV file to read.
        output_path (str): The path where the CSV file will be saved. Defaults to "Transformed".

    Returns:
        None
    """
    
    df = rename_col(data)
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / "2023_year_finance.csv"

    tr_data = df[["survey_year", "survey_value", "units", "variable_code"]]
    tr_data.to_csv(file_path, index=False)
    print("Column selection complete")


def transform_data():
    """
    Transforms the given DataFrame data by renaming columns and selecting specific columns.

    The given DataFrame data is read from a CSV file at the given data path, then
    the columns are renamed according to the given mapping, and then only the
    selected columns are saved to a CSV file at the given output path.

    Args:
        data_path (str): The path of the CSV file to read.

    Returns:
        None
    """
    data_path = Path("./data/survey_data.csv")
    rename_col(data_path)
    save_selected_columns(data_path)