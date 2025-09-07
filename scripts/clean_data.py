import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # scripts folder
RAW_PATH = os.path.join(BASE_DIR, "..", "data", "raw")
CLEANED_PATH = os.path.join(BASE_DIR, "..", "data", "cleaned")
os.makedirs(CLEANED_PATH, exist_ok=True)

def safe_convert_year(df):
    # Convert non-numeric year to NaN
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    # Drop rows where year is missing (optional) or fill with 0
    df = df.dropna(subset=['year'])  # safer than filling with 0
    df['year'] = df['year'].astype(int)
    return df

def clean_coverage():
    df = pd.read_excel(os.path.join(RAW_PATH, "coverage-data.xlsx"))
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    df['coverage'] = df['coverage'].fillna(0)
    df['target_number'] = df['target_number'].fillna(0)
    df['doses'] = df['doses'].fillna(0)
    
    df = safe_convert_year(df)
    
    df.to_csv(os.path.join(CLEANED_PATH, "coverage_data_cleaned.csv"), index=False)
    print("Coverage data cleaned and saved.")

def clean_incidence():
    df = pd.read_excel(os.path.join(RAW_PATH, "incidence-rate-data.xlsx"))
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    df['incidence_rate'] = df['incidence_rate'].fillna(0)
    df = safe_convert_year(df)
    
    df.to_csv(os.path.join(CLEANED_PATH, "incidence_rate_data_cleaned.csv"), index=False)
    print("Incidence rate data cleaned and saved.")

def clean_reported_cases():
    df = pd.read_excel(os.path.join(RAW_PATH, "reported-cases-data.xlsx"))
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    df['cases'] = df['cases'].fillna(0)
    df = safe_convert_year(df)
    
    df.to_csv(os.path.join(CLEANED_PATH, "reported_cases_data_cleaned.csv"), index=False)
    print("Reported cases data cleaned and saved.")

def clean_vaccine_intro():
    df = pd.read_excel(os.path.join(RAW_PATH, "vaccine-introduction-data.xlsx"))
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    df['intro'] = df['intro'].fillna("No")
    df = safe_convert_year(df)
    
    df.to_csv(os.path.join(CLEANED_PATH, "vaccine_intro_data_cleaned.csv"), index=False)
    print("Vaccine introduction data cleaned and saved.")

def clean_vaccine_schedule():
    df = pd.read_excel(os.path.join(RAW_PATH, "vaccine-schedule-data.xlsx"))
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    print("Columns found in vaccine schedule data:", df.columns.tolist())  # debug line
    
    # Only fill if the column exists
    if 'schedule_rounds' in df.columns:
        df['schedule_rounds'] = df['schedule_rounds'].fillna(0)
    else:
        print("Column 'schedule_rounds' not found, skipping fillna")
    
    if 'target_pop' in df.columns:
        df['target_pop'] = df['target_pop'].fillna("All")
    
    # Safe convert year
    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce').dropna().astype(int)
    
    df.to_csv(os.path.join(CLEANED_PATH, "vaccine_schedule_data_cleaned.csv"), index=False)
    print("Vaccine schedule data cleaned and saved.")


if __name__ == "__main__":
    clean_coverage()
    clean_incidence()
    clean_reported_cases()
    clean_vaccine_intro()
    clean_vaccine_schedule()
    print("All datasets cleaned and saved in 'data/cleaned/'")
