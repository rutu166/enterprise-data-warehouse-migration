from db_connection import get_connection
import pandas as pd

connection=None
cursor=None

try:
    connection=get_connection()
    print("Connection established successfully!!")
    cursor=connection.cursor()

    df=pd.read_csv("../../data/orders.csv")
    rows=[]

    for order in df.itertuples():
        rows.append(
           (
            order.order_id,
            order.customer_id,
            order.order_date,
            order.total_amount,
            order.status
         ) )
        cursor.executemany(
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
            rows
    )
    connection.commit()
    print("Orders inserted successfully")
except Exception as e:
    if connection:
        connection.rollback()
    print("Load failed")
    print(f"error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

    print("resourses released")
