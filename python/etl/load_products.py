import pandas as pd
import pyodbc

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)

print("SQL server connection done!")

df=pd.read_csv("../../data/products.csv")

cursor=connection.cursor()

for i in range(len(df)):
    product=df.iloc[i]

    cursor.execute(
        """
        INSERT INTO products(
        product_id,
        product_name,
        category_id,
        supplier_id,
        price,
        cost_price
        )
        values(? , ? , ? , ? , ? , ? )
        """,
        int(product["product_id"]),
        product["product_name"],
        int(product["category_id"]),
        int(product["supplier_id"]),
        float(product["price"]),
        float(product["cost_price"])

    )
connection.commit()

print("All products inserted successfully!!")