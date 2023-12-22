Data type
	 the kind of information the column can store
	 determines the operations it can take

String Types
Numeric Types
	Integers
	Floating Point
	Currency
	Numeric data
Temporal Types
	Dates
	Times
	Both
Additional
	rowversion
	geometry
	geography
	hierarchical data


### Numeric Types

3 Groups:
	Integer "exact numeric types"
	Decimal "exact numeric types"
	Real "approximate numeric types"

Integer
	whole numbers 
		bigint
		int
		smallint
		tinyint
		bit
Decimal
	fixed decimal point that does not vary
		**scale** = number of digits it has to the right of decimal point
		**precision** = total number of digits
		975.82 -> scale is 2, precision is 5
	types
		decimal
		numeric
		money
		smallmoney
Real
	floating point numbers
		large and small numbers, limited number of significant digits
	single-precision number
		up to 7 significant digits
	double-precision number
		up to 15 significant digits
	float(24) - float type usually used for real type numbers
		great for space saving in large numbers
		6.02E+32 rather than 10(32) nonsignificant digits, just 3: 6.02
	types
		real
		float

### String Types

with default collation,
var and varchar type uses 1 byte per character
		256 characters, code is 0-255
		first 128 are ASCII system
		max bytes of a string is 8000
		
nchar and narchar use 2 bytes
		for Unicode characters ("national characters")
		16 bits = 63,536 different characters
		great for multi-language support
		max bytes for a string is 4000

Fixed-length Strings
	char and nchar
		same number of bytes regardless of length of the string
		only use when the length is always the same
	varchar and nvarchar
		variable-length strings
			bytes used for the message, and 2 bytes for the length data


### Date/Time types

Old: datetime and smalldatetime
	datetime is larger but supports more precise time than smalldatetime

four date/time types from SQL2008
	use these
	date
	time(n)
	datetime2(n)
	datetimeoffset(n) (timezone offset)

formats
	yyyy-mm-dd
	mm/dd/yyyy
	Month dd, yyyy
	(mm-dd-yy, etc with 2 years)

time
	hh:mi
	hh:mi am/pm
	hh:mi:ss
	hh:mi:ss:mmm
	hh:mi:ss.nnnnnn

### Large Value Types

store up to 2GB of data per column

varchar(max)
	varchar, but up to 2GB of string data
nvarchar(max)
varbinary(max)
	same, but binary data

3 approaches to binary data
	- varchar(max) with string that points to a file
	- varbinary(max) to store binary data *in the database*
	- varbinary(max) with FILESTREAM


### How to convert data

*implicit conversion*
	SQL converts datatypes based on priority
	eg, converts int to float before doing math
		eg, int converted to money before subtracted from money

order of precedence, highest to lowest
	datetime2
	date
	time
	float
	real
	decimal
	money
	smallmoney
	int
	smallint
	tinyint
	bit
	nvarchar
	nchar
	varchar
	char


*explicit conversion*
	CAST
	CONVERT

CAST
	CAST(expression AS data_type)

SELECT InvoiceDate, InvoiceTotal
	CAST(InvoiceDate AS varchar) varcharDate,
	CAST(InvoiceTotal AS interger) AS intergerTotal),
	CAST(InvoiceTotal AS varchar) AS varcharTotal
FROM Invoices


eg, divide two integers, SQl returns a whole number
	cast one of the integer values as a decimal and then you get a decimal
	50/CAST(100 AS decimal(3)) -> 0.5

CONVERT

Without a (style) argument, CONVERT works just like CAST

Style codes for time
	0 or 100 
		Mon dd yyy hh:miAm/Pm
	1 or 101
		mm/dd/yy or mm/dd/yyyy
	7 or 107
		Mon dd, yy or Mon dd, yyyy
	8 or 108
		hh:mi:ss
	10 or 110
		mm-dd-yy or mm-dd-yyyy
	12 or 112
		yymmdd or yyyymmdd
	14 or 114
		hh:mi:ss:mmm (24 hour clock)

Style codes for real to character data
	0
		6 digits max
	1
		8 digits, sci not
	2
		16 digits, sci not

Style codes for money to character data
	0
		2 digits to the right, no commas to the left
	1
		2 digits to the right, commas to the left
	2
		4 digits to the right, no commas to the left


### TRY_CONVERT(data_type, expression [, style ])

Null value if CONVERT cannot be performed
Otherwise, CONVERT will return an error


### Other data conversion functions

STR(float[, length[, decimal]]) 
	to convert floating-point to character
	usually specify a length to make sure it doesn't cut off the digits

CHAR(integer)
	integer to one-byte character

ASCII(string)
	leftmost character in a string to its ASCII integer value

NCHAR(integer)
	integer to its Unicode character

UNICODE(string)
	leftmost character in a string to its unicode integer