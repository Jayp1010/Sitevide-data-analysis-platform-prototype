import pandas as pd
import sqlalchemy
from config import DATABASE_URI

def extract_data():
    # Extract data from various sources
    # Example with a CSV file:
    data = pd.read_csv('../data/raw/state_data.csv')
    return data

def transform_data(data):
    # Perform data transformations
    data['date'] = pd.to_datetime(data['date'])
    data = data.dropna()
    return data

def load_data(data):
    # Load data into a SQL database
    engine = sqlalchemy.create_engine(DATABASE_URI)
    data.to_sql('state_data', engine, if_exists='replace', index=False)

if __name__ == '__main__':
    raw_data = extract_data()
    processed_data = transform_data(raw_data)
    load_data(processed_data)

