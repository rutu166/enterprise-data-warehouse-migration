import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RetailNova;"
    "Trusted_Connection=yes;"
)

print("Connected to SQL Server successfully!")


import pandas as pd

df = pd.read_csv("../../data/customers.csv")

#print(df.head())

cursor=connection.cursor()

#customer=df.iloc[10]

#print(customers)

#print(customers["customer_id"])
#print(customers["first_name"])

for i in range(len(df)):
    customer = df.iloc[i]

    cursor.execute(
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
        int(customer["customer_id"]),
        customer["first_name"],
        customer["last_name"],
        customer["email"],
        str(customer["phone"]),
        customer["city"],
        customer["state"],
        customer["registration_date"]
    )

connection.commit()

print("All customers inserted successfully!")