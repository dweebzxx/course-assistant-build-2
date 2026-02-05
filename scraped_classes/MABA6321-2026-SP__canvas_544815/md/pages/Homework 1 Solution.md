# MABA 6321 Homework 1 - SQL (solution)

## Part 1: Short Answers

1. Explain the following concepts in one or two sentences.

* **DBMS**: refers to a general-purpose software system that facilitates the processes of defining, creating, using and maintaining databases
* **Primary Key**: A primary key is a column or a set of columns in a database table that uniquely identifies each row in that table.
* **Foreign Key**: is a field (or a set of fields) in one table that refers to the primary key in another table. It creates a relationship between two tables and enforces referential integrity.
* **DML**: are SQL commands that maintain and query a database
* **DDL**: are SQL commands that define a database, including creating, altering, and dropping tables and establishing constraints
* **Outer JOIN**: is a type of SQL join that returns matched rows from two tables along with the unmatched rows from one or both tables, filling in missing values with NULLs.

## Part 2: Hands On

```
-- ### 1. Find users from "New York", ordering results by `creationDate` and display only their id, display name, and location. Note that you should include cases such as "New York ...", "... New York", and "... New York ..." 

select id, displayname, location from users 
where location like "%New York%" 
order by creationdate;

-- 21 row(s) returned

-- # id, displayname, location
-- 5, Kasra Rahjerdi, New York, United States
-- 6, Kevin Montrose, New York City, New York
-- 8, David Fullerton, New York, NY
-- 82, Anna Lear, New York, NY
-- 107, Jeni, New York, United States
-- 113, SamtheBrand, New York, United States
-- 118, zompz, New York, NY
-- 120, Max, New York, United States
-- 122, Laura, New York, United States
-- 123, Abby T. Miller, New York, NY

-- ### 2. We know that both questions and answers are stored in the `posts` table. We wonder how many types are there in the posts table? Order results by post type ID. 

SELECT distinct PostTypeId FROM posts
ORDER BY PostTypeID;

-- 4 row(s) returned

-- # PostTypeId
-- 1
-- 2
-- 4
-- 5

-- ### 3.  Continuing with the previous query, find out the count of each Post Type, ordering results from the highest to the lowest count. The column header for count must be "count" and the column header for `PostTypeID` should be "Post Type ID". 

-- > Hint: `count` is a reserved word in SQL. 

SELECT PostTypeId as `Post Type ID`, 
    COUNT(*) AS `count` FROM posts
GROUP BY PostTypeId 
ORDER BY `count` desc;

-- 4 row(s) returned

-- # Post Type ID, count
-- 2, 1585
-- 1, 947
-- 5, 168
-- 4, 168

-- ### 4. If a question owner is satisified with one of the answers, he/she can mark the answer as an Accepted Answer (The answer's post id saved in `AcceptedAnswerID` field of the posts table). Show all the question posts on or after May 1, 2024 that DO NOT yet have an Accepted Answer, displaying the posts' id, type ID, creation date, owner user id, and title. 

Select id, posttypeid, creationdate, owneruserid, title
from posts 
where posttypeid=1 
    and AcceptedAnswerId is null 
    and creationdate >= "2024-05-01";

-- 6 row(s) returned

-- # id, posttypeid, creationdate, owneruserid, title
-- 3083, 1, 2024-05-01 22:46:56, 1290, Leg injury confusing the vet
-- 3087, 1, 2024-05-02 21:14:22, 1299, Why do my clothes smell like dog after laying in the wardrobe for so long?
-- 3088, 1, 2024-05-02 22:56:39, 165, What to do when a cat is in "attack mode"
-- 3091, 1, 2024-05-03 12:00:19, 1301, Is there a breed of rabbit that doesn't grow more than the size of a hand?
-- 3093, 1, 2024-05-03 14:04:38, 1166, Can dogs get head lice and transfer them to humans (or vice versa)?
-- 3095, 1, 2024-05-03 17:22:37, 1302, Do miniature cows with cat like agility exist?

-- ### 5. Show all the Answer posts in January 2024, ordering results by creation date and display the answer posts' ID, post type ID, creation date, and a trucated version of the answer body (the first 50 characters) as `body`. 

-- Hint: `Left(string_value, x)` returns the first x characters of the string_value

SELECT id, posttypeid, creationdate, 
    left(body,50) as body FROM posts 
WHERE postTypeid=2 and
    creationdate BETWEEN "2024-01-01" AND "2024-01-31"
ORDER BY CreationDate;

-- 150 row(s) returned

-- # id, posttypeid, creationdate, body
-- 1837, 2, 2024-01-01 12:10:37, <p><strong>Explanation:</strong></p><p>It is lik
-- 1838, 2, 2024-01-02 15:20:43, <p>I hold the opinion that people need to train th
-- 1839, 2, 2024-01-02 16:16:10, <p>Kittens need to stay in with their mother for 1
-- 1841, 2, 2024-01-02 18:02:19, <p>It depends on the kitten, but a good guideline 
-- 1845, 2, 2024-01-03 08:37:28, <p><strong>tl;dr version:</strong> Any combination
-- 1846, 2, 2024-01-03 11:15:02, <p>Unless you've directly observed one cat bullyin
-- 1847, 2, 2024-01-03 11:20:51, <p>Add a second litter box to the house.  </p><p
-- 1850, 2, 2024-01-03 14:11:34, <p>I'm going to make some assumptions here - that 
-- 1851, 2, 2024-01-03 14:16:05, <p>I've been told by vets that the most appropriat
-- 1852, 2, 2024-01-03 17:24:12, <p>The answer occurred to me the other day. No, I 

-- ### 6. For each Answer post with 25 or higher scores, displaying their vote count for each type of votes, along with the post's id, title, and first 50 characters of their body.

SELECT p.id, title, left(body, 50) as body, 
    votetypeid, COUNT(*) AS vote_count
FROM posts AS p JOIN votes as v ON p.Id = v.PostId
WHERE score>=25 and votetypeid=2
GROUP BY p.id, title, score, votetypeid
order by score desc;

-- 15 row(s) returned

-- # id, title, body, votetypeid, vote_count
-- 120, Why does my cat keep patting my face?, <p>My cat has a habit of randomly patting my face , 2, 35
-- 519, How much purring is too much purring?, <p>I have an adolescent cat that I adopted as a ki, 2, 32
-- 2725, How do I get my cat to wear a tuxedo for several hours?, <p>My cat is quite dapper and handsome, so when we, 2, 31
-- 1001, Who should win at tug of war?, <p>I love playing tug of war with my dog.  This is, 2, 30
-- 490, , <p>Declawing is considered a last option before ha, 2, 29
-- 559, , <p>My dogs also scoot, which indicates it is time , 2, 29
-- 1, What causes a dog to lunge at an unknown child and how should the owner respond?, <p>I have a 2.5 year old pitbull/boxer mix.  He is, 2, 28
-- 14, Can cats safely eat raw meat?, <p>Is it safe to feed my cat raw meat, or should w, 2, 28
-- 67, How should I discipline my cat for bad behavior?, <p>There are a couple of things that I try and pre, 2, 28
-- 247, , <p>This is one way cats show affection or try to g, 2, 28

-- ##7. Find each customer's last payment date. A customer must be shown even if the customer does not have any payment. Show `customernumber`, `customername`, and last payment date (as "last_pay_date"). Order results by `customername`. 

SELECT c.customernumber, customername, MAX(paymentdate) AS last_pay_date
FROM customers AS c
LEFT JOIN payments AS p ON c.customernumber = p.customernumber
GROUP BY c.customernumber
ORDER BY customername;

-- 122 row(s) returned

-- # customernumber, customername, last_pay_date
-- 242, Alpha Cognac, 2005-06-03 00:00:00
-- 168, American Souvenirs Inc, 
-- 249, Amica Models & Co., 2004-09-19 00:00:00
-- 237, ANG Resellers, 
-- 276, Anna's Decorations, Ltd, 2005-04-30 00:00:00
-- 465, Anton Designs, Ltd., 
-- 206, Asian Shopping Network, Co, 
-- 348, Asian Treasures, Inc., 
-- 103, Atelier graphique, 2004-12-18 00:00:00
-- 471, Australian Collectables, Ltd, 2004-07-28 00:00:00

-- ### 8.  Write an `INSERT INTO` statement(s) to enter the following four entries into the `orderdetails` table.

-- A customer places the following two orders numbered 30 and 31 respectively.

-- |**Order Number** | **Product Code** | **quantity** | **unit price** | **Order line number** |
-- | -| -| -| -| -|
-- | 30 | S18_4600 | 20 | $79.99 | 1 |
-- | 30 | S700_1938 | 5 | $50.00 | 2 |
-- | 30 | S700_3962 | 15 | $65.00 | 3 |
-- | 30 | S24_4258 | 20 | $75.00 | 4 |

Insert into orders (orderNumber, orderDate, 
    requiredDate, status, customerNumber)
values (30, "2025-05-31", "2025-06-07", "In Process", 114);

-- 1 row(s) affected

INSERT INTO orderdetails
VALUES ( 30, 'S18_4600', 20, 79.99, 1 ) , ( 30, 'S700_1938', 5, 50, 2 ) ,
 ( 30, 'S700_3962', 15, 65, 3 ), ( 30, 'S24_4258', 20, 75, 4) ;

 -- 4 rows affected

-- Alternatively, one can insert into `orderdetails` line by line:

INSERT INTO orderdetails VALUES ( 30, 'S18_4600', 20, 79.99, 1 );
INSERT INTO orderdetails VALUES ( 30, 'S700_1938', 5, 50, 2 ) ;
INSERT INTO orderdetails VALUES ( 30, 'S700_3962', 15, 65, 3 );
INSERT INTO orderdetails VALUES ( 31, 'S24_4258', 20, 75, 4);

-- 4 rows affected

-- ### 9. Write an update statement to update the line 1 of order 30 to increase the price for this item by 5. 

UPDATE orderdetails SET priceEach = priceEach + 5
WHERE orderNumber = 30 AND orderlinenumber = 1;
-- 1 rows affected.

-- ### 10. Delete the order line(s) for order 30 in `orderdetails` and the order 30 in orders.

DELETE from orderdetails 
WHERE ordernumber=30;

-- 4 row(s) affected

DELETE from orders 
WHERE ordernumber=30;

-- 1 row(s) affected
```
