import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# MySQL connection details
user = 'root'
password = urllib.parse.quote_plus('Iph0ne@use')  # Handles '@'
host = 'localhost'
port = '3306'
database = 'vaccination_db'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

data_files = {
    'coverage_data': 'data/cleaned/coverage_data_cleaned.csv',
    'incidence_rate': 'data/cleaned/incidence_rate_data_cleaned.csv',
    'reported_cases': 'data/cleaned/reported_cases_data_cleaned.csv',
    'vaccine_intro': 'data/cleaned/vaccine_intro_data_cleaned.csv',
    'vaccine_schedule': 'data/cleaned/vaccine_schedule_data_cleaned.csv'
}

for table_name, csv_file in data_files.items():
    try:
        df = pd.read_csv(csv_file)
        # Ensure 'year' column exists and is integer (for MySQL YEAR type)
        if 'year' in df.columns:
            df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
        if 'Year' in df.columns:
            df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')
        # Additional: remove NaNs in year columns if needed
        # df = df[df['year'].notnull()]  # Uncomment if you want to drop rows with no year
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"{table_name} loaded successfully!")
    except Exception as e:
        print(f"Error loading {csv_file} into table {table_name}: {e}")

print("All cleaned tables loaded (or error messages above if any issue).")
