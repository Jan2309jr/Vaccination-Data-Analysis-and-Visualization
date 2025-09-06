# Vaccination Data Analysis and Visualization Project
## Project Overview

This project focuses on analyzing global vaccination data to understand trends in vaccination coverage, disease incidence, and the effectiveness of vaccination programs. The data is processed using Python, stored in a normalized SQL database, and then visualized with interactive dashboards in Power BI.
## Project Goals

    Data Cleaning and Preparation: Handle missing values, normalize data units, and ensure consistency across multiple datasets.

    SQL Database Management: Design and implement a structured SQL database with proper relationships to store the cleaned data.

    Data Visualization: Create dynamic and actionable dashboards in Power BI to answer key questions related to public health strategy, disease prevention, and resource allocation.

## Folder Structure

.
├── data/                       # Contains the raw Excel data files
│
├── scripts/                    # Contains all Python and SQL scripts
│   ├── create_tables.sql       # SQL script to set up the database schema
│   ├── load_to_sql.py          # Python script to clean and load data into SQL
│   └── dashboard_queries.sql   # SQL queries for use in Power BI
│
└── README.md                   # This file

## Setup and Execution
### Prerequisites

    A running SQL Server instance (e.g., SQL Server, Azure SQL Database).

    ODBC driver for SQL Server installed.

    Python 3.x with the following libraries: pandas, sqlalchemy, and pyodbc. You can install them using pip:

    pip install pandas sqlalchemy pyodbc

    Power BI Desktop.

#### Step 1: Set up the SQL Database

    Open your SQL Server management tool (like SQL Server Management Studio).

    Run the scripts/create_tables.sql file to create the VaccinationDB database and all the necessary tables.

#### Step 2: Load the Data

    Place your raw Excel files (from the dataset explanation) into the data/ folder.

    Open the scripts/load_to_sql.py file and update the DB_CONNECTION_STRING with your SQL Server credentials.

    Run the Python script from your terminal:

    python scripts/load_to_sql.py

    This script will perform data cleaning and populate your SQL database.

#### Step 3: Build the Power BI Dashboards

    Open Power BI Desktop.

    Click Get Data and select SQL Server database.

    Enter localhost for the server and VaccinationDB for the database. Choose DirectQuery mode.

    Select all the tables and click Load.

    Use the SQL queries from scripts/dashboard_queries.sql as a guide to create the visualizations outlined in the project brief.

    Design and build the interactive dashboards to answer the project's key questions.