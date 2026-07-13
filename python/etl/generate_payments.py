import random 
import pandas as pd
from faker import Faker

fake=Faker()

payment_method = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Cash on Delivery"
]

payment_status = [
    "Success",
    "Pending",
    "Failed",
    "Refunded"
]

NUMBER_OF_PAYMENTS=20000

payments=[]

for i in range(NUMBER_OF_PAYMENTS):
    payments.append({
        "payment_id":i+1,
        "order_id":i+1,
        "payment_method":random.choice(payment_method),
         "payment_date":fake.date_between(
            start_date="-1y",end_date="today"
        ),
        "payment_status":random.choice(payment_status),
        "amount":random.randint(500,5000)
    })

df=pd.DataFrame(payments)

print(df)

df.to_csv("../../data/payments.csv",index=False)

print("payments.csv generated successfully!")