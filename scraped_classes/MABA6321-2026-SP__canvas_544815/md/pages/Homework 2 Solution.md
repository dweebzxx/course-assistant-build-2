# MABA 6321 Homework 2 - Advanced SQL

### 1. Find the information on `employees` who have other employees reporting to them and show their employee number, last name, first name,, extension, and job title. Make sure the output does not have duplicate rows.

```
SELECT employeeNumber, lastName, firstName, extension, jobTitle
FROM employees
WHERE employeeNumber IN
(SELECT DISTINCT reportsTo FROM employees);

-- 6 row(s) returned

-- # employeeNumber, lastName, firstName, extension, jobTitle
-- 1002, Murphy, Diane, x5800, President
-- 1056, Patterson, Mary, x4611, VP Sales
-- 1143, Bow, Anthony, x5428, Sales Manager (NA)
-- 1102, Bondur, Gerard, x5408, Sale Manager (EMEA)
-- 1088, Patterson, William, x4871, Sales Manager (APAC)
-- 1621, Nishi, Mami, x101, Sales Rep
```

### 2. Using a sub query to find the largest order quantity per order for each product, displaying the product's code, largest order quantity (as `largest_order_quantity`), ordering results from the highest to the lowest.

```
SELECT  distinct p.productCode, p.productName, o.quantityOrdered AS largest_order_quantity
FROM orderdetails AS o JOIN products AS p
USING (productcode)
WHERE o.quantityOrdered = (
    SELECT max(quantityOrdered) 
    FROM orderdetails
    WHERE productcode  = o.productCode
)
ORDER BY o.quantityOrdered desc;

-- 109 row(s) returned

-- # productCode, productName, largest_order_quantity
-- S12_4675, 1969 Dodge Charger, 97
-- S18_3278, 1969 Dodge Super Bee, 90
-- S700_2466, America West Airlines B757-200, 85
-- S700_3167, F/A 18 Hornet 1/72, 77
-- S12_3990, 1970 Plymouth Hemi Cuda, 77
-- S24_3856, 1956 Porsche 356A Coupe, 76
-- S18_1749, 1917 Grand Touring Sedan, 76
-- S24_2766, 1949 Jaguar XK 120, 76
-- S24_2300, 1962 Volkswagen Microbus, 70
-- S10_4698, 2003 Harley-Davidson Eagle Drag Bike, 66
```

### 3. Rewrite the above query using CTE. Then comment on the advantages of the CTE approach relative to the subquery approach, paying attention to the execution speed of the two queries as one aspect of difference.

```
WITH largest_orders as (
    SELECT productcode, max(quantityOrdered) AS largest_order_quantity
    FROM orderdetails
    GROUP BY productcode
) 
SELECT productCode, productName, largest_order_quantity
FROM products JOIN largest_orders USING (productcode)
ORDER BY largest_order_quantity desc;

-- 109 row(s) returned

# productCode, productName, largest_order_quantity
-- S12_4675, 1969 Dodge Charger, 97
-- S18_3278, 1969 Dodge Super Bee, 90
-- S700_2466, America West Airlines B757-200, 85
-- S700_3167, F/A 18 Hornet 1/72, 77
-- S12_3990, 1970 Plymouth Hemi Cuda, 77
-- S24_3856, 1956 Porsche 356A Coupe, 76
-- S18_1749, 1917 Grand Touring Sedan, 76
-- S24_2766, 1949 Jaguar XK 120, 76
-- S24_2300, 1962 Volkswagen Microbus, 70
-- S10_4698, 2003 Harley-Davidson Eagle Drag Bike, 66
```

-- The CTE approach is more readable and is also more computationally efficient since it does not need to compute largest\_order\_quanity over and over again for the same product.

### 4. Use CTE to find out low performing products with each product line, where a product's performance defined as the total sales of a product (a single sale amount is calculated from order details as quantityOrdered\*priceEach), and low performance is defined as below 50% of average total sales across all products in a product line. Display a product's code, name, line, total sales (as `total_sales`), and avg\_sales. Round avg\_sales to two decimal places.

> tip: consider using chained CTEs, first computing each product's total sales, then average total sales.

