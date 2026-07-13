from faker import Faker
import pandas as pd
import random

fake = Faker()

suppliers = []

NUMBER_OF_SUPPLIERS = 50

for i in range(NUMBER_OF_SUPPLIERS):
    suppliers.append({
        "supplier_id": i + 1,
        "supplier_name": fake.company(),
        "contact_number": str(random.randint(6000000000,9999999999)),
        "supplier_email": fake.company_email(),
        "address": fake.address().replace("\n", ", ")
    })

df = pd.DataFrame(suppliers)

print(df)

df.to_csv("../../data/suppliers.csv", index=False)

print("suppliers.csv created successfully!")