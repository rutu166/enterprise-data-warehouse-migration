from db_connection import get_connection
import pandas as pd

connection=None
cursor=None

try:
    connection=get_connection()
    print("SQL connection establish successfully")
    cursor=connection.cursor()
    df=pd.read_csv("../../data/products.csv")

    rows=[]
    for product in df.itertuples():
        rows.append(
            (
                product.product_id,
                product.product_name,
                product.category_id,
                product.supplier_id,
                product.price,
                product.cost_price
            )
        )
    executemany(
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
       rows
    )
    connection.commit()
    print("Products inserted successfully!!")

except Exception as e:
    if connection:
        connection.rollback()
    print("load failed")
    print(f"error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Resoursed released")