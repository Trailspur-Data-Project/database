import pandas as pd
from sqlalchemy import create_engine

# Replace with your PostgreSQL credentials
username = 'postgres'
password = '1'
host = 'localhost' 
port = '5432'  
database = 'postgres'

# Create a connection string
connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Query to extract data
query = "SELECT * FROM dfw_properties;"

# Extract data from the database into a pandas DataFrame
df = pd.read_sql(query, engine)

# Display the DataFrame
print(df.head())
