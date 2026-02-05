# MABA 6321 Lab 4: Modeling Data with ER Diagrams

In this lab, we will practice creating ER diagram using MySQL Workbench, as well as identifying entities, attributes, and relationships based on the given business description.

### 1. Consulting contracts

Create an ER diagram using **MySQL Workbench** based on the following description.

* The `consulting contracts` database has three entities: `consultants`, `companies`, and `contracts`.
* `Consultants` has three attributes: `consultant_id`, `consultant_name`, and `specialties`, where `consultant_id` is its primary key (PK).
* `Companies` has three attributes also: `company_id`, `company_name`, and `industry_type`, where the first one is the PK.
* `Contracts` has six attributes:`contract_id`, `company_id`, `consultant_id`, `contract_date`, `hourly_rate`, and `hours`, where the first one is the PK, and the second and third are PKs.

You may assume that all relationships are mandatory on both sides.

### 2. Sports Goods

The Sports Goods sales system maintains detailed records of employees, customers, orders, and products.

* For each customer, it maintains information such as name, address, city, state, zip code, and phone number. Each customer is uniquely identified by a CustomerID.
* Each order is uniquely identified by an OrderNo and includes the order date and total amount. Every order is associated with exactly one customer and one employee, indicating who placed the order and who handled it. The employees involved in the sales process are identified by an EmployeeID and have attributes such as first name, last name, and job title.
* Each order may include multiple products. For each product in an order, the system captures the quantity and purchase price. Each product is identified by a ProdID and includes descriptive attributes such as product name, group (or category), wholesale and retail prices, and the number of units currently on hand.

Create an ER diagram using **MySQL Workbench** based on the above business requirements. If you identify a many-to-many relationship, please convert it to a one-to-many relationships with an associative entity.

### 3. **Fraud Detection**

You are tasked with designing the database for a digital financial services platform that provides online payment and transaction services to a growing user base. The platform allows users to register accounts, log in from different devices, make financial transactions, and make payments using various methods. A critical business requirement is the ability to monitor user activity for fraud detection and generate appropriate reports for high-risk transactions.

Each user on the platform has a unique identifier and associated metadata, such as the date the account was created, the most recent login date, the current account status, and a cumulative count of past transactions. The platform supports device-based logins, meaning that users may interact with the platform using one or more devices, each uniquely identified by a device ID and specified by device type and MAC address.

All transactions are tracked with detailed logs that include the user involved, the transaction amount, the type of transaction (e.g., deposit, withdrawal, purchase), the date, and the device and IP address from which it was made. Additional metadata such as geolocation and number of login attempts at the time of the transaction are also captured. This data is crucial for behavioral analysis and anomaly detection.

To mitigate financial risks, the system includes a fraud detection component. When a suspicious transaction is identified, it is logged in a fraud report, which records the type of fraud, a risk score, and the current resolution status. Each fraud report is linked to both the transaction in question and the user associated with it. This allows the platform to analyze fraudulent behavior across different users and transactions for audit or enforcement actions.

Finally, the platform tracks payments made by users. A user may have multiple payment records, each specifying the payment amount, payment method (e.g., credit card, PayPal), the last four digits of a payment card, and the payment status (e.g., successful, failed, pending). These records are used to manage and reconcile financial flows, support refunds, and maintain compliance with industry standards for transaction processing.

Create an ER diagram using **MySQL Workbench** based on the above business requirements. If you identify a many-to-many relationship, please convert it to a one-to-many relationships with an associative entity.

---

#### Submission guidelines

* submit the PDFs for ER diagrams, one for each ERD.
