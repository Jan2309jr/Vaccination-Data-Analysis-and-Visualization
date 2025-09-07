import os

print("🚀 Running Vaccination Data Project")

# Step 1: Clean Data
os.system("python scripts/clean_data.py")

# Step 2: Load Data into SQL
os.system("python scripts/load_to_sql.py")

print("✅ Pipeline Completed. Now open Power BI and connect to SQL.")
