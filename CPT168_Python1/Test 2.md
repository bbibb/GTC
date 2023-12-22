## Chapter 4 Functions and modules

### Defining and calling

function is a unit of code that performs a task

easier to maintain, test, debug

when calling, put arguments in the same order they are in the definition
	variable names in your call do not have to match the ones in the def

def function_name([arguments]):
	statements

you can code a return statement that returns value to calling function

put all code in functions, and call them with main()
	if \_\_name\_\_ == "\_\_main\_\_":
		main()

when you define a function you can assign **default values** to one or more arguments
	name=value (no space)
	gets filled in if the calling function leaves it blank
	must be coded last in the list in the definition

**named arguments** in the calling statement
	so you don't have to use the same order
	name=value
	improve the readability of the code and reduce errors

### Global and local variables

Scope in a programming language refers to the visibility of variables

**global variables** are defined outside of all functions
	global scope
	accessed by any functions
	avoid

**local variables** are defined within functions
	can only be used in the function that defined them
	
if a function wants to change a global variables, has to use "global" keyword

**shadowing** is when the same name is used as a global and local variable
	can lead to debugging problems
	best avoided

**global constant** 
	when you don't use the global keyword for a global variable
	TAX_RATE = 0.05
	read-only by default
	have to use global keyword to change it (bad practice)


### Create and use modules

A modules is a file that contains reusable code like functions

contains function definitions
	def function(argument):
		code

and a main function for testing
	def main():
		testing code

ends with if \_\_name\_\_ == "\_\_main\_\_":
	main()

if you run the module directly, main gets called, but not if the module is loaded by another program

the name of the module comes from the name of the file

easiest way is to store all py files in the same directory
	else, must be in the **search path**

### Document a module

**docstrings**
	start and end with 3 double quotation marks
		"""
		Description of the module's purpose
		"""
	

**hints** to document the type of a function argument and the type of its return value
	for arguments, use a colon followed by the type
	for return value, use arrow followed by the type
		def to_celsius(fahrenheit: float) -> float:

help() function with the name of the module as its argument to see the documentation for the program
	run module in IDLE, import it, pass its name to help()


### Import a module

1.
import statement 
	into default namespace or specified namespace
		import temperature

namespace - area in main memory that holds a module
	default: namespace is same name as the module
	namespace.function()
	temp.to_celsius()

	AS lets you import into a different namespace
		import temperature as temp
2.
From variation to import into the global namespace
f you go into global, you can get **name collision**
	but you don't have to use namespace prefix
		from module_name import function_name1[, function_name2...]
i
3.
Import all functions
	from temperature import *

### How to use standard modules

import and call its functions, same as if you made them

**Random** module
	random() - (0.0, 1.0)
	randint(x, y)
	randrange(start, stop, step)

### Hierarchy chart

top-level function
functions called by it
use verb and noun syntax

when coding the functions of a program, make sure it does everything its name implies, and nothing not implied by the name

a return() statement can return multiple values
local variables must be passed to each other in calling statements and return statements


## Chapter 5 Debugging

TEST - make sure it works right
	combinations of data and actions, trying to make it fail
DEBUG - fix errors BUGS that oyu discover during testing

**3 types of errors**
1. Syntax errors - prevent from compiling
	"compile-time errors"
	easiest to find and fix

2. Runtime errors - throw "exceptions"

3. Logic errors
	program runs but not correctly - produce wrong results
	difficult to find and fix


Common errors:
not ending a for statement with a colon
using a variable name that has not been defined yet
forgetting quotation marks and parentheses
parenthesis instead of brackets, vv
improper indentation

misspelling keywords
keyword as variable or function name
wrong data types

floating-point arithmetic can be wrong
	need to round

### How to plan test runs
1. Valid Data - list entries and results
2. Invalid Data - list entries and results

you have to know what the results should be to test
test wide enough range


### Trace code execution

trace the execution of a program
	add statements that display messages or values at key points
	print(f"{i = } {future_value = }")
		the equals causes the variable name and value to be printed


### Top-down coding and testing
Code a function and getting it to work
Code a second, and adjust the first to make it use the second
Continue...
Code the main function 

testing a small amount at a time to make sure each piece works correctly


### IDLE shell to test

You can run a function right in the shell, isolating them from other code
	easier to see if it is working

Run the program to completion, or break it in the shell
then you can call any function in it

you can also load a module for the same thing


