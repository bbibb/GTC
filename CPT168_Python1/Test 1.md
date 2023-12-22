
/# 
	block comment
	inline comment
	"commenting out"
*=  
+=  
-=  
AND  
Boolean expressions 
Relational operators
	== equal to
	!= not equal to
	> greater than
	< less than
	>= greater than or equal to
	<= less than or equal to
Logical operators
	for compound conditional expression
	order of precedence:
		NOT - reversees the value of a boolean expression
		AND - returns True if both expressions are True
		OR - returns True if either expression is True
		
break statement 
bytecode  - created by Python interpreter, passed by Python VM to OS
	platform independent
camelCase
chain functions
	code one function as the argument of another function
clause  
collection-controlled loop 
comments  
compile key in IDLE  
	looks for syntax errors (bugs)
	<testing> - find errors
	<debugging> - fix errors
	runtime error, while being executed - "exception"
	<debug>
	run
	
compound assignment operators 
	+=   adds value of the right to the variable on the left
		counter += 1
	-=   subtracts value of right from variable on the left
	*=.  multiplies variable on left by result of expression on the right
		price *= .8

conditional expressions 
condition-controlled loop 
	**while loop**
console application  
continuation  
continue statement  
control statements  
data types  
data validation  
editor  - for writing code, save and run with F5 key
first programming language 
	simple syntax
	features
	wide use
	open source
float(data)  - converts data to float
for loop  
	collection control
function  - group of statements to perform a specific task
IDLE - IDE, integrated development environment

//

[ ] (using brackets) 
if statement
indentation  

input()
	takes a string argument for the message
	all data is entered as strings
	first_name = input("Enter your first name: ")
	print(f"Hello, {first_name}")

int(data) - converts data to inteteger

interactive shell - in IDLE, for writing commands with immediate processing

literal  - value in a variable
	string literal
	numeric literal
	
logical operators 

lower()
	converts string to lowercase

main memory - RAM (OS and apps); data read from disk storage

NOT

open source  
operating system  
OR  
pass statement 
	each if must have at least one statement, so pass() holds the place but does nothing
print()  - function displays arguments that are passed, optional
	print(data[, sep=' '][, end='\n'])
	print(1,2,3,4,sep=' | ') 1 | 2 | 3 | 4
pseudocode  
Python 3 and Python 2 
relational operators 
round(number [,digits]) - rounds numeric value to specified digits
	
runtime error  
source code - program code, translated by Python interpreter to bytecode
statement - single command to perform a task 
	can be over multiple lines with indents (implicit continuation)
str()  - string data type
syntax error  
upper()  
	converts string to upper case
variables  
	assignment statements - variable name = value
	initialized
	names are case-sensitive
web application  
while loop
	condition control

Order of precedence, left to right when the same
1. **
2. *  /  //  %
3. + -

Join strings with + operator
	may need str() operator to convert numbers for joining with +
	name = last_name + ", " + first_name
fstrings
	name = f"{last_name}, {first_name}"
	braces identify variables, everything in one set of quotation marks

escape sequences, eg in print() function
	\n new line
	\t tab
	\r return
	\" double quote
	\' single quote
	\\ backslash
		or mix up quotation markes ' and " 

sort sequence for strings - each character at a time
	Digits 0-9
	Uppercase A-Z
	Lowercase A-Z

"Zebra" < 'apple'
"1" < "5"
"10" < "5"
>


Control statements: both if and while/for loops

Selection structure

if statements, don't forget the colon
only one block is executed!
	if boolean_expression:
		block of statements
	elif:
		more statements
	else:
		final option
nested if
	
Iteration Structure
	repetition structure
	while loop - condition-controlled loop
		if always true, it is an infinite loop
		tests the boolean expression at the top
		if false, does not execute
	for loop - collection-controlled loop
		for int_var in range_function:
			statements
		executes once for each item in range, and ends after

break
	breaks out of loop, jumps to next statement
continue
	jumps to the top of the loop
nested loop

assignment expression
	statement assigns value to a variable AND a Boolean expression that compares that variable with a value
	assignment part is in parentheses
	:= walrus operator
		while (score := input("Enter a score: ")) != "-1":
			[this is a while loop that assigns the variable score to the input value
			and also says this is true as long as that input is not -1]

Quiz 1
systems software for running applications
disk storage memory is persistent
main memory is volatile
interactive shell to test a python statement
syntax errors must be fixed before compilation
	syntax error
testing = find errors
debugging = fix errors
Python VM turns bytecode into computer instructions
F5 to run in IDLE
shebang = #!/usr/bin/env python 3
exception - leads to crash and error message
	runtime error
source code
IDLE editor to create program
web application in browser
console application command prompt
runtime error is an exception

Quiz 2
variables are first_name or firstName
float data type for decimals
% is remainder
	23 % 15 = 8
myNewAge - nothing wrong
comments
	ignored by compiler, documents, keeps lines from executing
print("pi = " + str(round(pi, 2))
	watch for spaces and round function
get floating point number
	my_number = float(input("Enter a number:"))
rating = rating + 2 WRONG
	string variable used in arithmetic expression
correct indentation - 4 spaces
new_num = 23 // 15 --> 1
	integer division
student_score in print function - 'scores' undefined variable name
lions & tigers & bears oh, my!!
score_curve += score
	BUT score is a string variable, so this is an error
"My student ID is " + str(123456)

Quiz 3

while (your_num > 0):
	3 * 5 = 15
	2 * 5 = 10
	1 * 5 = 5
if statement
	if if is true, it is executed, and not the elif or else
you bought 0 widget(s) today - no at prompt
can't do else within an elif
lower() method to compare strings
[counter is 1-20; counter *= 3]
	1 3 9 
	The Loop has ended
	--
	
for loop uses range function
	for i in range(0, 5)
Boolean variable
	flag = True
Boolean expression has value of true or false
range function
	once for each integer returned by the range function
while
	tests at the beginning; executes if true
50
	for i in range(0, 25, 5):
   sum += i
 pseudocode
	 coding of control structures

sort sequence
