from faker import Faker
import pandas as pd

fake = Faker()

customers = []                     # List to store all customers

NUMBER_OF_CUSTOMERS = 10000        # Number of customers to generate

for i in range(NUMBER_OF_CUSTOMERS):
    customers.append({
    "customer_id": i + 1,
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "city": fake.city(),
    "state": fake.state(),
    "registration_date": fake.date_between(start_date="-3y", end_date="today")
})
df = pd.DataFrame(customers)

print(df)

df.to_csv("../../data/customers.csv", index=False)

print("customers.csv created successfully!")