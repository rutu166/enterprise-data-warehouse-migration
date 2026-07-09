USE RetailNova;
GO

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(20),

    FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id)
);