### IDLE debugger

step through statements of a program one at a time

set a breakpoint at the point just before where you think the problem is
	use exception info to see, maybe

set it on an executable statement
Go button
Step - execute every statement 
	debugger shows local variables and values
	can also click global list

### View the stack
list of functions that have just been executed
	for each function, see local and global variables
	use when an exception is thrown to explore
	Debug -> Auto-open Stack viewer, for automatic

expand the function folder to see
	double-click to get to that part of the code


## Chapter 6 Lists and Tuples


### Lists

Brackets, separated with commas
\ * Repetition operator (good for setting default values)
	scores = [0] * 5 --> scores = [0, 0, 0 ,0, 0]
 = assignment operator

If you try to access item not in a list, you get Index Error

Index
	0 is the first item
	-1 is the last item

append(item)
	add item to the end of a list
insert(index, item)
	add item anywhere in the list
	inventory.insert(3, "robe")
remove(item)
	remove an item
	inventory.remove("shows")

pop([index])
	if empty, removes the last item and returns it to the calling function
index(item)
	search for an item that matches

if remove() and index() don't find the item
	ValueError Exception

### Process items in a list

len(list) 
	gets absolute length of the list
	index() returns 0-9, and len() returns 10

print(list)
	print a list to the console
	good for testing

for loop
	once for each time in the list
	good b/c you don't need to use an index or counter variable, or know the length of the list
	for item in list:
		statements

enumerate(list[, start=0])
	associate a counter value with the items in a list
	gets both counter value and current item
	optional argument to set initial value, default=0

	for i, item in enumerate(inventory, start=1):
		print(f"{i}. {item}")
	prints a list of the items in numbered list
	
zip(list1, list2, ...)
	process two or more lists in parallel
	gets current item from each list 0,0; 1,1; and so on


### How lists are passed to functions

Python uses objects to store data of all data types
	strings, integers, floating-point numbers, Booleans values, lists
	all of those are **immutable**
	except lists which are **mutable**

immutable objects operated on in a function must be returned to the calling function
	the function is actually creating a new object
	value = value * 2
	return value

mutable object of a list does not need to be returned
	the calling function already has access to it.

### List of Lists

store a list in each item of another list
	data stored in two dimensions
		"two-dimensional list"

sort of like rows and columns

Use 2 indexes

Use nested loops to process items, one row at a time

students = \[\["Joel", 85, 95, 70],
				\["Anne", 95, 100, 100],
				\["Mike", 77, 70, 85]]
if you print it, the console prints the brackets

for loop
	for movie in movies:
		for item in movie:
			print(item, end=" | ")
	print()

	this prints the items in each row with pipe separator
		because it's doing each row, there are no brackets in output


or, use enumerate:
	for i, movie in enumerate(movie_list, start=1):
		print(f"{movie[0]} ({movie[1]})")

    this prints the movies in an enumerated list with the movie name (0) and the movie year (1) in each row

delete() function
	number of the movie to be deleted is one higher than the index number

If you ask for a movie number in the list, and then pop it, you have to pop the number *minus 1* because of the index0



### More Skills for lists

count(item)

reverse(list)

sort(key=function)
	because Z comes before a, you have to use a second key argument
	convert to lowercase letters before sorting
	foodlist.sort(key=str.lower)
		the uppercase letters are retained in the list, but disregarded for sorting
		if you print before and after you can see it.
		same list

sorted() works the same
	sorted() creates a new list while sort() does not
	sorted_foodlist = sorted(foodlist, key=str.lower)
	you're creating a new list

max(list)

min(list)

sum(list[, start])
	sum of all the items, optional start value

random module:
choice(list)
	randomly selected item from list
shuffle(list)
	shuffles list


### How to copy, slice, and concatenate

shallow copy
	assigns variable to another variable
	not both variables share the same *mutable* list
	list_two = list_one

deep copy
	deepcopy(list)
	two variables that refer to two different lists
	initially the same but can diverge then
	have to import copy module

	import copy
	list_one = []
	list_two = copy.deepcopy(list_one)


slicing a list

	mylist[start:end:step]
numbers = [1, 2, 3, 4, 5]
numbers[0:2]. -> 1, 2
numbers[:2] = -> 1, 2
numbers[:3] -> 4, 5
numbers[0:4:2] -> 2, 4
numbers[::-1] -> 5, 4, 3, 2, 1

