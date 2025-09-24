import pandas as pd

def transform_data(df):
    print("Transforming data...")
    # Clean age (convert to int, handle invalid)
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)
    # Uppercase name
    df['name'] = df['name'].str.upper()
    # Dummy email validation (just uppercase domain for demo)
    df['email'] = df['email'].str.lower()
    print("Transformed data:\n", df)
    return df