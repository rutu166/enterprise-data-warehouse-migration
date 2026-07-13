import pyodbc

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)

print("connected to SQL server successfully!!")
import pandas as pd
 
df=pd.read_csv("../../data/categories.csv")

cursor=connection.cursor()

for i in range(len(df)):
    category=df.iloc[i]

    cursor.execute(
        """
        INSERT INTO categories(
            category_id,
            category_name,
            status
            ) 
        values( ? , ? , ?)
        """,
        int(category["category_id"]),
        category["category_name"],
        category["status"]
    )

connection.commit()
print("All categories inserted successfully!!")