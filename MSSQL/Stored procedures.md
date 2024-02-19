
of 4 ways to store procedures, only scripts can have multiple batches
	stored in files outside database

Other three are database objects
	stored procedures
		run in a statement
		can use parameters
		good to let other users run complex code
	user-defined functions
		run in a statement
		used more often
		can use parameters
	triggers
		run automatically in response to action query
		used more often
		do not use parameters
		used like constraints to prevent errors, but more flexibility

created with DDL statements, remain in database until dropped

**Code Stored Procedures**

also called a sproc or procedure

CREATE PROC procedureName AS
	statements

Call with EXEC procedureName

first time it is run, sql creates an execution plan
	compiled procedure stored in database

user doesn't need to know the structure of the database

allow a user or program to call certain procedures but not any other SQL statements
	restricts access to rows and columns accessed only through the sproc
	**use this for access control in PHP project?**


name cannot be the name of any other object in the database
	prefix with 'sp'

CREATE PROC must be the first and only statement in the batch.
	(follows a GO statement in a script)

*temporary sproc*
	stored in tempdb
	only while session is open
	prefix with \# for local and \#\# for global

optional
	WITH RECOMPILE - don't precompile
	WITH ENCRYPTION - can't view the declaration of the stored procedure
	WITH EXECUTE_AS - allow users to execute with specific security setting


**Work with parameters**

input parameters - passed to stored procedure
	value required or no
	required = must be passed from calling program or error occurs
	optional
		assign default value, used if one isn't passed
	list required first then optional
output parameters - returned to calling program
	OUTPUT

@parameter_name data_type \[= default_value\]  \[output\]

@DateVar date
@VendorVar varchar(40) = NULL
	
	CREATE PROC spInvTotal1
		@DateVar date,
		@InvTotal money OUTPUT
	AS
	SELECT @InvTotal = SUM(InvoiceTotal)
	FROM Invoices
	WHERE InvoiceDate >= @DateVar;


**Call sproc w/parameters**

code values in EXEC statement
pass values either by position or by name
	position - listed in order, no names
	most common

	DECLARE @MyInvTotal money;
	EXEC spInvTotal3 @MyInvTotal OUTPUT, '2023-01-01', 'p%';



**return values**

default value is zero
RETURN statement - single integers

when return value and when output parameter?
	RETURN for single integer value output
	but if there are multiples or any other type of data, use output

**validate data and raise errors**

check data before you use it
	data validation
	return error with a THROW statement
	calling program can then handle with TRY...CATCH

THROW [error_number, message, state]

	CREATE PROC spInsertInvoice
		(columns...)
	AS

	IF EXISTS(SELECT * FROM Vendors WHERE VendorID = @VendorID)
		INSERT INVOICES
		VALUES (values...);
	ELSE
		THROW 50001, 'Not a valid *VendorID', 1;

use it:

	BEGIN TRY
		EXEC spInsertInvoice
			..values..;
	END TRY
	BEGIN CATCH
		PRINT ..error message..
		IF ERROR_NUMBER >= 50000
			PRINT ..custom message..
	END CATCH


**sproc for insert operations**

validate data in a new invoice:
IF statements to validate data in each row
	if invalid, THROW and terminate

testing before the INSERT lets you avoid system errors, don't need to use CONSTRAINTS to catch it

if everything passes, INSERT
then return the new InvoiceID generated to the calling program

**pass a table as a parameter**
so far we've only seen scalar values as parameters

multiple invoices, eg?
	custom data type - "user defined table type"
	can't use foreign keys

CREATE TYPE

Then, CREATE PROC that accepts a single parameter of your custom type
	the body can treat the table as a table variable

must use READONLY
can use a JOIN

	CREATE TYPE TableTypeName AS
	TABLE
	table_definition

**Delete or change stored procedure**

DROP PROC
	delete one ore more stored procedures
	
ALTER PROC
	redefine existing stored procedure
	completely replaces it, like ALTER VIEW
	better to just delete and make a new one
	unless you need to maintain permissions

If you delete a table or view used by a sproc, you should delete the sproc also
	it could still be called and be an error

**system stored procedures**

hundreds
use to help with admin tasks, but don't use in applications
change with new versions

create own system sproc
	start with sp_
	create in master database

sp_Help [name]
	info about database object or data type
sp_HelpText name
	text of unencrypted sproc, user defined function, trigger, or view
sp_HelpDb [database_name]
	info about the database
