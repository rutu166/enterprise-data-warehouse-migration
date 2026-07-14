from db_connection import get_connection
import pandas as pd

connection=None
cursor=None

try:
    connection=get_connection()
    print("Connection established successfully")
    cursor=connection.cursor()

    df=pd.read_csv("../../data/payments.csv")
    rows=[]

    for payment in df.itertuples():
        rows.append(
            (
                payment.payment_id,
                payment.order_id,
                payment.payment_method,
                payment.payment_date,
                payment.payment_status,
                payment.amount
            )
        )
    cursor.executemany(
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
        rows
    )
    connection.commit()
    print("Payments inserted successfully!!")

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
    print("Resourses released")