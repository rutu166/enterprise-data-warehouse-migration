import pandas as pd
import pyodbc

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)
print("SQL server connected successfully!")

df=pd.read_csv("../../data/payments.csv")

cursor=connection.cursor()

for i in range(len(df)):
    payment=df.iloc[i]
    cursor.execute(
        """
        INSERT INTO payments(
        payment_id,
        order_id,
        payment_method,
        payment_date,
        payment_status,
        amount
        )
        values(?,?,?,?,?,?)
        """,
        int(payment["payment_id"]),
        int(payment["order_id"]),
        payment["payment_method"],
        payment["payment_date"],
        payment["payment_status"],
        float(payment["amount"])

    )

connection.commit()

print("Payments inserted successfully")