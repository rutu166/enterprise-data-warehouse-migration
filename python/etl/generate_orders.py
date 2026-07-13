from faker import Faker
import random
import pandas as pd

fake=Faker()

status = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]

NUMBER_OF_ORDERS=20000

orders=[]

for i in range(NUMBER_OF_ORDERS):
    [
        orders.append({
            "order_id":i+1,
            "customer_id":random.randint(1,10000),
            "order_date":fake.date_between(
                start_date="-1y",end_date="today"
            ),
            "total_amount":random.randint(500,50000),
            "status":random.choice(status)
        })
    ]

df=pd.DataFrame(orders)

print(df)

df.to_csv("../../data/orders.csv",index=False)

print("orders.csv file generated successfully!")
