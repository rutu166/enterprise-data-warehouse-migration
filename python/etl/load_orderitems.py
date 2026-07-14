from db_connection import get_connection
import pandas as pd

connection=None
cursor=None
try:
    connection=get_connection()
    print("Connection established successfully")
    cursor=connection.cursor()
    df=pd.read_csv("../../data/orderitems.csv")
    rows=[]
    for orderitem in df.itertuples():
        rows.append(
            (
                orderitem.order_item_id,
                orderitem.order_id,
                orderitem.product_id,
                orderitem.quantity,
                orderitem.price
            )
        )
    cursor.executemany(
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
            rows
    )
    connection.commit()
    print("Orderitems inserted successfully!")
except Exception as e:
    if connection:
        connection.rollback()
    print("load failed")
    print(f"Error: {e}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("resourses released")