from db_connection import get_connection
import pandas as pd
cursor=None
connection=None

try:
    connection=get_connection()
    print("SQL connection establshied successfully!")

    cursor=connection.cursor()
    df=pd.read_csv("../../data/customers.csv")
    
    rows=[]

    for customer in df.itertuples():
        rows.append(
            (
                customer.customer_id,
                customer.first_name,
                customer.last_name,
                customer.email,
                customer.phone,
                customer.city,
                customer.state,
                customer.registration_date
            )
        )
    cursor.executemany(
    """
    INSERT INTO customers
    (
        customer_id,
        first_name,
        last_name,
        email,
        phone,
        city,
        state,
        registration_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    rows
    )
    connection.commit()
    print("all customers inserted sucessfully!!")

except Exception as e:
    if connection:
        connection.rollback()
    print("customer load failed")
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("resourses released")

