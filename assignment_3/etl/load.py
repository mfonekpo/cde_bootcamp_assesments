import psycopg2
import os

def load_data(df, db_host, db_port, db_user, db_password, db_name):
    print("Loading data into database...")
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        dbname=db_name
    )
    cur = conn.cursor()
    
    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            age INTEGER,
            email TEXT
        )
    """)
    
    # Insert data
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
            (row['name'], row['age'], row['email'])
        )
    
    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded successfully!")