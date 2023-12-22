
## Chapter 7 File IO


A binary file is like a text file in all but what way?
	A binary file stores numbers with binary notation
	
	  [can be used to store a python list]
	   [can be grouped into records or rows
	   [stores strings with character notation]]


To work with a file when you're using Python, you must do all but one of the following
	decode the data in a file

	 open
	 write or read
	 close

with open("classes.bin", "rb") as file:
	**causes an exception if the file names classes.bin doesn't exist**

to read the rows in a csv file, you need to
**get a reader object by using the reader() function of the csv module**


not a benefit of a with statement?
	you don't have to specify the path for the file

	file is closed even if an exception occurs while the file is being processed
	file is automatically closed
	resources used by the file are released

write list to CSV file
with open("prog.csv", "w", newline = "") as file:
	writer = csv.writer(file)
	writer.writerows(programming)


Python (3)
Trig (3)
	the parentheses are in the print statement
	range is len - 2, which 4-2 = 2, so prints 2 lines


Python 3 Physics 4
	there are no parentheses in the print statement
	the i +=2 means you print the first and third one
	the end is defined as " " rather than default /n, so on one line

which of the following is not true of csv
	the csv module is a standard module you don't have to import


What happens if csv file doesn't exist when open statement is in w mode?
	**a new file with that file name is created**

with statement in "wb" mode
	**writes courses to a binary file if the file name doesn't exist**

to read a list of lists in a binary file?
	**the load() method of the pickle module**


in first open statement, what is written to the file?
**The list named courses**



## Exceptions



Python program should use try statements to handle
**all exceptions that cannot be prevented by normal coding techniques**


To throw an exception with Python, you use the
	**raise statement**

The finally clause of a try statement
	**is executed whether or not an exception has been thrown**

Its a common practice to throw exceptions to test error handling to
	**catch exceptions that are hard to produce otherwise**

If the for statement refers to readers instead of reader
	**NameError**

If names.csv is not in the same directory
	**FileNotFoundError**

To cancel the execution of a program
	**exit() function of the sys module**

When an exception is thrown, the exception object contains info about the type, name, and message but not
	**the severity of the exception**
	

try:
	number = int(input...
**except Exception as e:
	print(type(e), e)**

Within the try clause you code
	**a block of statements that might cause an exception**

catch any type of exception;
	try:
		number = 
		print()
	**except:
		print("Invalid number")**

If a program attempts to read from a file that does not exist?
	**FileNotFoundError** and **OSError**


## Numbers

You can use the format() method to format numbers in all but what way?
	apply $ signs
		insert commas
		apply % signs
		right and left align

comma format with two decimals
	print("{:,.2f}".format(number))

{:10.2f}
	2f means **a floating point number with 2 decimal places**

Which module provides function for getting square root
	**math**

area = m.pi * m.pow(radius, 2)
	same as m.pi * radius** 2

pounds with 2 decimals and a comma
	lc.setlocale(lc.LC_ALL, "uk")
	print(lc.currency(34567.89, grouping=True))


deal with fp inacuracies
	**round the results of those calculations that may lead to more decimal places than you want in the final result**

floating point numbers
	**are approximate values**

module to work with decimal numbers
	**decimal**

with Decimal objects in an arithmetic operation, you cannot use
	**floating point values as operands**

not floating point
	-683

.15605 as 16%
	**print("{:.0%}".format(number))**

decimal
	**from decimal import Decimal
	number = Decimal(123.4567)**

Name.             ID
Liz                     234
Mike              23456
	print("{:10} {:>5}".format(name, ID))
	print("{:10} {:7d}".format("Liz", 234))
	print("{:10} {:7d}".format("Mike", 23456))


round decimal number in variable to 2 places with business
	**number = number.quantize(Decimal("1.00"), ROUND_HALF_UP)**

To be sure that results are accurate to 2 places
	**round the result of each expression to 2 decimal places**

Which variables might contain approximate results
	1, 2, and 3

:5d
	**integer with 5 spaces allowed**

module for currency
	**locale**

deal with inaccuracies
	**do the math with Decimal objects instead of fp numbers**
