
### Make a copy

	SELECT select_list
	INTO table_name
	FROM table_source
	[WHERE search_condition]
	[GROUP BY group_by_list]
	[HAVING search_condition]
	[ORDER BY order_by_list]

complete copy
SELECT *
INTO InvoiceCopy
FROM Invoices;

partial copy
SELECT *
INTO OldInvoices
FROM Invoices
WHERE InvoiceTotal-PaymentTotal-CreditTotal = 0;

summary rows
SELECT VendorID, SUM(InvoiceTotal) AS SumOfInvoices
INTO VendorBalances
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal <> 0
GROUP BY VendorID;

drop
DROP TABLE InvoiceCopy;


### Insert rows

	INSERT INTO table_name [column_list]
	[DEFAULT] VALUES (expressions);

INSERT INTO Invoices
VALUES 
	(v1, v2, v3, v4, v5, 0, 0, NULL),
	(v1, v2, v3, v4, v5, v6, NULL, 9);

with column list
INSERT INTO Invoices
	(Col1, Col2, Col3, Col4, Col5)
VALUES
	(v1, v2, v3, v4, v5);


### Default and NULL values

DEFAULT keyword means that default values are used in every column with a default value, and all others will get NULL
	except Identity column
	only use when all columns are default, null, or identity

NULL keyword assigns null to that column

In a column list, if you omit columns with default or NULL values, those will be assigned automatically


### insert rows from another table

	INSERT INTO table
	SELECT column list
	FROM table source
	WHERE search condition

use SELECT instead of VALUES

you can use SELECT * but all of the columns have to match

Better to list the columns in the INSERT INTO and SELECT statements


### Update

	UPDATE table name
	SET columnName = expression
	[FROM table source AS alias]
	WHERE search condition

updates columns of a specific row
UPDATE Invoices
SET PaymentDate = date, PaymentTotal = total
WHERE InvoiceNumber = number;

set new value to column for multiple rows
UPDATE Invoices
SET TermsID = 1
WHERE VendorID = num;

math expression
UPDATE Invoices
SET Credit = Credit + 100
WHERE InvoiceNumber = num;

can't update an identity column
if you omit the WHERE, all rows will be updated with the SET value

### Subqueries

UPDATE Invoices
SET TermsID = 1
WHERE VendorID = 
	(SELECT VendorID
	FROM Vendors
	WHERE VendorName = 'name');

code suquery in SET, FROM, or WHERE of an UPDATE statement
	in SET -> return a value that's assigned to a column
	in FROM -> to identify rows to update, new derived table
	in WHERE -> to provide one or more values for the search condition

### Joins

UPDATE Invoices
SET TermsID = 1
FROM Invoices i
	JOIN Vendors v
		ON i.VendorID = v.VendorID
WHERE VendorName = 'name';

Use JOIN if you need to specify column values or search conditions that depend on data in another table

You can use columns from the joined tables to assign values in the SET clause or in the search condition of WHERE


### Delete Rows

WHERE search clause:
	identify rows to be deleted
If you don't ALL ROWS will be deleted!

Can include FROM in DELETE
JOIN additional tables
	then search with WHERE

DELETE table_name
[FROM table_source]
WHERE search condition;

DELETE Invoices
WHERE InvoiceID = 115;

DELETE Invoices;

DELETE INVOICES
WHERE InvoiceTotal - PaymentTotal = 0;

### Subqueries and Joins in DELETE

DELETE tablename
WHERE VendorID = 
	(SELECT column
	 FROM insidetable
	 WHERE search condition);

DELETE tablename
FROM tablename t1
	JOIN table2 t2
		ON t1.pk = t2.fk
WHERE search condition;

DELETE vendors that don't have invoices
	DELETE Vendors
	WHERE VendorID NOT IN
		(SELECT DISTINCT VendorID FROM Invoices);

Subqueries in WHERE -> find one or more values used in the search condition

Use any column returned by a subquery or join in the WHERE

FROM -> use subqueries and joins to access data in other tables than the one in the initial DELETE clause


### Merge rows

updating + inserting = upsert

MERGE INTO target table
USING source table
ON condition that is used to join
WHEN MATCHED when a row in inserted, updated, or deleted
	use table aliases
	THEN dml statement
WHEN NOT MATCHED [BY TARGET]
	THEN dml statement
WHEN NOT MATCHED BY SOURCE
	THEN dml statement

; required ending


AND to get compound conditions


MERGE INTO InvoiceArchive AS ai
USING Invoices as ic
ON ic.InvoiceID = ia.InvoiceID
WHEN MATCHED AND
	ia.PaymentDate IS NOT NULLL
	ic.PaymentTotal > ia.PaymentTotal
	THEN
	UPDATE SET
		ia.PaymentTotal = ic.PaymentTotal
		ia.CreditTotal = ic.CreditTotal
		ia.PaymentDate = ic.PaymentDate
WHEN NOT MATCHED
	THEN
	INSERT (InvoiceID, VendorID, InvoiceNumber...)
	VALUES (ic.InvoiceID, ic.VendorID, ic.InvoiceNumber...)
;






