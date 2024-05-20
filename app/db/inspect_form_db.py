import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Function to inspect the table structure
def inspect_table():
    query = """
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = 'form_data';
    """
    table_structure = pd.read_sql(query, engine)
    print("Table structure for 'form_data':")
    print(table_structure)

# Function to fetch and display all rows from the form_data table
def fetch_all_rows():
    query = "SELECT * FROM form_data;"
    data = pd.read_sql(query, engine)
    print("\nData in 'form_data':")
    print(data)

if __name__ == "__main__":
    inspect_table()
    fetch_all_rows()