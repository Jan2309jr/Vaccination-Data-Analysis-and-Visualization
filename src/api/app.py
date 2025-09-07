from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)
DB_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://vacc_user:vacc_pass@localhost:5432/vacc_db')
engine = create_engine(DB_URL, future=True)

@app.get("/kpi/coverage_by_country")
def coverage_by_country():
    year = request.args.get('year')
    q = """
    SELECT c.country_name, avg(cv.coverage_percent) as avg_coverage
    FROM coverage cv JOIN dim_country c ON cv.iso3 = c.iso3
    WHERE (:year IS NULL OR cv.year = :year)
    GROUP BY c.country_name
    ORDER BY avg_coverage DESC
    LIMIT 500
    """
    with engine.connect() as conn:
        rows = conn.execute(text(q), {"year": int(year) if year else None }).mappings().all()
    return jsonify([dict(r) for r in rows])

@app.get("/")
def ping():
    return jsonify({"status":"ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
