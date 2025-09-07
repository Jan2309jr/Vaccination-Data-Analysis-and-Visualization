# Vaccination Data Analysis and Visualization

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql)
![Power BI](https://img.shields.io/badge/BI-PowerBI-yellow?logo=powerbi)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Analyze and visualize global vaccination and disease incidence data to support public health strategies, resource allocation, and vaccine effectiveness studies. Cleaned datasets are stored in a SQL database and brought to life with interactive Power BI dashboards.

---

## Project Overview

This project investigates global vaccination coverage and disease incidence trends using cleaned, structured health data. Insights from interactive dashboards empower stakeholders to improve immunization programs, target interventions, and inform health policy.

---

## Skills and Technologies

- **Python:** Data cleaning, transformation, EDA  
- **SQL (MySQL):** Normalized schema, data integrity  
- **Power BI:** Dashboards, geographic maps, time series  
- **Healthcare Analytics:** Public Health, Epidemiology

---

## Problem Statement

Analyze multi-year, multi-region data to answer:  
- How do vaccination rates impact disease incidence?  
- Where are coverage gaps, and what improvements are needed?  
- What policies or resource allocations will most benefit population health?

---

## Business Use Cases

- **Public Health:** Assess program effectiveness, identify intervention areas  
- **Disease Prevention:** Detect vaccine inefficacies, recommend booster campaigns  
- **Resource Allocation:** Pinpoint regions for targeted distribution  
- **Global Policy:** Supply data-driven recommendations for government/NGO strategies

---

## Data Pipeline & Architecture

1. **Raw Data Cleaning**  
   - Python scripts (see `scripts/clean_data.py`) clean Excel sheets, handle missing values, normalize columns  

2. **SQL Database Normalization**  
   - Relational design with lookup and fact tables (see `sql/sql_setup.sql`)  

3. **ETL Loading**  
   - Python (`scripts/load_to_sql.py`) loads cleaned CSVs into MySQL database  

4. **Power BI Integration**  
   - `.pbix` file connects live to SQL database for visual exploration  

**Schema Overview:**
- CoverageData, DiseaseIncidence, ReportedCases  
- VaccineIntroduction, VaccineSchedule  
- Countries, Vaccines, Diseases 

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/vaccination-data-analysis.git
   cd vaccination-data-analysis
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your MySQL database:**

   * Update connection details in `scripts/load_to_sql.py`
   * Run the SQL schema setup:

     ```bash
     mysql -u root -p < sql/sql_setup.sql
     ```

4. **Clean the data:**

   ```bash
   python scripts/clean_data.py
   ```

5. **Load data to SQL database:**

   ```bash
   python scripts/load_to_sql.py
   ```

6. **Open Power BI report:**

   * Open `powerbi/vaccination_data_analysis.pbix`
   * Connect to your MySQL database

---

## How It Works

* Data extracted, cleaned, and normalized with Python scripts
* ETL pipeline loads all tables to MySQL, enforcing strict relationships
* Power BI dashboards visualize coverage rates, disease incidence, annual trends, and highlight actionable insights

---

## Power BI Visualizations

* **Geographical Heatmaps:** Vaccination coverage & disease incidence by region
* **Trend Lines/Bar Charts:** Yearly changes and vaccination effect over time
* **KPI Cards:** Quick stats vs. targets/goals
* **Scatter Plots:** Correlation between disease rates & vaccine coverage

![Key Visualizations](assets/visualizations.png)

---

## Exploratory Data Analysis

Analyze patterns and disparities by:

* Region, gender, urban/rural, education level
* Booster dose trends and seasonality
* Disease incidence before/after vaccine introduction
* Coverage gaps for high-priority diseases (e.g., TB, Hepatitis B)

---

## Key Questions Addressed

* How do vaccination rates correlate with disease reduction?
* What are the coverage gaps and drop-off between dose rounds?
* Are there disparities by region, gender, education, or urban/rural?
* Which campaigns have made the most impact?
* What is the forecast for future vaccine demand?
<img width="958" height="535" alt="image" src="https://github.com/user-attachments/assets/03f9d9d3-ffaa-4502-8b27-4f6558d78830" />

---

## Contributing

Contributions are welcome!

* Fork the repo and submit a pull request
* File issues for bugs or missing features
* Add new data sources or visualization templates

---