```
WITH product_sales as (
    SELECT productcode, sum(quantityOrdered*priceEach) AS sales
    FROM orderdetails
    GROUP BY productcode
),    
average_sales AS (
    SELECT productline, round(avg(sales),2) AS avg_sales
    FROM products join product_sales USING (productcode)
    GROUP BY productline
)
SELECT productCode, productName, productLine, sales, avg_sales
FROM products JOIN average_sales USING(productLine)
JOIN product_sales USING(productcode)
WHERE sales < 0.5*avg_sales;

-- 9 row(s) returned

-- # productCode, productName, productLine, sales, avg_sales
-- S18_4933, 1957 Ford Thunderbird, Classic Cars, 50101.57, 104160.07
-- S24_1444, 1970 Dodge Coronet, Classic Cars, 50255.45, 104160.07
-- S24_1628, 1966 Shelby Cobra 427 S/C, Classic Cars, 42015.54, 104160.07
-- S24_1937, 1939 Chevrolet Deluxe Coupe, Vintage Cars, 28052.94, 74898.32
-- S24_2840, 1958 Chevy Corvette Limited Edition, Classic Cars, 31627.96, 104160.07
-- S24_2972, 1982 Lamborghini Diablo, Classic Cars, 30972.87, 104160.07
-- S24_3969, 1936 Mercedes Benz 500k Roadster, Vintage Cars, 29763.39, 74898.32
-- S32_2206, 1982 Ducati 996 R, Motorcycles, 33268.76, 86263.55
-- S32_2509, 1954 Greyhound Scenicruiser, Trucks and Buses, 46519.05, 93101.23

### 5. Find each payment's amount along with the paying customer's cumulative payment up to this date, displaying customer number, payment date, payment amount, and customer_cum_amount, ordering results by customer number and payment date.

```sql
SELECT customerNumber, paymentDate, amount, SUM(amount) OVER (partition by customerNumber ORDER BY paymentDate) AS customer_cum_amount
FROM payments
ORDER BY customerNumber, paymentDate;

-- 273 row(s) returned

-- # customerNumber, paymentDate, amount, customer_cum_amount
-- 103, 2003-06-05 00:00:00, 14571.44, 14571.44
-- 103, 2004-10-19 00:00:00, 6066.78, 20638.22
-- 103, 2004-12-18 00:00:00, 1676.14, 22314.36
-- 112, 2003-06-06 00:00:00, 32641.98, 32641.98
-- 112, 2004-08-20 00:00:00, 33347.88, 65989.86
-- 112, 2004-12-17 00:00:00, 14191.12, 80180.98
-- 114, 2003-05-20 00:00:00, 45864.03, 45864.03
-- 114, 2003-05-31 00:00:00, 7565.08, 53429.11
-- 114, 2004-03-10 00:00:00, 44894.74, 98323.85
-- 114, 2004-12-15 00:00:00, 82261.22, 180585.07
```

### 6. (monthly order cumulative average) Find each order's total amount (computing the total amount from orderDetails), along with the same month's average order amount, showing each order's number, date, customer number, order total, and monthly cumulative average (as `cumulative_average`)

> tip: to obtain the year-month, you may use `left(orderDate, 7)`, treating orderDate as a string.

```
WITH order_totals AS (
    SELECT ordernumber, SUM(quantityOrdered*priceeach) AS order_total
    FROM orderdetails
    GROUP BY ordernumber
) 
SELECT orderNumber, orderDate, customerNumber, order_total, 
AVG(order_total) OVER (PARTITION BY left(orderDate, 7) ORDER BY orderDate, orderNumber) AS cumulative_average
FROM orders JOIN order_totals USING (ordernumber);

-- 326 row(s) returned

-- # orderNumber, orderDate, customerNumber, order_total, cumulative_average
-- 10100, 2003-01-06 00:00:00, 363, 10223.83, 10223.830000
-- 10101, 2003-01-09 00:00:00, 128, 10549.01, 10386.420000
-- 10102, 2003-01-10 00:00:00, 181, 5494.78, 8755.873333
-- 10103, 2003-01-29 00:00:00, 121, 50218.95, 19121.642500
-- 10104, 2003-01-31 00:00:00, 141, 40206.20, 23338.554000
-- 10105, 2003-02-11 00:00:00, 145, 53959.21, 53959.210000
-- 10106, 2003-02-17 00:00:00, 278, 52151.81, 53055.510000
-- 10107, 2003-02-24 00:00:00, 131, 22292.62, 42801.213333
-- 10108, 2003-03-03 00:00:00, 385, 51001.22, 51001.220000
-- 10109, 2003-03-10 00:00:00, 486, 25833.14, 38417.180000
```

### 7. (top 10 orders) Find the top 10 order of all time, displaying the order's number, total amount (as `order_total`), and rank (as `order_rank`).

> tip: since order total must be computed from order details, consider chained CTEs that compute the order totals first, then rank them, then select top 10.

```
WITH order_totals AS (
    SELECT ordernumber, SUM(quantityOrdered*priceeach) AS order_total
    FROM orderdetails
    GROUP BY ordernumber
),
order_ranks AS (
    SELECT orderNumber, order_total, RANK() OVER (ORDER BY order_total DESC) AS order_rank
    FROM order_totals
)
SELECT * 
FROM order_ranks 
WHERE order_rank<=10;

-- 10 row(s) returned

-- # orderNumber, order_total, order_rank
-- 10165, 67392.85, 1
-- 10287, 61402.00, 2
-- 10310, 61234.67, 3
-- 10212, 59830.55, 4
-- 10207, 59265.14, 5
-- 10127, 58841.35, 6
-- 10204, 58793.53, 7
-- 10126, 57131.92, 8
-- 10222, 56822.65, 9
-- 10142, 56052.56, 10
```
