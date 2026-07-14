from db_connection import get_connection
import pandas as pd

connection=None
cursor=None

try:
    connection=get_connection()
    print("SQL server established successfully")

    cursor=connection.curosr()
    rows=[]

    df=pd.read_csv("../../data/suppliers.csv")

    for supplier in df.itertuples():
        rows.append(
            (
            supplier.supplier_id,
            supplier.supplier_name,
            supplier.contact_number,
            supplier.supplier_email, 
            supplier,address
     ) )
    cursor.executemany(
        """
        INSERT INTO suppliers(
        "supplier_id",
        "supplier_name",
        "contact_number",
        "supplier_email",
        "address"
        )
        VALUES ( ? , ? , ? , ? , ?)
        """,
        rows
    )
    connection.commit()
    print("Suppliers inserted successfull!")

except Exception as e:
    if connection:
        connection.rollback()
    print("Load failed")
    print(f"error : {e}")

finally:
    if cursor:
        curosr.close()
    if connection:
        connection.close()
    print("Resourses released")