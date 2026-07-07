USE RetailNova;
GO

-- 1. Show completed orders

SELECT order_id, customer_id, status
FROM Orders
WHERE status='Completed';

---------------------------------------------------

-- 2. Customers from Maharashtra

SELECT first_name AS Name,
       city
FROM Customers
WHERE state='Maharashtra';

---------------------------------------------------

-- 3. Customer name with order date and status

SELECT c.first_name,
       o.order_date,
       o.status
FROM Customers c
JOIN Orders o
ON c.customer_id=o.customer_id;

---------------------------------------------------

-- 4. Product name with quantity and price

SELECT p.product_name,
       oi.quantity,
       oi.price
FROM Products p
JOIN OrderItems oi
ON p.product_id=oi.product_id;

---------------------------------------------------

-- 5. Total amount spent by each customer

SELECT c.first_name,
       SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o
ON c.customer_id=o.customer_id
GROUP BY c.first_name;

---------------------------------------------------

-- 6. Customer payment details

SELECT c.first_name,
       p.payment_method,
       p.payment_status
FROM Customers c
JOIN Orders o
ON c.customer_id=o.customer_id
JOIN Payments p
ON o.order_id=p.order_id;

---------------------------------------------------

-- 7. Customer, Product, Quantity and Payment Method

SELECT c.first_name AS customer_name,
       p.product_name,
       oi.quantity,
       py.payment_method
FROM Customers c
JOIN Orders o
ON c.customer_id=o.customer_id
JOIN OrderItems oi
ON o.order_id=oi.order_id
JOIN Products p
ON p.product_id=oi.product_id
JOIN Payments py
ON o.order_id=py.order_id;