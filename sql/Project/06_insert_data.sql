USE RetailNova;
GO

--------------------------------------------------
-- Customers
--------------------------------------------------

INSERT INTO Customers
(customer_id, first_name, last_name, email, phone, city, state, registration_date)
VALUES
(101,'Rutuja','Kulkarni','rutuja@gmail.com','9876543210','Pune','Maharashtra','2026-01-10'),
(102,'Aman','Sharma','aman@gmail.com','9876543211','Mumbai','Maharashtra','2026-01-12'),
(103,'Sneha','Patil','sneha@gmail.com','9876543212','Nashik','Maharashtra','2026-01-14');

--------------------------------------------------
-- Products
--------------------------------------------------

INSERT INTO Products
(product_id, product_name, category_id, supplier_id, price, cost_price)
VALUES
(101,'Laptop',1,101,122.99,100.99),
(102,'Mouse',2,102,12.99,10.99),
(103,'Keyboard',2,102,30.99,27.99),
(104,'PlayStation 5',3,103,70.99,67.99),
(105,'Smart Watch',4,104,17.99,15.99);

--------------------------------------------------
-- Orders
--------------------------------------------------

INSERT INTO Orders
(order_id, customer_id, order_date, total_amount, status)
VALUES
(1001,101,'2026-01-12',159.99,'Completed'),
(1002,102,'2026-01-13',189.99,'Pending'),
(1003,103,'2026-01-14',259.99,'Cancelled');

--------------------------------------------------
-- OrderItems
--------------------------------------------------

INSERT INTO OrderItems
(order_item_id, order_id, product_id, quantity, price)
VALUES
(1,1001,101,1,122.99),
(2,1001,102,2,12.99),
(3,1002,103,1,30.99),
(4,1003,104,1,70.99),
(5,1003,105,3,17.99);

--------------------------------------------------
-- Payments
--------------------------------------------------

INSERT INTO Payments
(payment_id, order_id, payment_method, payment_date, payment_status, amount)
VALUES
(1001,1001,'Cash','2026-01-12','Completed',159.99),
(1002,1002,'UPI','2026-01-13','Pending',189.99),
(1003,1003,'Card','2026-01-14','Failed',259.99);