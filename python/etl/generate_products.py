import random
import pandas as pd

product_names = [
    "Samsung Smart TV",
    "Apple iPhone 15",
    "Nike Running Shoes",
    "Dell Laptop",
    "Office Chair",
    "Dining Table",
    "Coffee Maker",
    "Mixer Grinder",
    "Bluetooth Speaker",
    "Wireless Mouse",
    "Keyboard",
    "Air Conditioner",
    "Refrigerator",
    "Washing Machine",
    "Microwave Oven",
    "School Bag",
    "Water Bottle",
    "Cricket Bat",
    "Football",
    "Novel Book"
]
products=[]

price = random.randint(500, 50000)

cost_price = int(price * random.uniform(0.6, 0.9))

NUMBER_OF_PRODUCTS=1000

for i in range(NUMBER_OF_PRODUCTS):

    products.append({

        "product_id":i+1,
        "product_name":random.choice(product_names),
        "category_id":random.randint(1,8),
        "supplier_id":random.randint(1,50),
        "price":price,
        "cost_price":cost_price
    }
    )

df=pd.DataFrame(products)

print(df)

df.to_csv("../../data/products.csv",index=False)

print("products.csv created successfully!")

