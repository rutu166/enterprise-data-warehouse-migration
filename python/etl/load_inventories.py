import pyodbc
import pandas as pd

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)

print("SQL connection established successfully!!")

df=pd.read_csv("../../data/inventory.csv")

cursor=connection.cursor()

for i in range(len(df)):
    inventory=df.iloc[i]

    cursor.execute(
        """
        INSERT INTO inventory(
        inventory_id,
        product_id,
        available_quantity,
        warehouse_location,
        last_updated
        )
        values(?,?,?,?,?)
        """,
        int(inventory["inventory_id"]),
        int(inventory["product_id"]),
        int(inventory["available_quantity"]),
        inventory["warehouse_location"],
        inventory["last_updated"]
    )

connection.commit()
print("all inventories updated successfully")
