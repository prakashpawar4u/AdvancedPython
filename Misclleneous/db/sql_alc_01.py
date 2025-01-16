# Note: Install pandas, sqlalchemy and psycopg2
import sqlalchemy

from sqlalchemy import create_engine

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Define the connection string
db_url = "postgresql+psycopg2://postgres:postgres@192.168.56.114:5432/otaf_git11"

try:
    # Create an engine
    engine = create_engine(db_url)

    print("Engine created successfully")

    query = "SELECT * FROM job_creation_details"
    df = pd.read_sql(query, engine)

    print(df.head())
except Exception as e:
    print(f"Error occured :: {e}")
finally:
    print("Closing the db connection")
    engine.dispose()
