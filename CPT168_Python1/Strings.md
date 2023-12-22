

Unicode - integer mapped to ordinal value
	ord(*char*) shows value of character

Use an index to refer to a character in a string
	if incorrect, you get an IndexError

A string is immutable
	if you try to change it, you get a TypeError
can slice like a list

\* repetition operator

**How to search a string**

**in** keyword
	term in *string*
	"million" in spam - returns true if so
	if search_term in spam:
		print("Term found.")

**basic string methods**
isdigit()
isalpha()
isupper()
islower()
	these all return True if so, useful in conditional expressions
	
startswith()
endswith()

lower()
upper()
title()

lstrip()
rstrip()
strip()
	string.strip() - removes whitespace from beginning and end

ljust()
rjust()
center())

**find/remove/replace**

find(str, start, end)
replace(old, new, num) (optional num = number of times to replace)
	cc_number.replace("-", " ") - removes - and adds spaces
removeprefix()
removesuffix()


**how to split and join strings**

split(delimiter, num)
	uses delimiter to split a string into substrings
	returns a list of those substrings
	optional num - number of splits to make

words = quotation.split()
print(words\[0]) - prints the first word in the quotation

date = "11/9/1972"
date = date.split("/")
month = int(date\[0]) - 11

full_name = "Guido von Rossum"
name_parts = full_name.split(" ", 1)
print(name_parts\[0]) - Guido
print(name_parts\[1]) - von Rossum

join strings methods
	with +      a + b
	with +=   a += b
	with f-string
		full_name = f"{last_name}, {first_name}"


use join() to create a new string from string + delimiter
address = "|".join(address)
	prints list items with | delimiter







