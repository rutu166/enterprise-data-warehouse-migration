import pyodbc
from config import DRIVER, SERVER, DATABASE, TRUSTED_CONNECTION

def get_connection():
    connection = pyodbc.connect(
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"Trusted_Connection={TRUSTED_CONNECTION};"
    )

    return connection