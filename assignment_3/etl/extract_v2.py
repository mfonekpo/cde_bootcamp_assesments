import subprocess

subprocess.run("mkdir -p ./new_data", shell=True, check=True)

subprocess.run("wget -O ./new_data/survey_data.csv https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv", shell=True, check=True)