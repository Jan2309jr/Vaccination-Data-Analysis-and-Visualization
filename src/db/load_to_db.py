import os
from sqlalchemy import create_engine, text
import pandas as pd
from pathlib import Path
from src.etl.read_data import load_all
from src.etl.clean_data import clean_coverage, clean_incidence, clean_reported_cases

DB_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://vacc_user:vacc_pass@localhost:5432/vacc_db')

engine = create_engine(DB_URL, pool_pre_ping=True, future=True)

def run_schema():
    sql_path = Path(__file__).parent / "db_schema.sql"
    with engine.connect() as conn:
        sql = sql_path.read_text()
        conn.execute(text(sql))
        conn.commit()
    print("Schema created/verified")

def upsert_dim_countries(df):
    # df has columns iso3, country_name, who_region
    df = df.dropna(subset=['iso3'])
    with engine.begin() as conn:
        for _, row in df.iterrows():
            conn.execute(text("""
                INSERT INTO dim_country (iso3, country_name, who_region)
                VALUES (:iso3, :country_name, :who_region)
                ON CONFLICT (iso3) DO UPDATE SET country_name = EXCLUDED.country_name, who_region = EXCLUDED.who_region
            """), dict(iso3=row['iso3'], country_name=row.get('country_name'), who_region=row.get('who_region')))
    print("Countries upserted")

def bulk_insert(df, table_name, dtype_map=None):
    # simple bulk insert via pandas to_sql
    df.to_sql(table_name, con=engine, if_exists='append', index=False, method='multi', chunksize=1000)
    print(f"{len(df)} rows inserted into {table_name}")

def main():
    run_schema()
    data = load_all()
    # clean each
    cov = clean_coverage(data['coverage'])
    inc = clean_incidence(data['incidence'])
    rep = clean_reported_cases(data['reported_cases'])
    # build dim_country from coverage (and other tables)
    from src.etl.transform_normalize import build_dim_countries
    dim_countries = build_dim_countries([cov, inc, rep, data['vaccine_intro'], data['vaccine_schedule']])
    upsert_dim_countries(dim_countries.rename(columns={'name':'country_name'}))
    # prepare dims
    dim_antigen = cov[['antigen_code','antigen_description']].drop_duplicates().dropna(subset=['antigen_code'])
    dim_disease = pd.concat([
        inc[['disease_code','disease_description']],
        rep[['disease_code','disease_description']]
    ]).drop_duplicates().dropna(subset=['disease_code'])
    # upsert dims
    with engine.begin() as conn:
        for _, r in dim_antigen.iterrows():
            conn.execute(text("""
            INSERT INTO dim_antigen (antigen_code, antigen_description)
            VALUES (:code, :desc)
            ON CONFLICT (antigen_code) DO UPDATE SET antigen_description = EXCLUDED.antigen_description
            """), dict(code=r['antigen_code'], desc=r.get('antigen_description')))
        for _, r in dim_disease.iterrows():
            conn.execute(text("""
            INSERT INTO dim_disease (disease_code, disease_description)
            VALUES (:code, :desc)
            ON CONFLICT (disease_code) DO UPDATE SET disease_description = EXCLUDED.disease_description
            """), dict(code=r['disease_code'], desc=r.get('disease_description')))
    # Insert main tables
    cov_insert = cov[['iso3','year','antigen_code','coverage_category','coverage_category_description','target_number','doses','coverage']].rename(columns={'coverage':'coverage_percent'})
    cov_insert['coverage_percent'] = cov_insert['coverage_percent'].round(2)
    bulk_insert(cov_insert, 'coverage')
    inc_insert = inc[['iso3','year','disease_code','denominator','incidence_rate']]
    bulk_insert(inc_insert, 'incidence')
    rep_insert = rep[['iso3','year','disease_code','cases']]
    bulk_insert(rep_insert, 'reported_cases')
    print("ETL load finished")

if __name__ == "__main__":
    main()
