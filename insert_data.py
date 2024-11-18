# Server [localhost]:
# Database [postgres]:
# Port [5432]:
# Username [postgres]:
# Password for user postgres:1

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

username = 'postgres'
password = '1'
host = 'localhost' 
port = '5432'  
database = 'postgres'

# Create a connection string
connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create an SQLAlchemy engine
try:
    engine = create_engine(connection_string)
    print("Database connection successful.")
except SQLAlchemyError as e:
    print(f"Error connecting to database: {e}")
    exit(1)  # Exit if unable to connect

df = pd.read_csv('cleaned_DFW_Properties.csv')

# Insert data into the 'dfw_properties' table
try:
    df.to_sql('dfw_properties', engine, index=False, if_exists='replace')  
    print("Data inserted successfully.")
except SQLAlchemyError as e:
    print(f"Error inserting data: {e}")

