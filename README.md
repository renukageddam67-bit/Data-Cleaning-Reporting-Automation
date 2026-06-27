# Data Cleaning & Reporting Automation

## Overview

This project automates the process of data cleaning and reporting using Python. The workflow handles missing values, removes duplicate records, generates summary statistics, and prepares clean data for analysis and reporting.

## Objective

The objective of this project is to improve data quality by automating data preprocessing tasks and generating reports that help in data-driven decision making.

## Dataset

Dataset Used: **train.csv**

The dataset contains sales-related information including:

* Order ID
* Order Date
* Ship Date
* Customer Information
* Product Information
* Category
* Sub-Category
* Region
* Sales
* Profit

## Features

* Load and process data using Pandas
* Detect and handle missing values
* Remove duplicate records
* Generate summary statistics automatically
* Export cleaned dataset
* Create automated reports

## Technologies Used

* Python
* Pandas
* Excel (OpenPyXL)
* Power BI
* GitHub

## Project Structure

Data-Cleaning-Reporting-Automation/

├── train.csv

├── data_cleaning.py

├── cleaned_data.csv

├── summary_report.xlsx

├── dashboard.pbix

├── dashboard.png

└── README.md

## Output Files

### cleaned_data.csv

Contains the cleaned dataset after:

* Removing duplicate records
* Handling missing values
* Data preprocessing

### summary_report.xlsx

Contains:

* Statistical summary
* Count
* Mean
* Standard Deviation
* Minimum and Maximum values

## Dashboard Features

* Total Sales KPI
* Total Profit KPI
* Sales by Category
* Sales by Region
* Sales Trend Analysis
* Interactive Filters

## How to Run

1. Install required libraries:

pip install pandas openpyxl

2. Place train.csv in the project folder.

3. Run the script:

python data_cleaning.py

4. Generated files:

* cleaned_data.csv
* summary_report.xlsx

## Expected Outcome

* Automated data cleaning workflow
* Improved data quality
* Automated reporting process
* Better understanding of data preprocessing techniques

## Author

Renuka Geddam
