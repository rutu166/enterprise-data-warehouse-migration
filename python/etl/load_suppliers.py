import pyodbc
import pandas as pd

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)

print("Sql server connect has been done successfully!!")

df=pd.read_csv("../../data/suppliers.csv")

cursor=connection.cursor()

for i in range(len(df)):
    supplier=df.iloc[i]

    cursor.execute(

        """
        INSERT INTO suppliers(
        "supplier_id",
        "supplier_name",
        "contact_number",
        "supplier_email",
        "address"
        )
        VALUES ( ? , ? , ? , ? , ?)
        """,
        int(supplier["supplier_id"]),
        supplier["supplier_name"],
        str(supplier["contact_number"]),
        supplier["supplier_email"],
        supplier["address"]
    )
connection.commit()
print("All suppliers inserted sucessfully!!")
