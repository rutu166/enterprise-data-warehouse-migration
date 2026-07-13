import pyodbc
import pandas as pd

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)
print("SQL connection successfully!")

df=pd.read_csv("../../data/orderitems.csv")

cursor=connection.cursor()

for i in range(len(df)):
        orderItem=df.iloc[i]
        cursor.execute(
            """
            INSERT INTO orderitems(
                order_item_id,
                order_id,
                product_id,
                quantity,
                price           
            )
            values(?,?,?,?,?)
            """,
            int(orderItem["order_item_id"]),
            int(orderItem["order_id"]),
            int(orderItem["product_id"]),
            int(orderItem["quantity"]),
            float(orderItem["price"])

        )
    
connection.commit()
print("orderItems inserted successfully")

