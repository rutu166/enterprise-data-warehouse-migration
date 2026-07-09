USE RetailNova;
GO

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT,
    supplier_id INT,
    price DECIMAL(10,2),
    cost_price DECIMAL(10,2)
);