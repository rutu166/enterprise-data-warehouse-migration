import random
import pandas as pd
from faker import Faker

fake=Faker()


warehouse_location = [
    "Pune Warehouse",
    "Mumbai Warehouse",
    "Delhi Warehouse",
    "Bangalore Warehouse",
    "Hyderabad Warehouse",
    "Chennai Warehouse",
    "Kolkata Warehouse",
    "Ahmedabad Warehouse"
]
NUMBER_OF_INVENTORIES=1000

inventory=[]

for i in range(NUMBER_OF_INVENTORIES):


    {
        inventory.append({
            "inventory_id":i+1,
            "product_id":i+1,
            "available_quantity":random.randint(0,500),
            "warehouse_location":random.choice(warehouse_location),
            "last_updated":fake.date_between(
                start_date="-1y",end_date="today"
            )
    
        })
    }
df=pd.DataFrame(inventory)

print(df)

df.to_csv("../../data/inventory.csv", index=False)

print("inventory.csv file generated successfully!")