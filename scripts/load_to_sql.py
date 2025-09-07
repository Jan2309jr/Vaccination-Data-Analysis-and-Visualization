import pandas as pd
import mysql.connector
import os

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iph0ne@use",  # change this
    database="vaccination_db"
)
cursor = conn.cursor()

# Function to load CSV into MySQL
def load_csv_to_sql(table_name, csv_path):
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return
    
    df = pd.read_csv(csv_path)
    print(f"Loading {csv_path} with shape {df.shape} into {table_name}")

    # Replace NaN with None for SQL
    df = df.where(pd.notnull(df), None)

    # Create placeholders and column string
    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Convert dataframe rows to list of tuples
    data = [tuple(row) for row in df.to_numpy()]

    # Execute batch insert
    cursor.executemany(sql, data)
    conn.commit()
    print(f"✅ Loaded {len(data)} rows into {table_name}")

# Correct CSV paths
load_csv_to_sql("CoverageData", "../data/cleaned/coverage_data_cleaned.csv")
load_csv_to_sql("IncidenceData", "../data/cleaned/incidence_rate_data_cleaned.csv")
load_csv_to_sql("ReportedCases", "../data/cleaned/reported_cases_data_cleaned.csv")
load_csv_to_sql("VaccineIntro", "../data/cleaned/vaccine_intro_data_cleaned.csv")
load_csv_to_sql("VaccineSchedule", "../data/cleaned/vaccine_schedule_data_cleaned.csv")

print("✅ All data loaded into MySQL database.")
cursor.close()
conn.close()