sp_Who [login_ID]
	logged in user and processes
sp_Columns name
	columns defined in a table or view


	USE AP;
	EXEC sp_HelpText spInvoiceReport;



## Review

Which of the following statements calls the following stored procedure, passes the value ‘2019-10-01’ to its input parameter, and stores the value of its output parameter in a variable named @MyInvoiceTotal?

	EXEC spInvoiceTotal2 '2019-10-01', @MyInvoiceTotal OUTPUT;

System Stored procedures 
	ALL
		perform standard tasks on the current databse
		are stored in the Master database
		can change with each version of SQL server

You can store procedural code in
	ALL
		scripts
		stored procedures
		user-defined functions

Which of the following returns the value of a variable @InvoiceCount
	RETURN @InvoiceCount

Which of the following statements executes a stored procedure named spInvoiceCount and stores its return value in a variable named @InvoiceCount?
	EXEC @InvoiceCount = spInvoiceCount

statement to manually raise an error in a sproc
	THROW (formerly RAISEERROR)


if you delete and then create it again
	you delete the security permissions assigned to the object

to make a parameter for a sproc optional
	code a default value

prevent users from examining code, use ENCRYPTION


Which of the following statements calls the stored procedure and passes the values ‘2019-10-01’ and 122 to its input parameters?

CREATE PROC spInvoiceTotal1
      @DateVar smalldatetime,
      @VendorID int
AS
SELECT SUM(InvoiceTotal)
FROM Invoices
WHERE VendorID = @VendorID AND InvoiceDate >= @DateVar;
	
	EXEC spInvoiceTotal1 @VendorID = 122, @DateVar = '2019-10-01';

When passing a list of parameters to a sproc by name, you can omit optional by
	omitting parameter name and value from the list


what do you use to create a user-defined table
	CREATE

which keyword can you use to pass a parameter back to the calling program
	OUTPUT

stored procedures are faster because they are
	precompiled

use return value of sproc to
	indicate to the calling program that the sproc completed successfully

Data validation is the process of
	preventing errors due to invalid data

## Exercises

**Exercise 1 and 2**

CREATE PROC spBalanceRange
	@VendorVar varchar(50) = '%',
	@BalanceMin money = 0,
	@BalanceMax money = 0

AS

IF @BalanceMax = 0
	BEGIN
		SELECT VendorName, InvoiceNumber, 
			InvoiceTotal - CreditTotal - PaymentTotal AS Balance
		FROM Vendors JOIN Invoices
			ON Vendors.VendorID = Invoices.VendorID
		WHERE VendorName LIKE @VendorVar AND
			(InvoiceTotal - CreditTotal - PaymentTotal) > 0 AND
			(InvoiceTotal - CreditTotal - PaymentTotal) >= @BalanceMin 
		ORDER BY Balance DESC;
	END
ELSE
	BEGIN
		SELECT VendorName, InvoiceNumber
			InvoiceTotal - CreditTotal - PaymentTotal AS Balance
		FROM Vendors JOIN Invoices
			ON Vendors.VendorID = Invoices.VendorID
		WHERE VendorName LIKE @VendorVar AND
			(InvoiceTotal - CreditTotal - PaymentTotal) > 0 AND
			(InvoiceTotal - CreditTotal - PaymentTotal) 
			  BETWEEN @BalanceMin AND @BalanceMax
		ORDER By Balance DESC;
	END;


EXEC spBalanceRange 'M%';

EXEC spBalanceRange
	@BalanceMin = 200,
	@BalanceMax = 1000;

EXEC spBalanceRange '\[C,F\]%', 0, $200;


**Exercise 3 and 4**

CREATE PROC spDateRange
	@DateMin varchar(50) = NULL,
	@DateMax varchar(50) = NULL

AS

IF @DateMin IS NULL OR @DateMax IS NULL
	THROW 50001, 'The DateMin and DateMax parameters are required.', 1;
IF NOT (ISDATE(@DateMin) = 1 AND ISDATE(@DateMax) = 1)
	THROW 50001, 'The date format is not valid. Please use mm/dd/yy.', 1;
IF CAST(@DateMin AS date) > CAST(@DateMax AS date)
	THROW 50001, 'The DateMin parameter must be earlier than DateMax.', 1;

SELECT InvoiceNumber, InvoiceDate, InvoiceTotal, InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Invoices
WHERE InvoiceDate BETWEEN @DateMin AND @DateMax
ORDER BY InvoiceDate;
