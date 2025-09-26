import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def load_data_to_db(data: pd.DataFrame):
    conn_params = {"dbname":os.getenv("POSTGRES_DB"),
    "user":os.getenv("POSTGRES_USER"),
    "password":os.getenv("POSTGRES_PASSWORD"),
    "host":"localhost",
    "port":"5432"}

    try:
        with psycopg2.connect(**conn_params) as conn:
            print("Connected to the database successfully.")
            # create a table
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS survey (
                        id SERIAL PRIMARY KEY,
                        survey_year INTEGER,
                        survey_value INTEGER,
                        units VARCHAR(100),
                        variable_code VARCHAR(20)
                    );
                    """)
            print("Table 'survey' created successfully.")

            # insert data into table
            with conn.cursor() as cur:

                rows = data.to_records(index=False).tolist()
                insert_query = """
                    INSERT INTO survey (survey_year, survey_value, units, variable_code)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (survey_year, variable_code) DO NOTHING;
                """
                cur.executemany(insert_query, rows)
            print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")