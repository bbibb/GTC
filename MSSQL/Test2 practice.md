
### Chapter 5 Exercises

1.
SELECT VendorID, SUM(PaymentTotal) AS PaymentSum
FROM Invoices
GROUP BY VendorID
ORDER BY VendorID;

2.
SELECT TOP 10 VendorName, COUNT(\*) AS InvoiceCount, SUM(PaymentTotal) AS PaymentSum
FROM Vendors v
	JOIN Invoices i
	ON i.VendorID = v.VendorID
GROUP BY VendorName
ORDER BY InvoiceCount;

3.
SELECT VendorName, COUNT(\*) AS InvoiceCount, SUM(InvoiceTotal) AS InvoiceSum
FROM Vendors v
	JOIN Invoices i
	ON i.VendorID = v.VendorID
GROUP BY VendorName
ORDER BY InvoiceCount DESC;


4.
SELECT g.AccountDescription, COUNT(\*) AS LineItemCount,
	SUM(InvoiceLineItemAmount) AS LineItemSum
FROM GLAccounts g
	JOIN InvoiceLineItems i
		ON g.AccountNo = i.AccountNo
WHERE 
GROUP BY g.AccountDescription
HAVING COUNT(\*) > 1
ORDER BY LineItemCount DESC;

5.
SELECT g.AccountDescription, COUNT(\*) AS LineItemCount,
	SUM(InvoiceLineItemAmount) AS LineItemSum
FROM GLAccounts g
	JOIN InvoiceLineItems il
		ON g.AccountNo = i.AccountNo
	JOIN Invoices i
		ON il.InvoiceID = i.InvoiceID
WHERE i.InvoiceDate BETWEEN '2022-10-02' AND '2022-12-31'
GROUP BY g.AccountDescription
HAVING COUNT(\*) > 1
ORDER BY LineItemCount DESC;

6.
SELECT AccountNo, SUM(InvoiceLineItemAmount)
FROM InvoiceLineItems
GROUP BY ROLLUP(AccountNo)
ORDER BY AccountNo DESC;

7.


SELECT VendorName, AccountDescription, COUNT(\*) AS LineItemCount,
	SUM(InvoiceLineItemAmount) AS LineItemSum
FROM Vendors v
	JOIN Invoices i
		ON v.VendorID = i.VendorID
	JOIN InvoiceLineItems ili
		ON ili.InvoiceID = i.InvoiceID
	JOIN GLAccounts g
		ON g.AccountNo = ili.AccountNo
GROUP BY VendorName, AccountDescription
ORDER BY VendorName, AccountDescription;


8.
SELECT VendorName, COUNT(DISTINCT AccountNo) AS AccountNos
FROM Vendors v
	JOIN Invoices i
		ON v.VendorID = i.VendorID
	JOIN InvoiceLineItems ili
		ON ili.InvoiceID = i.InvoiceID
GROUP BY VendorName
HAVING COUNT(DISTINCT AccountNo) > 1
ORDER BY VendorName;

9.

SELECT VendorID, InvoiceDate, InvoiceTotal,
	SUM(InvoiceTotal) OVER (PARTITION BY VendorID) AS VendorTotal,
	COUNT(InvoiceTotal) OVER (PARTITION BY VendorID) AS VendorCount,
	AVG(InvoiceTotal) OVER (PARTITION BY VendorID) AS VendorAvg
FROM Invoices;



### Chapter 6 Exercises

1.
SELECT VendorName
FROM Vendors
WHERE VendorID IN
	(SELECT DISTINCT VendorID
	FROM Invoices)
ORDER BY VendorName;

2.
SELECT InvoiceNumber, InvoiceTotal
FROM Invoices
WHERE PaymentTotal >
	(SELECT AVG(PaymentTotal)
	 FROM Invoices)
ORDER BY InvoiceTotal DESC;

3.
SELECT InvoiceNumber, InvoiceTotal
FROM Invoices
WHERE PaymentTotal > ALL
	(SELECT TOP 50 PERCENT PaymentTotal
	 FROM Invoices
	 WHERE PaymentTotal <> 0
	 ORDER BY PaymentTotal)
ORDER BY InvoiceTotal DESC;

4.

SELECT AccountNo, AccountDescription
FROM GLAccounts gl
WHERE NOT EXISTS
	(SELECT AccountNo
	 FROM InvoiceLineItems li
	 WHERE gl.Accountno = li.AccountNo)
