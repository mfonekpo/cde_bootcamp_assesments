import requests
from pathlib import Path

def extract_file(
        url: str = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv",
        output_path: str = "data",
        filename: str = "survey_data.csv",
    ):

    """
    Downloads a file from the given URL and saves it to the given output path with the given filename.

    Args:
        url (str): The URL of the file to download. Defaults to "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv".
        output_path (str): The path where the file will be saved. Defaults to "data".
        filename (str): The name of the file to be saved. Defaults to "survey_data.csv".

    Returns:
        Path: The path of the saved file.
    """
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / filename

    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print("File extraction complete")
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
