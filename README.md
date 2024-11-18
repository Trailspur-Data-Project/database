# Project database management
This repository contains scripts and instructions for various data processing tasks, including data cleaning, data insertion, data extraction from a PostgreSQL database, as well as SQL scripts for table creation.

## Table of Contents

1. [Data Cleaning](#data-clean.py)
2. [Data Insertion](#insert_data.py)
3. [Data Extraction](#extract_data.py)
4. [Create Table SQL](#create-tables.sql)

## Prerequisite
A working SQL server, Co-star data ready to work with.

### Instructions

1. Create table first, using the [Create Table SQL](#create-tables.sql) script.
2. Clean the data by inserting the DFW_Properties file into Data Cleaning file, which creates a new cleaned `.csv` file.
3. Insert data from the csv file to database by running the code inside the [Data Insertion](#insert_data.py) file.
4. Extract the data from database for usage by running the [Data Extraction](#extract_data.py) file.
