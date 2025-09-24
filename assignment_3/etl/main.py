import os
from extract import extract_data
from transform import transform_data
from load import load_data

# Get env vars (set by docker run)
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_USER = os.getenv('DB_USER', 'etl_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'etl_pass')
DB_NAME = os.getenv('DB_NAME', 'etl_db')

# Paths inside container
DATA_FILE = '/app/data/sample.csv'

# Run ETL
df = extract_data(DATA_FILE)
df_transformed = transform_data(df)
load_data(df_transformed, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)