from faker import Faker
import random
import pandas as pd

fake=Faker()
NUMBER_OF_ORDERITEMS=50000
orderitems=[]

for i in range(NUMBER_OF_ORDERITEMS):
          orderitems.append({
            "order_item_id":i+1,
            "order_id":random.randint(1,20000),
            "product_id":random.randint(1,1000),
            "quantity":random.randint(1,5),
            "price":random.randint(100,50000)
        })


df=pd.DataFrame(orderitems)
print(df)

df.to_csv("../../data/orderItems.csv",index=False)

print("orderItems.csv file generated successfully!")
