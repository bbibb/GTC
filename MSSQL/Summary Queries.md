Chapter 5


Aggregate Functions
	operate on a series of values and return a single summary value 
	- SCALAR AGGREGATE
	aka column functions - operate on all values in a column

Summary query
	SELECT statement
	contains one or more aggregate function

Operate on an expression
ALL or DISTINCT keywords
	mostly you only use DISTINCT with COUNT
null values always excluded

AVG - avg of nonnull values
SUM - total of nonnull values
MIN - lowest
max - highest
COUNT - number
COUNT(\*)  - number of rows selected by the query
	don't use DISTINCT, ALL, or an expression

MIN MAX COUNT
	result in numeric, date, or string value

SELECT COUNT(\*) AS NumberOfInvoices
	SUM(InvoiceTotal - PaymentTotal - CreditTotal)
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;

SELECT with an aggregate function can only contain aggregate functions
	except:
	if the column specification results in a literal value
	if the query includes GROUP BY
	If the functions include OVER

If you want to count all selected rows, use COUNT(\*)

Use COUNT(DISTINCT column) to count rows with a unique value

### Group and Summarize

GROUP BY
	how the selected rows are grouped
HAVING
	determines which groups are included in final results

WHERE applies before grouping
ORDER BY applied after

a single row is returned for each unique set of values in the GROUP BY

AVG with GROUP BY
	calculates the average for each group rather than for total set
	- VECTOR AGGREGATE

HAVING
	applied after rows are grouped and AVG calculated

GROUP BY columns do NOT have to be in the SELECT clause

SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY

	SELECT VendorID, AVG(InvoiceTotal) AS Average InvoiceAmount
	FROM Invoices
	GROUP BY VendorID
	HAVING AVG(InvoiceTotal) > 2000
	ORDER BY Average InvoiceAmount DESC;

**When a SELECT statement has GROUP BY, the SELECT clause can have:
	aggregate functions
	columns used for grouping
	expressions that result in a constant value**

Count the number of invoices by Vendor
	SELECT VendorID, COUNT(\*) AS InvoiceQty
	FROM Invoices
	GROUP BY VendorID;

Count with average
	SELECT VendorState, VendorCity, Count(\*) AS InvoiceQty, 
		AVG(InvoiceTotal) AS InvoiceAvg
	FROM Invoices i
		JOIN Vendors v
			ON i.VendorID = v. VendorID
	GROUP BY VendorState, VendorCity
	ORDER BY VendorState, VendorCity
		(number of invoices + average amt for vendors in each state/city)

Add HAVING COUNT(\*) >=2
	to limit to cities with 2 or more invoices


### Having vs WHERE

HAVING filters the summarized result set defined by SELECT FROM WHERE GROUPBY
HAVING can have aggregate function, not WHERE
HAVING can only refer to columns that are in the SELECT or GROUP BY

AND and OR just like in WHERE
aggregate function must be in HAVING
can put everything in HAVING or split with WHERE

### Extensions

ROLLUP
	add one or more summary rows to a result set with grouping and aggregates
	added at the end

When you group by 2 columns, ROLLUP  adds a summary for each of the col1 groups

	SELECT VendorID, COUNT(*) AS InvoiceCount,
		SUM(InvoiceTotal) AS InvoiceTotal
	FROM Invoices
	GROUP BY ROLLUP(VendorID);

	  could also say GROUP BY VendorID WITH ROLLUP

With ROLLUP, you cannot use DISTINCT



CUBE
	adds summary rows for each combination of groups
	with one column, just like ROLLUP
	with 2 or more, summary row for each of the groups in each grouping row

	GROUP BY VenderState, VendorCity WITH CUBE

GROUPING SETS

only includes summary rows
adds summary rows for each specified group

can create composite groups of multiple columns

you can use ROLLUP and CUBE with a composite group
	code ROLLUP or CUBE before a composite group

	SELECT VendorState, VendorCity, VendorZipCode, COUNT (*) AS QtyVendors
	FROM Vendors
	WHERE VendorState in ('IA, 'NJ')
	GROUP BY GROUPING SETS ((VendorState, VendorCity), VendorZipCode, ())

	The empty set of parentheses summarizes the entire result set


OVER clause

return the individual rows used to calculate summaries, with the summary

OVER after the aggregate function, with parentheses
	in parentheses, you can PARTITION BY or ORDER BY or both

(PARTITION BY is like GROUP BY but it isn't combining)

with ORDER BY you can show summaries accumulating for each row, eg
	cumulative total
	running average
use both, get cumulative total for each section


Group summary data by date:

	SELECT InvoiceNumber, InvoiceDate, InvoiceTotal,
		SUM(InvoiceTotal) OVER (PARTITION BY InvoiceDate) AS DateTotal
		COUNT(InvoiceTotal) OVER (PARTITION BY InvoiceDate) AS DateCount
		AVG(InvoiceTotal) OVER (PARTITION BY InvoiceDate) AS DateAvg
	FROM Invoices;


cumulative total and moving average:

	SELECT InvoiceNumber, InvoiceDate, InvoiceTotal,
		SUM(InvoiceTotal) OVER (ORDER BY InvoiceDate) AS DateTotal
		COUNT(InvoiceTotal) OVER (ORDER BY InvoiceDate) AS DateCount
		AVG(InvoiceTotal) OVER (ORDER BY InvoiceDate) AS DateAvg
	FROM Invoices;