joining lists
list_total = list_one + list_two
	new list

list_one += list_two 
	list_one now ends with list_two items

### Map, filter, reduce

map(function, list)
	passes each item in the list it receives to the function it receives, and returns all the items produced by those function calls
	- a map object
	- contains the return value for each function call
	- use list() to convert it to a list
if the function is n * n, you can pass it and a list to get a list of squares

filter(function, list)
	new list of numbers based on criteria
	also passes each item in the list it receives to the function it receives
use n % 2 == 0, pass to a list to get even numbers


reduce(function, list[, start])
	reduces the items in an existing list to a single value
	returns that single value
in basic form sort of like sum, max, min

### List comprehensions
a more concise way to create a new list from a list
	rather than map() and filter()
	optional if statement you can use to filter data

assignment expression :=
	you can use the variable that's assigned a value *in the expression* right in the expression itself
	can use it for list comprehension in the if section
		but the variable name has to be different from the outside one
	

newlist = [*expression* for *item* in *list* [if condition]]

create a list of squares
	numbers = [1, 2, 3, 4, 5]
	squares = [n * n for n in numbers] -> 1, 4, 9, 16, 25

even squares
	even_squares = [n * n for n in numbers if n % 2 == 0]

calling a function
	def square
	def is_even
	even_squares = [square(n) for n in numbers if is_even(n)]

assignment expression
	import random
	 def get_number:
		return random.randrange(1, 10)
	squares = [square(num) for n in range(10) if (num := get_number()) <= 6]



### tuples

immutable
	can't use add, modify, or remove methods

parentheses instead of brackets
if it only has one item, you have to use a hanging comma
	scores = (99,)

to retrieve, you use an index in brackets, same as lists

use *multiple assignment statement* to **unpack** the items in a tuple

	tuple_value = (1, 2, 3)
	a, b, c = tuble_values
		(now a = 1, b = 2, and c = 3)

a call to get_location that and unpacks the tuple
def get_location():
	gets x, y and z, and returns them as a tuple
x, y, z = get(location)



## Quiz 4

def multiply(num1, num2):
   product = num1 * num2
   result = a.add(product, product)
   return result
answer is 24

def get_volume(width, height, length=2):
   volume = width * height * length
   return volume
(10, 2) -> 40


To call a function with named arguments, you code the name of each argument, an equals sign, and the value or variable that's being passed

A return statement can be used to return a local variable to the calling function

import a module into the default namespace
	import temperature

def add(x = 4, y = 2):
   z = x + y
   return z
   x=5, y=6
   The sum is 11

import address as a
a.print_name(name)

import a module into the global namespace
from temperature import *

before you can use a standard module like the random module, you need to import the module

def get_username(first, last):
   s = first + "." + last
   return s.lower()
what arguments are defined? first, last

a global variable is defined outside of all functions

def add(x = 4, y = 2):
   z = x + y
   return z
 a.add(5, 6)
 now x=5, y=6

the best way to call the main() function is to code an if statement that calles the main() only if the current module is the main module
if \_\_name\_\_ == "\__main\_\_":
	main()

the scope of the variable inside a function is **local**

s = first + "." + last
   return s.lower()
returns lopez.maria

coin toss:
	number = random.randinit(0, 1)
**randinit sets range including last value**

*the define function is called by the multiply function*

what function is called first when the program run?
	main()

To assign a default value to an argument when you define a function, you
code the name of the argument, the assignment operator(=), and the default value

x and y after code runs:
	12, 12

get_volume()
3x4x5 = 60

NOT TRUE
You can use regular Python comments to document the functions of a module
TRUE
You can call the help() function from the interactive shell
The documentation can describe each function in the module
You can use Python docstrings to document the functions of the moduel

NOT TRUE hierarchy charts
Related functions should be combined into a single function

If you import two modules in global with same name,
	a name collision occurs

random.random() returns value between 0 and 1
	0.94

the default namespace for a module is the same as the name of the module

to call a function you code the function name and a set of parentheses that contains zero or more arguments

a file that contains reusable code is a module

to define a function you code the def keyword and the name of the function
	followed by a set of parentheses that contains 0 or more arguments

a local variable is defined inside a function

random even integer 2 to 200
	number = random.randrange(0, 202, 2)
	(have to do 202 because randrange does not include the top value)


### Chapter 5 quiz

When you use the IDLE debugger, you start by setting a breakpoint on a statement before the statement you think is causing the bug

