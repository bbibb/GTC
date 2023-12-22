### Working with String Data

**string manipulation**

LEN()
	counts spaces at the beginning of a string but not at the end

LTRIM() 
RTRIM()
	remove extra spaces

LEFT(string, length)
RIGHT(string, length)
	get the specified number of characters at the beginning and end of a string
	*use to format columns in a result set*

SUBSTRING(string, start, length)
	splits the string on the passed separator

STRING_SPLIT(string, separator)

REPLACE(search, find, replace)
	replace a substring within a string with another one

TRANSLATE(search, find, replace)
	replace one or more characters with other characters
	might used instead of REPLACE()

REVERSE()
	reverse order of characters in a string

CHARINDEX(find, search [start])
	locate the first occurrence of a substring in a string
	*start* argument for starting other than the beginning

PATINDEX(find, search)
	locates a string pattern

CONCAT(value1, value2, ... valueN)
	concetenate two or more values into a single string
	you can combine other data types, NULL, converts to strings
CONCAT_WS(delimiter, value1,...)
	separate concat values by given delimiter

LOWER()
UPPER()
	convert case
	
SPACE(integer)
	returns a string with a specified number of spaces


Use CAST(ID AS int) to convert string column of numbers to integer type for sorting

Parse a string with full name into first and last
SELECT Name,
	LEFT(Name, CHARINEX(' ', Name) - 1) AS First,
	RIGHT(Name, LEN(Name) - CHARINDEX(' ', Name) ) AS LAST
FROM StringSample;
	*finds the first space and grabs letters up to the space
	finds the length and subtracts the number of spaces through the list, and grabs*'
	

### Numeric Data


ROUND(number, length, function)
	rounds a number to the precision you specify
ISNUMERIC()
	returns 1 if it is numeric, otherwise 0
ABS()
	returns absolute value
CEILING()
	smallest integer that is greater than or equal to the number
FLOOR()
	largest integer that is less than or equal to the number
SQUARE()
	returns square of a floating point number
SQRT()
	returns square root of a floating point number
RAND
	returns a random floating point number between 0 and 1

**How to search for floating-point numbers**


search for approximate value because floats are not exact
cannot use ==
	search on a range of values, eg .99-1.01
		SELECT * FROM RealSample
		WHERE R BETWEEN 0.99 AND 1.01;
	search for values that round to an exact value
		not as efficient as the first method
		SELECT * FROM RealSample
		WHERE ROUND(R,2) = 1;

 **How to work with date/time functions**

GETDATE - current local date and time
GETUTCDATE - GMT

datetime2 value
more precise fractional second than GETDATE
	SYSDATETIME:
	SYSUTCDATETIME:
	SYSDATETIMEOFFSET (includes time zone offset):
		datetimeoffset value

Extract different parts of a date value:
DAY
MONTH
YEAR
DATENAME
DATEPART
DATERUNC

Addition and subtraction on date/time values
DATEADD
DATEDIFF

offset data:
TODATETIMEOFFSET (add time zone offset)
SWITCHOFFSET (specify new time zone)

get last day of month:
EOMONTH

create date value from given integers:
DATEFROMPARTS

boolean is it a valid date/time?
ISDATE
	doesn't work with datetime2 values

Date Part Values
	yy, yyyy
	qq, q
	mm, m
	dy, y
	dd, d
	wk, ww
	dw (weekday)
	hh
	mi, n
	ss, s
	ms
	mcs
	ns
	tz (tzoffset)

DATEPART(month, '2023-04-30')    # 4
DATENAME(month, '2023-04-30')    # 'April'
EOMONTH('2023-02-01')            # 2023-02-28
DATEFROMPARTS(2023, 4, 3)        # 2023-04-03

**How to parse dates and times**

