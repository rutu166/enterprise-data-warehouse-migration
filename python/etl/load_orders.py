import pyodbc
import pandas as pd

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)
print("SQL server connection establish successfully")

cursor=connection.cursor()

df=pd.read_csv("../../data/orders.csv")

for i in range(len(df)):
    order=df.iloc[i]

    cursor.execute(
        """
        INSERT INTO orders(
        order_id,
        customer_id,
        order_date,
        total_amount,
        status
        )
        values(?,?,?,?,?)
        """,    
        int(order["order_id"]),
        int(order["customer_id"]),
        order["order_date"],
        float(order["total_amount"]),
        order["status"]
    )

connection.commit()

print("orders inserted successfully")