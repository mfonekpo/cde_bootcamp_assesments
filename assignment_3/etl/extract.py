import requests
from pathlib import Path

def download_file(
        url: str = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv",
        output_path: str = "data",
        filename: str = "survey_data.csv",
    ):

    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / filename

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print("File extraction complete")

    return file_path

def main():
    download_file()

if __name__ == "__main__":
    main()
