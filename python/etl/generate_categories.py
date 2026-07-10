import pandas as pd

categories=[
    {"category_id":1,"category_name":"Electronics","status":"Active"},
    {"category_id": 2, "category_name": "Clothing", "status": "Active"},
    {"category_id": 3, "category_name": "Grocery", "status": "Active"},
    {"category_id": 4, "category_name": "Furniture", "status": "Active"},
    {"category_id": 5, "category_name": "Sports", "status": "Active"},
    {"category_id": 6, "category_name": "Books", "status": "Active"},
    {"category_id": 7, "category_name": "Beauty", "status": "Active"},
    {"category_id": 8, "category_name": "Toys", "status": "Active"}
]

df=pd.DataFrame(categories)

print(df)

df.to_csv("../../data/categories.csv",index=False)

print("categories.csv created successfully")