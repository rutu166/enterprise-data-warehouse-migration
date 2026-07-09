USE RetailNova;
GO

CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_method VARCHAR(20),
    payment_date DATE,
    payment_status VARCHAR(20),
    amount DECIMAL(10,2),

    FOREIGN KEY (order_id)
        REFERENCES Orders(order_id)
);