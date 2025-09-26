import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def load_data_to_db(data: pd.DataFrame):
    """
    Loads the given DataFrame data into a PostgreSQL database table named 'survey'.

    Args:
        data (pd.DataFrame): The DataFrame data to be loaded into the database.

    Returns:
        None

    Raises:
        psycopg2.Error: If there is an error connecting to the database.
    """
    conn_params = {"dbname":os.getenv("POSTGRES_DB"),
    "user":os.getenv("POSTGRES_USER"),
    "password":os.getenv("POSTGRES_PASSWORD"),
    "host":"db",
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
                        survey_value VARCHAR,
                        units VARCHAR(100),
                        variable_code VARCHAR(20)
                    );
                    """)
            print("Table 'survey' created successfully.")

            # insert data into table
            with conn.cursor() as cur:
                # df = pd.read_csv(data)
                rows = data.to_records(index=False).tolist()
                insert_query = """
                    INSERT INTO survey (survey_year, survey_value, units, variable_code)
                    VALUES (%s, %s, %s, %s)
                """
                cur.executemany(insert_query, rows)
            print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")