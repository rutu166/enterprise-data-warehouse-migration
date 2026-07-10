# Business Requirement Document

## 1. Project Overview

RetailNova Pvt. Ltd. is a multinational retail organization operating both physical stores and an e-commerce platform. Over the years, the company has accumulated large volumes of transactional and customer data in a legacy on-premises SQL Server data warehouse.

As the business expanded, the existing platform began experiencing challenges related to scalability, performance, maintenance, and reporting. Business users also required faster access to reliable data for analytics and decision-making.

The objective of this project is to modernize the existing data platform by migrating data from the legacy SQL Server data warehouse to an Azure Lakehouse architecture. The new solution will leverage Azure Data Factory for orchestration, Azure Data Lake Storage for scalable storage, Databricks with PySpark for data processing, Delta Lake for reliable and optimized storage, and Power BI for business reporting.

The solution will support secure, scalable, and efficient data processing while enabling faster analytics and improved business insights.


## 2. Business Problem

RetailNova Global Ltd. currently stores business data in a legacy on-premises SQL Server data warehouse. Data is collected from multiple business applications, including sales, inventory, customer management, logistics, suppliers, and online commerce.

As business operations expanded across multiple countries, the existing platform began experiencing performance issues, increasing infrastructure costs, limited scalability, and lengthy report generation times. Different departments also maintain separate data sources, resulting in inconsistent business reports and delayed decision-making.

The organization has decided to modernize its data platform by migrating to an Azure Lakehouse architecture to improve scalability, security, performance, and business analytics.

## 3. Current Challenges

* Increasing volume of transactional and historical data.
* Slow report generation affecting business decisions.
* High maintenance cost for on-premises infrastructure.
* Limited scalability of the existing SQL Server environment.
* Data inconsistencies across different business departments.
* Manual data integration processes.
* Difficulty supporting advanced analytics and future AI initiatives.


## 4. Business Objectives

* Migrate historical and incremental data from the legacy SQL Server data warehouse to Azure Lakehouse.
* Build a scalable, secure, and highly available data platform.
* Improve data quality through validation and cleansing.
* Reduce report generation time and improve query performance.
* Enable business users to access reliable analytics through Power BI dashboards.
* Implement automated data ingestion and transformation pipelines.
* Establish a modern architecture that supports future analytics and machine learning initiatives.


## 5. Scope of Migration

The project includes the migration of business-critical datasets from the legacy SQL Server environment to Azure Lakehouse.

The migration covers the following business domains:

* Customer Management
* Product Management
* Sales Transactions
* Order Management
* Inventory Management
* Warehouse Operations
* Supplier Management
* Payment Processing
* Shipment Tracking
* Returns Management

The solution includes data ingestion, transformation, validation, storage, reporting, and monitoring.

## 6. Expected Benefits

* Faster business reporting.
* Improved scalability for growing data volumes.
* Reduced infrastructure and maintenance costs.
* Enhanced data quality and consistency.
* Better governance and security.
* Near real-time analytics for business users.
* Foundation for advanced analytics and AI workloads.


## 7. Assumptions
- Source data is available and accessible.
- Data quality issues are manageable.
- Required cloud resources are available.
- Business users have defined reporting requirements.
- Source schema changes are communicated before deployment.

## 8. Success Criteria
- 100% successful migration of required data.
- Data validation between source and target passes.
- Reports load within acceptable performance limits.
- Automated pipelines execute successfully.
- Business users can access accurate dashboards.