ORDER BY gl.AccountNo;

5.
SELECT VendorName, i.InvoiceID, InvoiceSequence, InvoiceLineItemAmount
FROM Vendors v
	JOIN Invoices i
		ON v.VendorID = i.VendorID
	JOIN InvoiceLineItems li
		ON i.InvoiceID = li.InvoiceID
WHERE i.InvoiceID IN
	(SELECT InvoiceID
	 FROM InvoiceLineItems
	 WHERE InvoiceSequence > 1)
ORDER BY VendorName, i.InvoiceID, InvoiceSequence;


6.

SELECT SUM(InvoiceMax) AS InvoiceSum
FROM (SELECT VendorID, MAX(InvoiceTotal) AS InvoiceMax
	 FROM Invoices
	 WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0
	 GROUP BY VendorID) AS MaxInvoice;


7.
SELECT VendorName, VendorCity, VendorState
FROM Vendors AS v1
WHERE VendorCity + VendorState NOT IN
	(SELECT VendorCity + VendorState
	 FROM Vendors AS v2
	 WHERE v2.VendorID <> v1.VendorID)
ORDER BY VendorState, VendorCity;


8.
SELECT VendorName, InvoiceNumber, InvoiceDate, InvoiceTotal
FROM Invoices i
	JOIN Vendors v
		ON i.VendorID = v.VendorID
WHERE i.InvoiceDate =
	(SELECT MIN(InvoiceDate)
	 FROM Invoices i2
	 WHERE i2.VendorID = i.VendorID)
ORDER BY VendorName;

9.
WITH MaxInvoice AS
(
	SELECT VendorID, MAX(InvoiceTotal) AS InvoiceMax
	FROM Invoices
	WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0
	GROUP BY VendorID
)

SELECT SUM(InvoiceMax) AS InvoiceSum
FROM MaxInvoice;


### Chapter 7

1.
SELECT *
INTO VendorCopy
FROM Vendors;

SELECT *
INTO InvoiceCopy
FROM Invoices;

2.
INSERT INTO InvoiceCopy 
	(VendorID, InvoiceTotal, TermsID, InvoiceNumber)
VALUES 
	(32, 434.58, 2, AX-014)
;


3.
INSERT VendorCopy
SELECT VendorName, VendorAddress1, VendorAddress2,
       VendorCity, VendorState, VendorZipCode,
       VendorPhone, VendorContactLName, VendorContactFName,
       DefaultTermsID, DefaultAccountNo
FROM Vendors
WHERE VendorState <> 'CA';

4.
UPDATE VendorCopy
SET DefaultAccountNo = 403
WHERE DefaultAccountNo = 400;

5.
UPDATE InvoiceCopy
SET PaymentDate = GETDATE(), 
	PaymentTotal = (InvoiceTotal - CreditTotal)
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;

6.
UPDATE InvoiceCopy
SET TermsID = 2
WHERE VendorID IN
	(SELECT VendorID
	 FROM VendorCopy
	 WHERE DefaultTermsID = 2);

7.
UPDATE InvoiceCopy
SET TermsID = 2
FROM Invoices i
	JOIN Vendors v
		on i.VendorID = v.VendorID
WHERE DefaultTermsID = 2;

8.
DELETE VendorCopy
WHERE VendorState = 'MN';

9.
DELETE VendorCopy
WHERE VendorState NOT IN
	(SELECT DISTINCT VendorState
	FROM Vendors v
		JOIN Invoices i
			ON v.VendorID = i.VendorID);
;



### Ch5 quiz
A search condition in the **WHERE** clause is applied before the rows are grouped; condition in the **HAVING** clause isn't applied until after the grouping

When coding a query with 2 columns in the GROUP BY clause, you can insert a summary row for each major group by coding which operator?
	**ROLLUP**
	
Expressing coded in the HAVING clause 
	**can use either aggregate search conditions or non-aggregate search conditions**

SELECT VendorState, COUNT(\*) AS Column 2
FROM Vendors
GROUP BY VendorState
HAVING COUNT(\*)>1;
	**The number of vendors in each state having more than one vendor**

Which aggregate expression gets the number of unique values in the VendorID column?
	**COUNT**(**DISTINCT** **VendorID**)

Which aggregate expression finds the VendorName column that's last in alphabetical order?
	**MAX**(**VendorName**)

By default, all duplicate values are included in an aggregate calculation unless you specify which keyword?
	**DISTINCT**

