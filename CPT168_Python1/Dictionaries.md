
**create a dictionary**
{key: value}
unordered
	can't loop through and expect the order to be the same
key must be unique
	can be any immutable type
value can be simple data or complex (list or dictionary)
whitespace is ignored
aka "associative arrays"

countries = {"CA": "Canada",
			"US": "United States"
			"MX": "Mexico"}

print(countries)
	{'MX': 'Mexico', 'CA': 'Canada', 'US': 'United States'}

**get, set, and add items**

use a key
	if not there, a KeyError
	country = countries\["MX"]

use **in** keyword
	checks and prevents error
	if code in countries:
	do some stuff

get() method
	key as argument, returns value
	default, return None if key not there
	optional argument to get different null value
country = countries.get("MX")


*Delete items*
**del** keyword followed by variable and the key in brackets
	check if there before to prevent error
	del countries\["MX"]
or, use pop() method
	returns and deletes specified key
	helpful if you need to store the deleted value in a variable
	country = countries.pop("MX")
	prevent Key error
		country = countries.pop("MX", "Nothing")

delete all?
	clear() method

*Loop through keys and values

3 methods to get keys and values
each returns a **view object**
	linked to the dictionary
	can use to loop through
But, if you want to sort, need to convert to list
	then, it will no longer be linked to original dictionary

keys()
	view object with all keys
	default iterator with *for key in dictionary* loop
items()
	view object with tuple for each key/value pair
values()
	view object with all values



**convert between dictionaries and lists**


list() constructor
keys() -> list() -> sort()

convert list of lists to a dictionary:
	dict()
	the lists must all contain exactly two values


**merge and update**

| merge operator - union operator
	merges two and returns a new dictionary
	countries = north_america | europe | asia
	if duplicate keys, the value of the last one is used

|= update operator
	updates the dict on the left with the items from the right
	if the keys are the same, value is updated
	or, key/value pair is added


**complex data types**

dictionary can contain other dictionaries as values
contacts = {"Anne": {"phone": "555-555-5555"}}
	phone = contacts\["Anne"\]\["phone"]

can test for existence of first key before looking for second
	otherwise, KeyError

can use get()
	but if key does not exist, gets AttributeError
	can use optional second parameter


lists as values
students = {"Joel":\[85, 95, 70]}
	joel_score = students\["Joel"]\[0]  -- 85

