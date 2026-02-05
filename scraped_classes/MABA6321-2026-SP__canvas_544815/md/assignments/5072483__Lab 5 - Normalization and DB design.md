# MABA 6321 Lab 5 - Normalization and DB design

[sportsGoods.mwb](https://canvas.umn.edu/courses/544815/files/58502053?verifier=zt5LN6S2P4KstNvZMNxbgaixfJTNiZQHbGvbbn4M&wrap=1 "Link")

In this lab, we will focus on normalization and MySQL database design.

* It is recommended that you create a single google doc to hold answers for all three questions.

## Part 1: Normalization

For each problem below, transform the table(s) into a database design that satisfieds the 3rd normal form.

* Do so step by step - first check and satisfy the 1st normal form, then the 2nd normal form, and the third normal form.
* Please give each table an appropriate name that reflects its granularity and content.
* Please also mark each table's primary key fields with PK (or bold or underline).

### 1. employee training courses

In this example, we consider a business scenario where a corporation tracks employee participation in professional training courses. Originally, all the information is stored in one table, which leads to data redundancy and update anomalies. The initial table looks like this:

* **EmployeeTraining** (emp\_id, name, dept, salary, training\_course\_id, training\_date)

### 2. Online Retails Sales

Imagine you’re working with an e-commerce dataset that tracks sales transactions. The initial design is a single large table with order details, customer information, and product data, which leads to redundancy and potential data anomalies.

* **SalesData** (order\_id, order\_date, customer\_id, customer\_name, email, shipping\_address, product\_id, product\_name, unit\_price, quantity)

## Part 2. MySQL Database creation

### 3. Create a `SportsGoods` database

`sportsgood.mdb` is the MySQL workbench EER diagram we have created in the previous week. In this lab problem, we are going to create a database based on the EER model. We will then use generative AI (e.g. ChatGPT) to generate sample data and populate the database. Finally we will verify our database by creating a multi-table query.

* `sportsgood.mwb` was created with out much regard to the field data type. We now want to make these improvements before creating the database.

  + All the financial fields should use a `decimal(10,2)` data type.
  + Some fields should be integeter type (e.g. zip code, prodID, Onhands)
  + Data/Datetime fields should have `date` and `datetime` data types, respectively.
  + The database (schema) should be called `sportsgoods` instead of the default `mydb` (you can change it on the left panel, **Catalog Tree**).
  + Add a comment to the `onHand` field "Number of units on hand" (later on, this provide a hint to ChatGPT what this field is about; other fields are self-explanatory)
* Using **File**> **Export**> **Foreward Engeer SQL create script** to create and save an SQL script for table and database creation. Note that in the last step, you can use **save to Other file** to save the generated script to `sportsgoods.sql`.
* Execute `sportsgoods.sql` in MySQL workbench to create the database and tables.
* Using **GenAI** (e.g. **Copilot** or **ChatGPT**, free version is fine) to generate the insert data scripts. One prompt could be:

  + *I am going to provide a MySQL database creation script. Can you generate corresponding sample data for each table in the form of insert into SQL statements. Make sure the referential integration of the database is respected.*
  + Then, you can paste the sportsgoods.sql into the chatbot, when prompted.
  + Copy the resulting SQL insert scripts to a SQL file, and execute it to populated the database.
* Test your database with a multi-table query that select all tables and fields (with appropriate join conditions).

  + **Tip**: watch out for duplicate column names.

---

**Submission guidelines**:

* For the first two questions.

  + Type out the appropriate steps and resultant tables in each step, making sure the primary key for each table is properly identified.
* For the 3rd question,

  + paste the **dataqbase table creation** script,
  + the **insert into** scripts,
  + and the **query script and results**.
