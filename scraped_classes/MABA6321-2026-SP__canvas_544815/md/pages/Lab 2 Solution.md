# MABA 6321 Lab 2 - Intermediate SQL

```
-- -----------------------------------------------------
-- Lab 2 Intermediate SQL 
-- -----------------------------------------------------

-- Problems for Video 1 --------------------------------

-- ##1: show the number and amount (invoice_total) of invoices that receive no payment (i.e. payment_total = 0).
 
SELECT COUNT( * ), SUM( invoice_total )
FROM invoices
WHERE payment_total = 0;

-- # COUNT( * ), SUM( invoice_total )
-- 40, 68196.24
 
-- ##2: count the number of invoices by the type of terms, displaying the count as `no_invoices`

SELECT terms_id, COUNT( * ) AS no_invoices
FROM invoices
GROUP BY terms_id;

-- # terms_id, no_invoices
-- 1, 28
-- 2, 27
-- 3, 38
-- 4, 20
-- 5, 1
 
-- ##3: show the number of invoices and average invoice total per day for days when there are at least two invoices.

SELECT invoice_date, COUNT( * ) AS no_invoices, AVG( invoice_total ) AS avg_invoice_total
FROM invoices
GROUP BY invoice_date
having no_invoices > 1
limit 10;

-- # invoice_date, no_invoices, avg_invoice_total
-- 2024-04-16, 2, 13909.165000
-- 2024-04-17, 2, 1456.100000
-- 2024-04-24, 4, 3146.677500
-- 2024-04-26, 3, 907.206667
-- 2024-04-30, 4, 1039.237500
-- 2024-05-01, 6, 295.893333
-- 2024-05-02, 2, 15.625000
-- 2024-05-07, 2, 5519.730000
-- 2024-05-08, 2, 30741.885000
-- 2024-05-09, 6, 48.275000

-- Problems for Video 2 --------------------------------

-- ##4: using the invoices table, cast invoice numbers to unsigned integers and invoice_date to datetime, show both original values and new values. What happens when the invoice number contains non-numeric characters?
 
SELECT invoice_number, CAST(invoice_number AS UNSIGNED) AS invoice_number_integer ,
invoice_date, CAST(invoice_date AS DATETIME) AS invoice_datetime
FROM invoices
limit 10;

-- # invoice_number, invoice_number_integer, invoice_date, invoice_datetime
-- QP58872, 0, 2024-02-25, 2024-02-25 00:00:00
-- Q545443, 0, 2024-03-14, 2024-03-14 00:00:00
-- P-0608, 0, 2024-04-11, 2024-04-11 00:00:00
-- P-0259, 0, 2024-04-16, 2024-04-16 00:00:00
-- MABO1489, 0, 2024-04-16, 2024-04-16 00:00:00
-- 989319-497, 989319, 2024-04-17, 2024-04-17 00:00:00
-- C73-24, 0, 2024-04-17, 2024-04-17 00:00:00
-- 989319-487, 989319, 2024-04-18, 2024-04-18 00:00:00
-- 989319-477, 989319, 2024-04-19, 2024-04-19 00:00:00
-- 989319-467, 989319, 2024-04-24, 2024-04-24 00:00:00

-- ##5:  Using the vendors table, display the vendor’s name, phone, and area code.

SELECT vendor_name, vendor_phone, SUBSTR(vendor_phone,2,3) AS area_code
FROM vendors
limit 10;

-- # vendor_name, vendor_phone, area_code
-- US Postal Service, (800) 555-1205, 800
-- National Information Data Ctr, (301) 555-8950, 301
-- Register of Copyrights, , 
-- Jobtrak, (800) 555-8725, 800
-- Newbrige Book Clubs, (800) 555-9980, 800
-- California Chamber Of Commerce, (916) 555-6670, 916
-- Towne Advertiser's Mailing Svcs, , 
-- BFI Industries, (559) 555-1551, 559
-- Pacific Gas & Electric, (800) 555-6081, 800
-- Robbins Mobile Lock And Key, (559) 555-9375, 559
 
-- ##6: Using invoices table, find out invoices whose invoice_date are within 60 days of 2024-04-01. show invoice_id and invoice_date.

SELECT invoice_id, invoice_date FROM invoices 
WHERE invoice_date BETWEEN '2024-04-01' AND DATE_ADD('2024-04-01', INTERVAL 60 DAY)
limit 10;

-- # invoice_id, invoice_date
-- 3, 2024-04-11
-- 4, 2024-04-16
-- 5, 2024-04-16
-- 6, 2024-04-17
-- 7, 2024-04-17
-- 8, 2024-04-18
-- 9, 2024-04-19
-- 10, 2024-04-24
-- 11, 2024-04-24
-- 12, 2024-04-24

-- ##7:  Show invoice_id and payment_status which is "no payment" if the payment date is NULL and "has payment", otherwise.
 
SELECT invoice_id, if(payment_date is null, "no payment","has payments") as  payment_status
FROM invoices
limit 10;

-- # invoice_id, payment_status
-- 1, has payments
-- 2, has payments
-- 3, no payment
-- 4, has payments
-- 5, has payments
-- 6, no payment
-- 7, has payments
-- 8, no payment
-- 9, has payments
-- 10, has payments

-- ##8:  Show invoice id, terms_id, and term (e.g. due in 10 days, due in 20 days, etc) by the decending order of invoice_id.
SELECT invoice_id, terms_id, 
case terms_id when 1 then "due in 10 days" 
when 2 then "due in 20 days" 
when 3 then "due in 30 days" 
when 4 then "due in 60 days" 
when 5 then "due in 90 days"
else "unknown terms"
end as term
FROM invoices
order by invoice_id desc
limit 10;

-- # invoice_id, terms_id, term
-- 114, 2, due in 20 days
-- 113, 3, due in 30 days
-- 112, 3, due in 30 days
-- 111, 3, due in 30 days
-- 110, 3, due in 30 days
-- 109, 3, due in 30 days
-- 108, 1, due in 10 days
-- 107, 1, due in 10 days
-- 106, 2, due in 20 days
-- 105, 3, due in 30 days

-- Problems for Video 3 --------------------------------

-- ##9: find out invoice numbers (in invoices table), terms_id, and their term descriptions (in terms table)

SELECT invoice_number, invoices.terms_id, terms_description
FROM invoices
INNER JOIN terms 
	ON invoices.terms_id = terms.terms_id
limit 10;

-- # invoice_number, terms_id, terms_description
-- 989319-427, 1, Net due 10 days
-- 989319-417, 1, Net due 10 days
-- 97/465, 1, Net due 10 days
-- 4-314-3057, 1, Net due 10 days
-- 2-000-2993, 1, Net due 10 days
-- 1-202-2978, 1, Net due 10 days
-- 1-200-5164, 1, Net due 10 days
-- 21-4923721, 1, Net due 10 days
-- 963253240, 1, Net due 10 days
-- 963253239, 1, Net due 10 days
   

-- ##10: Rewrite the above query using `using`
SELECT invoice_number, terms_id, terms_description
FROM invoices
INNER JOIN terms 
	using (terms_id)
limit 10;

-- # invoice_number, terms_id, terms_description
-- 989319-427, 1, Net due 10 days
-- 989319-417, 1, Net due 10 days
-- 97/465, 1, Net due 10 days
-- 4-314-3057, 1, Net due 10 days
-- 2-000-2993, 1, Net due 10 days
-- 1-202-2978, 1, Net due 10 days
-- 1-200-5164, 1, Net due 10 days
-- 21-4923721, 1, Net due 10 days
-- 963253240, 1, Net due 10 days
-- 963253239, 1, Net due 10 days

-- ##11: Find pairs of vendors that share the same default account number. show vendor names and their shared account. Order results by vendor name.
SELECT v1.vendor_name AS vendor1, v1.default_account_number, v2.vendor_name AS vendor2
FROM vendors v1
JOIN vendors v2 USING ( default_account_number ) 
WHERE v1.vendor_name < v2.vendor_name
ORDER BY v1.vendor_name;

-- 517 row(s) returned

-- # vendor1, default_account_number, vendor2
-- American Booksellers Assoc, 574, City Of Fresno
-- American Booksellers Assoc, 574, Fresno County Tax Collector
-- American Express, 160, Micro Center
-- American Express, 160, IBM
-- American Express, 160, Wang Laboratories, Inc.
-- American Express, 160, Wells Fargo Bank
-- Ascom Hasler Mailing Systems, 532, Yale Industrial Trucks-Fresno
-- Ascom Hasler Mailing Systems, 532, RR Bowker
-- Ascom Hasler Mailing Systems, 532, Graylift
-- Ascom Hasler Mailing Systems, 532, Frank E Wilber Co

-- note:  in the above we used the WHERE clause to avoid listing identical vendors as a pair.  

-- Problems for Video 4 --------------------------------

-- the following questions use the `department` database.

-- ##12: Using employees and departments, find employees' departments, show employee names and their department names. If the employee's department is not in departments table, show NULL for the department name.
SELECT last_name, first_name, department_name
FROM employees
LEFT JOIN departments
USING ( department_number ) ;

-- # last_name, first_name, department_name
-- Smith, Cindy, Payroll
-- Jones, Elmer, Personnel
-- Simonian, Ralph, Payroll
-- Hernandez, Olivia, Accounting
-- Aaronsen, Robert, Payroll
-- Watson, Denise, 
-- Hardy, Thomas, Maintenance
-- O'Leary, Rhea, Personnel
-- Locario, Paulo, 

-- ##13: Find the assignment between projects and employees, allowing projects without employees and employees without projects. Show project number, employee id, and employee name
(
SELECT project_number, p.employee_id, last_name, first_name
FROM  `employees` AS e
LEFT JOIN projects AS p
USING ( employee_id )
)
UNION (
SELECT project_number, p.employee_id, last_name, first_name
FROM projects AS p
LEFT JOIN  `employees` AS e
USING ( employee_id )
);

-- # project_number, employee_id, last_name, first_name
-- P1012, 1, Smith, Cindy
-- , , Jones, Elmer
-- P1012, 3, Simonian, Ralph
-- P1011, 4, Hernandez, Olivia
-- P1012, 5, Aaronsen, Robert
-- P1013, 6, Watson, Denise
-- , , Hardy, Thomas
-- P1011, 8, O'Leary, Rhea
-- P1013, 9, Locario, Paulo
-- P1014, 10, ,
```
