USE RetailNova;
GO

--------------------------------------------------
-- Categories
--------------------------------------------------

INSERT INTO Categories
(category_id, category_name, status)

VALUES
(1,'Electronics','Active'),
(2,'Accessories','Active'),
(3,'Gaming','Active'),
(4,'Wearables','Active'),
(5,'Home Appliances','Inactive');

--------------------------------------------------
-- Suppliers
--------------------------------------------------

INSERT INTO Suppliers
(supplier_id,supplier_name,contact_number,supplier_email,address)

VALUES
(101,'Dell India','9876543201','sales@dell.com','Bengaluru'),
(102,'Logitech India','9876543202','support@logitech.com','Mumbai'),
(103,'Sony India','9876543203','contact@sony.com','Delhi'),
(104,'Boat Lifestyle','9876543204','info@boat.com','Mumbai'),
(105,'HP India','9876543205','support@hp.com','Pune');

--------------------------------------------------
-- Inventory
--------------------------------------------------

INSERT INTO Inventory
(inventory_id,product_id,available_quantity,warehouse_location,last_updated)

VALUES
(1,101,45,'Pune Warehouse','2026-07-10'),
(2,102,150,'Mumbai Warehouse','2026-07-10'),
(3,103,90,'Hyderabad Warehouse','2026-07-10'),
(4,104,30,'Delhi Warehouse','2026-07-10'),
(5,105,75,'Pune Warehouse','2026-07-10');