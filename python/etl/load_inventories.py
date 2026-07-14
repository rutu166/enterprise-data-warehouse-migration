from db_connection import get_connection
import pandas as pd

connection=None
cursor=None

try:
    connection=get_connection()
    cursor=connection.cursor()
    print("SQL established successfully!!")

    df=pd.read_csv("../../data/inventory.csv")
    rows=[]

    for inventory in df.itertuples():
        rows.append(
            (
                inventory.inventory_id,
                inventory.product_id,
                inventory.available_quantity,
                inventory.warehouse_location,
                inventory.last_updated
            )
        )
    cursor.executemany(
        """
        INSERT INTO inventory(
        inventory_id,
        product_id,
        available_quantity,
        warehouse_location,
        last_updated
        )
        values(?,?,?,?,?)
        """,
        rows
    )
    connection.commit()
    print("Inevtories inserted successfully!!")

except Exception as e:
    if connection:
        connection.rollback()
    print("Load failed")
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()
    print("Resourses released")