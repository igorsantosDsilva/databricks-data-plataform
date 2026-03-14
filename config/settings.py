import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# databricks_df
DBX_DF_HOST_DF_API_KEY = os.getenv("DBX_DF_HOST_DF_API_KEY")
DBX_DF_HOST = os.getenv("DBX_DF_HOST")