SELECT VendorID, SUM(InvoiceTotal - PaymentTotal - CreditTotal) AS Column2
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0
GROUP BY VendorID;
	**the total unpaid balance due for each VendorID

These six clauses must be in which order?
	**SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY**

Expressions coded in the WHERE clause
	**can use non-aggregate each conditions, but not aggregate**.


### Ch6 Quiz

If coded as follows, what the subquery return?
WHERE VendorID NOT IN (subquery)
	**a column of one or more values**

Which operator can you use to test whether any rows are returned by a subquery?
	**EXISTS**

SELECT VendorName, COUNT(\*) AS NumberOfInvoices,
      MAX(InvoiceTotal - PaymentTotal - CreditTotal) AS BalanceDue**
FROM Vendors v
 JOIN Invoices i 
   ON v.VendorID = i.VendorID
WHERE InvoiceTotal - PaymentTotal - CreditTotal >
   ******(SELECT AVG(InvoiceTotal - PaymentTotal - CreditTotal)
    FROM Invoices)
GROUP BY VendorName
ORDER BY BalanceDue DESC;
	**one row for each vendor that shows the largest balance due for any of the vendor's invoices, but only if that balance due is larger than the average balance due for all invoices**

A correlated subquery
	**is executed once for each row in the outer query**

If coded as follows, what can the subquery return?
SELECT (Subquery)
	**a single value**

Subqueries can be **nested** within other subqueries

A subquery can sometimes be restated as **a join**


**WITH Top5 AS**
   **(SELECT TOP 5 VendorID, AVG(InvoiceTotal) AS AvgInvoice**
    **FROM Invoices**
    **GROUP BY VendorID**
    **ORDER BY AvgInvoice DESC)**
**SELECT i.VendorID, MAX(i.InvoiceTotal) AS LargestInvoice**
**FROM Invoices i**
 **JOIN Top5**
   **ON i.VendorID = Top5.VendorID**
**GROUP BY i.VendorID**
**ORDER BY LargestInvoice DESC;**
In this query, the table named Top5 is used as part of a _____________
	**a join**

A subquery is a **SELECT** statement that's coded within another SQL statement

**WITH Top5 AS**
   **(SELECT TOP 5 VendorID, AVG(InvoiceTotal) AS AvgInvoice**
    **FROM Invoices**
    **GROUP BY VendorID**
    **ORDER BY AvgInvoice DESC)**
**SELECT i.VendorID, MAX(i.InvoiceTotal) AS LargestInvoice**
**FROM Invoices i**
 **JOIN Top5**
   **ON i.VendorID = Top5.VendorID**
**GROUP BY i.VendorID**
**ORDER BY LargestInvoice DESC;**
When this query is executed, the result table will contain one row for ______
	**each vendor in the Top5 table**



### Chapter 7 quiz

If you omit the WHERE clause from a DELETE statment
	**all rows in the table will be deleted**

Which of the following statements best describes what this INSERT statement does?

**INSERT INTO InvoiceArchive**
**SELECT \*
FROM Invoices**
**WHERE TermsID = 1**

 **adds all of the rows in the Invoices table that have 1 in the TermsID column to the InvoiceArchive table**

When you use the SELECT INTO statement, the result set that's defined by the SELECT statement is **copied into** a new table

Which of the following deletes every row in the Vendors table?
	**DELETE Vendors;**

If you use **calculated values** in the select list of a SELECT INTO statement, you must name the column since that name is used in the definition of the new table.

When you code an UPDATE statement for one or more rows, the SET clause specifies the new data for the specified columns and the **WHERE** clause specifies which rows are to be updated.

In an update statement you can use a **JOIN** in the FROM clause if you need to specify column values or search conditions that depend on data from a table other than the one named in the UPDATE clause.

If you code a column list in an INSERT statement that includes a column that has a default value, which keyword can you code in the VALUES clause to use the default value?
	**DEFAULT**

When coding search conditions, which keyword can you use to create compound search conditions?
	**AND**


**INSERT INTO Invoices**
   **(VendorID, InvoiceNumber, InvoiceTotal, PaymentTotal, CreditTotal,**
   **TermsID, InvoiceDate, InvoiceDueDate)**
**VALUES**
   **(97, '456789', 8344.50, 0, 0, 1, '2023-06-01');**
Problem?
	**the number of items in the column list doesn't match the number in the VALUES list**
	