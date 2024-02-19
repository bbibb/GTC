
A view is a select statement that is stored in the database.
CREATE VIEW
	like a virtual table
	tables listed are the *base tables*
	does not store data itself, always refers back to current data

Use a view - refer to it from another statement

stored as an object, can be used by anyone

CREATE VIEW VendorsMin AS
	SELECT VendorName, VendorState, VendorPhone
	FROM Vendors;

query that uses that view:
	SELECT * FROM VendorsMin
	WHERE VendorState = 'CA'
	ORDER BY VendorName;

benefits:
	design independence
	data security
	flexibility
	simplified queries
	updatability

Views can be nested, where the SELECT statement calls another view
	(up to 32 levels deep)
But, cannot include ORDER BY unless it has TOP, or OFFSET/FETCH
Cannot include the INTO keyword - not permanent

default uses same column names
give names to calculated columns
rename columns from different tables that have the same name
	even if you only need to rename one column, you must include names for all the columns even if they are the same as in the base table
		however, if you let the SELECT statement do the naming, don't need to name everything in the CREATE VIEW


WITH SCHEMABINDING
	prevents data from being changed in a way that damages the view
	can't use * in SELECT
	qualify names of tables and views in FROM with the name of the schema that contains them
WITH CHECK OPTION
	prevents a row from being updated if it would remove it from the view

WITH ENCRYPTION
	keeps users from seeing the SQL code that creates the view

**Updatable View**
modify underlying table with INSERT UPDATE and DELETE
	inflexible and prone to errors - avoid

4 requirements
1. cannot include DISTINCT or TOP
2. cannot include aggregate function such as SUM or AVG
3. cannot include GROUP BY or HAVING
4. cannot include UNION operator

updatable column
	cannot be the result of a calculation

Delete or Modify a view

DROP VIEW

ALTER VIEW

Can delete and then just make a new one, but it also deletes the permissions you may have set on the original.

Before you delete a table you should delete the view beforehand.
	WITH SCHEMABINDING makes you do that

Update Rows through a view

UPDATE can update only one table even if view refers to more

An updated row might not end up in the view afterward.
	you can use WITH CHECK OPTION in CREATE VIEW
	will not let UPDATE do anything that would remove a row from the view

INSERT rows 
	must have all the required values for a new row in the base table.
	can only insert into one table at a time

DELETE operations cascade to the underlying base table

Catalog Views
system catalog lists all objects in a database

SQL server supplies catalog views
	independent of the system tables
	use SELECT
	JOIN to make a view with info from more than one system table


sys.schemas
sys.sequences
sys.tables
sys.views
sys.columns
sys.key_constraints
sys.foreign_keys
sys.foreign_key_columns
sys.objects


## Review

CREATE VIEW VendorName, SUM(InvoiceTotal)
...
ORDER BY VendorName;
	*will fail because ORDER BY isn't allowed in this view*

By default
	columns in a view are given the same names as the columns in the base tables


CREATE VIEW Example2
AS
SELECT InvoiceNumber,
	DATEDIFF(day,InvoiceDate,InvoiceDueDate)
FROM INVOICES;
	*will fail because the second column isn't named*

A view
	is like a virtual table
	consists of rows specified
	doesn't store data itself
	*all of the above*

What can you use to create or modify a view in SSMS?
	View Designer

One way to examine system objects
	*catalog views*

Code views that
	join tables
	summarize data
	use subqueries
	*all of the above*

What is not a benefit of using views
	you can create a view that simplifies data insertion by hiding a complex INSERT statement within the view

Which do you use to select columns in View Designer
	diagram pane

WITH SCHEMABINDING
	protects the view by binding it to database schema
	prevents base tables from being deleted
	prevents base tables from being modified in a way that messes up view
	*all of the above*

DROP VIEW

system objects are stored in a 
	system catalog

SELECT statement for a view
	can use ORDER BY if it also uses TOP

modify an existing view
	ALTER VIEW

table used to create a view is 
	base table

View Designer
	display results of a view
	specify the selection criteria and sort order
	edit the design of a view
	*all of the above*

Example4
	*will fail because the SELECT statemtnt returns two columns named VendorID*

use to view code that is generated for a view in the View Designer
	SQL Pane

WITH CHECK
	prevents an update if it causes a row to no longer be included in the view

A view is a ..... statement that's stored as an object in the database
	SELECT

WITH ENCRPYTION
	prevents users from seeing the code that defines the view
