import psycopg2
import os
from dotenv import dotenv_values, load_dotenv
from pathlib import Path

# global psql connection instance
psql_conn = None


def init_db_conn():
    global psql_conn
    # Use load_dotenv to set variables in environment
    load_dotenv()

    DB_USER_NAME     = os.getenv('postgres')
    DB_USER_PASSWORD = os.getenv('021202')
    DB_ADDRESS       = os.getenv('localhost')
    DB_NAME          = os.getenv('Web')
    
    try:
        psql_conn = psycopg2.connect(
            dbname = DB_NAME,
            user = DB_USER_NAME,
            host = DB_ADDRESS,
            password = DB_USER_PASSWORD
        )
        
    except Exception as e:
        # print(f"Error connecting to database: {e}")
        psql_conn = None

    # print(f"conneted to database: {psql_conn}")


def get_psql_conn():
    # print(psql_conn)
    return psql_conn