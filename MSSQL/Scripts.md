*script* is a file with any number of statements, divided into one or more batches

a *batch* is a sequence of statements executed as a unit

end of a batch is GO command

## Basic commands
Statements that must be the first and only statement in a batch:
	CREATE VIEW
	CREATE TRIGGER
	CREATE PROCEDURE
	CREATE SCHEMA
	CREATE FUNCTION

T-SQL statements to process scripts
	USE
		change which database you're using
	PRINT
		return a message to a client

Commands to control flow of execution
	IF...ELSE - condition
	BEGIN...END - defines a statement block
	WHILE
	BREAK
	CONTINUE
	TRY...CATCH
	GOTO - unconditionally changes flow of execution
	RETURN - exits unconditionally

Other commands
	USE - changes database
	PRINT - returns a message
	DECLARE - local variable
	SET - sets value of local or session variable
	EXEC - executes a dynamic sql statement or stored procedure

USE database

PRINT string_expression

	DECLARE @variable type;
	SET @variable = (value or SELECT statement)

## Variables and Temp tables

**Scalar Variables**
Can only contain a single value, standard data type
starts with @
DECLARE/SET
SELECT with alternate syntax

	SELECT @variable_name_1 = column_spec_1[, ...]

*local variables* - created with DECLARE
scope limited to single batch
cannot be a keyword or object name

**Table Variables**
stores the contents of an entire table
use table data type in the DECLARE statement
define columns and constraints same as in CREATE TABLE
can use variable name instead of table name in UPDATE and DELETE
	cannot in an INTO clause of SELECT INTO
local scope
constraints limited to primary keys, unique keys, and nulls

	USE AP;
	
	DECLARE @BigVendors table
	 (VendorID int, VendorName varchar(50));
	
	INSET @BigVendors
	SELECT VendorID, VendorName
	FROM Vendors
	WHERE VendorID IN
		(SELECT VendorID FROM Invoices WHERE InvoiceTotal > 5000);

	SELECT * FROM @BigVndors;


**Temporary Tables**
Table data stored within a script
good for testing queries against temp data rather than permanent
exists for duration of database session, as long as Query editor is open
	can be referred to in one or more script
	can be deleted with DROP during the session

Begins with \# sign
	local temporary table
	\#\# global temporary table

derived tables are usually more efficient

can't change the schema, only default dbo
name up to 116 characters (standard: 128)

	SELECT TOP 1 VendorID, AVG(InvoiceTotal) as AvgInvaoice
	INTO #TopVendors
	FROM Invoices
	GROUP BY VendorID
	ORDER BY AvgInvoice DESC;

**Five Types of T-SQL Table Objects**

	Standard Table
	View
	Temporary Table
	Table Variable
	Derived Table
	
differences in scope
	standard tables and views have broadest scope
	derived exists only in the statement in which it is defined
	temp and table variables are in between

differences in storage
	standard and temp - disk
	views - disk, but changes here can impact actual tables, unlike others
	table variables and derived tables - memory

## How to control execution of a script

**Conditional Processing**
IF...ELSE
can be nested

	DECLARE @EariestInvoiceDue date;
	SELECT @EarliestInvoiceDue = MIN(InvoiceDueDate)
	FROM Invoices
	WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;
	IF @EarliestInvoiceDue < GETDATE()
		PRINT 'Oustanding invoices overdue!;

If you need to use more than 1 SQL statement, use BEGIN...END block

	IF @EarliestInvoiceDue < GETDATE()
		BEGIN
			PRINT 'Outstanding invoices overdue';
			PRINT '...'
		END;
	ELSE --@EarliestInvoiceDue >= GETDATE()
		PRINT 'No overdue invoices.';

**test for existence of database object**
add IF EXISTS to DROP statement

also could use OBJECT_ID function or DB_ID
	if they don't, returns null, if so, returns index number

	DROP OBJECT_TYPE IF EXISTS object_name;

	USE master;
	IF DB_ID('TestDB') IS NOT NULL
		DROP DATABASE TestDB;

	IF EXISTS (SELECT * FROM sysm.tables where name = 'InvoiceCopy')
		DROP TABLE InvoiceCopy;


**repetitive procssing**

WHILE

BREAK exits loop
CONTINUE causes script to jump to beginning of loop

If you need two or more statements in a while loop, use BEGIN...END


**Use a cursor**