def sales_tax(amt)
	error: syntax error in line 1, no colon

def display_info(fname, lname, score):
     print("Hello, " , fname, " " , Lname)
syntax error: Lname variable does not exist

count = 1
	while count <= 4:
	print(count, end=" ")
  i *= 1
 print("\nThe loop has ended.")
syntax error line 4: i variable does not exist

When the IDLE debugger reaches a breakpoint, you can do all but one of the following
FALSE
	view the values of all the variables you have stepped through

TRUE
	view the values of the local variables that are in scope
	step through the program one step at a time
	run the program until the next breakpoint is reached

print("Your score on this exam is ", score)
score = score + 5
logic error
	the curve is calculated after the score has been displayed

pay = (hours * rate) + (hours - 40 * rate * 1.5)
LOGIC ERROR
	pay = (40 * rate) + ((hours - 40) * rate * 1.5)

The stack is available when an exception occurs. It displays a list of
	just the functions that were called prior to the exception

A runtime error throws an exception that stops the execution of the program

user-friendly correct result
	round(discount, 2)

For tracing, use print functions for:
FALSE
	display the values of the global constants used by the function
TRUE
	global variables used by the function
	function that print() is in
	local variables in the function


ERROR
score = score + 5
The variable has been input as a string so must be converted to int or float


plan test runs, do all but
FALSE
	list the expected exceptions for each test run
TRUE
	list valid entries
	list invalid entries
	list expected results

ERROR
def main():
	first = input("first name: ")
	last = input("last name: ")
	grade = input("exam score: ")
	 display_info(last, first, score)
grade is defined, but undefined score is passed

Sometimes program crashes
	because programmer didn't test for 0 value in the denominator

Common types of syntax errors
	forgetting a colon
	improper indentation
	forgetting to close a parenthesis
	NOT: invalid variable names
		(that's a runtime error)

ERROR
Total cost: 30
Average cost: 8
	line 8, average_cost = round(item_total / (count-1))
	because count starts as 1, not 0

To test the functions of a module from the IDLE shell, you
	import the module and then call any function from the IDLE shell

Syntax error prevents compiling and running



### Chapter 6 quiz

numbers = (22, 33, 44, 55)
	-> w, x, y, z = numbers
	change tuple to variables

What is not true about a list of lists
FALSE
	to delete an item in the outer list, you first have to delete the list in the item
TRUE
	use nested for statements to loop
	inner and outer are mutable
	refer to item in inner list with two indexes

prices = [10, 15, 12, 8]
	while i < len(prices)
	+=
total is 35 because you are adding 1, 2, and 3 (15+12+8)

When a function changes the data in a list, the changed list 
	does not need to be returned because lists are mutable

primary difference between tuple and list
	tuple is immutable

ghost, witch, elf, ogre
remove elf, print()
	ghost
	witch
	ogre

Lizzy 73 C Mike 98 A Joel 88 B+ Anne 95 A
(because end=" " instead of \\n)

tuple
	vehicles = ("sedan", "SUV", "motorcycles", "bicycle")

list of floating points
	number = [5.3, 4.8, 6.7]

sort/reverse students
	\[\['Mike, 98, 'A'], \[\], \[\], \[]]
	printing the list creates brackets around each row, and around total group

remove mangos
	fruit.remove("mangos")
	fruit.pop(3)
	(remove takes a string, pop takes an index)

List copies
FALSE
	deep copy of a list, both variables refer to the same list
TRUE
	deep copy, both refer to their own copy of the list
	shallow copy, both refer to the same list
	shallow copy, the list is mutable

ages[5]
	None: Index error

adding
	sandwich, chips, pickle, apple pie
	(apple pie replaces banana in the add function)

fruit.insert(3, "melon")
	insert(index, item)
	index is first!

list of list index
	\[2]\[1]
	third row, second column

To refer to an item in a list, you code the list name followed by
	an index number in brackets, starting with the number 0

choice()
	function randomly selects one item in a list

append()
	method adds an item to the end of a list


when you use a multiple assignment statement to unpack a tuple
	you assign the tuple to variable names separated by commas

The pet store sells 
	list of all animals
These start with c: cat, canary

ages.insert(3,4)
	put 4 into the 3rd index spot (4th absolute spot)


my_name = name.pop()
	"Donny" , and names is all of them without donny
	pop removes the last one and returns it