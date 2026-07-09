-- Creating Categories Table
CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50),
    status VARCHAR(25)
);

-- Creating Suppliers Table
CREATE TABLE Suppliers (
    Supplier_id INT PRIMARY KEY,
    Supplier_name VARCHAR(100),
    contact_num VARCHAR(15),
    supplier_email VARCHAR(150),
    Address varchar(250)
);

-- Creating Inventory table 
CREATE TABLE Inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT,
    available_quantity INT,
    warehouse_location VARCHAR(250),
    last_updated DATE,

    FOREIGN KEY (product_id)
        REFERENCES Products(product_id)
);
