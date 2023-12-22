SELECT statement within another SQL statement:

WHERE - search condition (subquery predicate)
HAVING - search condition (subquery predicate)
FROM - table specification
SELECT - column specification

- can be *nested*
- single-value subquery can be introduced anywhere as an expression
- single-column subquery used in place of list of values (e.g., with IN)
- table subquery (two or more columns) in a FROM clause
- subquery cannot use ORDER BY unless it has the TOP phrase
- subquery predicates are most common

i
WHERE subqueries can be restated as JOINS
	result of JOIN can include columns from both tables
	result of subquery only has columns from outer query table


## Search Conditions (WHERE and HAVING)

A list of values
	- eg, to get vendors without invoices, use subquery on VendorID in Invoices table in a WHERE VendorID NOT IN clause
	- those VendorIDs get passed to the Vendors table on the outside
	- DISTINCT keyword to return each VendorID only once

WHERE test_expression [NOT] IN (subquery)

Compare with JOIN:
	SELECT columns
	FROM outside table
		LEFT JOIN inside table 
			ON primary=foreign
	WHERE (search condition)

Comparison with an expression
	- subquery must return a single value (aggregate function)
	- or, can have multiple values with SOME ANY or ALL to modify

WHERE expression comparison_operator [SOME ANY ALL] (subquery)
	eg, WHERE invoice total is less than
		(subquery to average the invoices that are greater than 0
			SELECT avg(column)
			FROM inside table column
			WHERE (aggregate search expression)
			)
			returns a single value that can be compared with a column in outside table

ALL
	- condition must be true for all values returned by the subquery
	- can be used with > < = <>
	- if no rows are returned, ALL is always TRUE
	- if all rows returned are NULL, ALL is always FALSE

ANY SOME
	- condition must be true for any one or more
	- can usually be replaced with equivalent condition, eg MAX
	- ANY more commonly used
	- if no rows are returned, ANY is always FALSE
	- if rows returned are NULL, ANY is always FALSE

invoices smaller than the largest invoice for specific vendor
	SELECT columns from outside table and inside table
	FROM outside table
		JOIN inside table
			ON keys
	WHERE outside.column < ANY
		(SELECT inside.column
		FROM inside table
		WHERE VendorID = 115);

## Correlated subqueries




## Common Table Expressions CTE

code CTE as a query beginning with WITH
The CTE can be used in the main SELECT as a Table name

WITH cte_name1 AS 
(
query definition
)
, 
cte_name2 AS 
(
query definitino 1
)
sql_statement

Each CTE and the SQL can refer to CTEs *coded before it*

Can use:
SELECT (most common)
INSERT
UPDATE
DELETE


1 A single value
2 Exists
3 Select
4 nested
5 is executed once for each row in the outer query
6 join
7 a column of one or more values

8
C: Each Vendor in the Top5 Table

9 correlated table expression

10 one row for each vendor that shows the largest balance due, but only if larger than that the average due for all invoices