a cursor points to a row in the result set
	declare a cursor - begins just before first row
	use FETCH NEXT to move to the next row and fetch that data
	can only move forward

define the results set for the cursor
use WHILE to process each row in the result set
	can use @@FETCH_STATUS to see if the last fetch was successful

probably better to use an UPDATE statement

	DECLARE cursor_name CURSOR FOR select_statement;
	OPEN cursor_name;
	FETCH NEXT FROM cursor_name INTO @variable1;
	CLOSE cursor_name;
	DEALLOCATE cursor_name;


**How to handle errors**

TRY...CATCH

Doesn't stop everything; some errors are low-priority and just messages
Major errors can cause database connection to be closed

TRY...CATCH must be in a single block, stored procedure, or trigger
can be nested

	BEGIN TRY
		statement block
	END TRY
	BEGIN CATCH
		statement block
		PRINT
		ERROR_NUMBER()
		ERROR_MESSAGE()
		ERROR_SEVERITY()
		ERROR_STATE()
	END CATCH

error handling / exception handling
if there are no errors, the CATCH block is skipped
if an error occurs, control is passed to the CATCH block

**surround-with snippets**

snippet is a template that makes coding certain statements easier
surround-with snippets to enclose a block in a BEGIN...END, IF, or WHILE

select the code you want to enclose
Insert Snippet in query editor
replace any highlighted conditions needed
## Advanced Scripting Techniques

**system functions**
@@IDENTITY - retrieve value of identity column
@@ROWCOUNT - whether something is added correctly

values can be stored in variables
	better to store a variable because the value of the function can change
some can provide value for a DEFAULT constraint on a column

@@ERROR  - error number returned by most recent SQL statement

@@SERVERNAME
@@HOST_NAME
@@SYSTEM_USER

	CREATE TABLE #SysFunctionEx
	 (EntryDBUser varchar(128) DEFAULT SYSTEM_USER);
causes name of the user to be inserted automatically when each new row is added to the table

IDENT_CURRENT('tablename')
	similar to IDENTITY, returns last identity value generated for a table

**change session settings**

ANSI_NULLS
	default ON
	OFF lets you use PaymentDate = NULL rather than IS NULL

SET ROWCOUNT
	limits rows processed by subsequent statements
	default value is 0, which means all rows
	same as TOP when in SELECT
	better to use TOP

SET DATEFORMAT format
	default is mdy
SET NOCOUNT
	whether returns a message of number of rows affected by a statement
SET ANSI_PADDING
	should always be ON

	SET DATEFORMAT ymd;

**Dynamic SQL**

changes from one execution of the script to another
EXEC to execute

create a variable to store the string for the dynamic SQL that is created.
SET assigns beginning of SQL statement to the variable
For each row retrieved by select, the script adds custom parameters


## Review
local variable that can store a single value
	scalar

change to TestDB
	USE TestDB;

execute dynamic SQL
	EXEC

create table variable 
	DECLARE @TestTable table;

series of statements you store in a file
	script

statement to repeatedly execute a statement
	WHILE

System Database that stores temporary table
	tempdb

control flow with true/false
	IF..ELSE

test whether database exists
	IF DB_ID('TestDB') IS NOT NULL

statement to return a message
	PRINT

Utility to execute scripts from command line
	SQLCMD

statement assigns value "test" to a scalar variable named @Name
	SET @Name = 'Test';

script to divide into batches
	GO

return value of most recently assigned identity column
	@@IDENTITY

handle errors
	TRY...CATCH

WHILE @Total + (SELECT TOP 1 InvoiceTotal 
				FROM \#InvoiceCopy
				ORDER BY InvoiceTotal DESC) <= 200000
	When the value of @Total variable plus the largest invoice total in the InvoiceCOpy table becomes greater than 200,000

What can cause the WHILE loop to end other than the expression becoming true?
	If the @InvoiceTotal < 1000

What is the maximum value of the @Total variable?
	200,000

Scope of local variable is limited to
	the batch in which it's defined


DECLARE @Example1 varchar(128);
SET @Example1 = 'Invoices';
What will cause an error?
	SELECT *
	FROM @Example1;
	(it's not a table type)

scope of derived table is limited to
	the statement in which it's defined

scope of a temporary table is
	the session in which it's defined


which can be coded in a batch?
	CREATE TABLE
	(not VIEW, FUNCTION, PROCEDURE)