from db_connection import get_connection
import pandas as pd

connection=None
cursor=None

try:
    connection=get_connection()
    cursor=connection.cursor()

    print("SQL connection done successfully!")

    df=pd.read_csv("../../data/categories.csv")


    rows=[]

    for category in df.itertuples():
        rows.append(
            (
                category.category_id,
                category.category_name,
                category.status
            )
        )
    cursor.executemany(
        """
        INSERT INTO categories(
            category_id,
            category_name,
            status
            ) 
        values( ? , ? , ?)
        """,
        rows
    )
    connection.commit()
    print("All categoroies inserted successfully!")

except Exception as e:

    if connection:
        connection.rollback()
    print("Categories load failed")
    print(f"error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:    
        connection.close()
    print("Resourses released!!")
    


    