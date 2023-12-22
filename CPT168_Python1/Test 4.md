## Chapter 10

The join() method of a list can combine
	the items in the list into a string separated by delimiters

B = 66
	print("B = ", ord("B"))
	ord changes an ASCII number to its letter

You cannot modify a string

strip() method strips away extra whitespace

To determine the length of a string that's in a variable named city:
	len(city)


You can use the split method to split a string into a list of strings
	based on a specified delimiter

book = book_name.title()
	title() method changes every word to upper case

Create a string named n2
	numbers = ["8", "17", "54"]
	n2 = "".join(numbers)
	NOT
		numbers = 8, 17, 54
		n2 = "".join(numbers)


A unicode character is represented by a
	2-digit code

word = "a horse"
	a horse! a horse! My kingdom for a horse!
		print((word + "1") * 2 + " May kingdom for " + word + "1")

If user enters 555-123-4567 when len(number) == 10
	the length will be greater than 10, so the else clause will execute

abc def ghi
1:5 = bc d
replace('b', 'z')
	s3 = zc d

car = "PORSCHE"
color = "red"
my_car = car.join(color)
print(my_car)
	rPORSCHEePORSCHEd
	(the thing that is joined becomes the delimiter between each letter of the list being operated on)

To access the first 3 characters in a string
	first_three = message\[0:3\]

email = "joel.murach@com"
result  email.find("@") - email.find(".")
print(result)
	7 (11-4)

Countdown...
5...
4...
3...
2...
2...
Blastoff!
	counting = "54321"
	print("Countdown...")
	for char in counting:
		print(char + "...")
	print("Blastoff")

email = "marytechknowsolve.com"
result = email.find("@")
	-1
	(means that it was not found)

isdigit() method returns
	true if the string contains only digits

5551234567
phone_number = "()" + phone_number\[:3\] + ")"
					+ phone_number\[3:6\]
					+ "-" + phone_number\]6:\]
	prints:
		Phone number: (555-123-4567)

To retrieve the 4th character in a string:
	city\[3\]

name = "Mervin the Magician"
words = name.split()
print(words\[0\] + ", you are quite a " + words\[2\].lower())
	Mervin, you are quite a magician


## Chapter 11

from datetime import date
this_day = date(2018, 2, 8)
this_day = this_day.strftime("%B %d %Y")
print("Today is", this_day)
	Today is February 08, 2018

When you subtract one datetime object from another you get
	a timedelta object

(Tracking only hours and minutes if day=0) If timer is started at 4:00pm and stopped 3 seconds later:
	Time elapsed:
	hours: 0, minutes: 0

To create a datetime object by parsing a string, you can use the
	strptime() method of the datetime class

When you care a datetime object by parsing a string, you pass 
	a string that represents the date and a formatting string that determines the parsing

("%B %d, %Y (%A)")
	February 08, 1998 (Sunday)

you can access the parts of a date/time object by using its
	attributes

Time, Nov 17 at 4:00PM to Nov 18 at 6:30pm
	Time elapsed:
	days: 1
	hours: 2, minutes: 30

In that problem, the value of minutes is 30
But the value of seconds is undefined

A naive datetime object doesn't account for
	time zones and daylight savings time

striptime(today, "%m/%d/%Y")
print(this_day)
Enters: 21/11/2018
	ValueError: time data does not match format

from datetime import datetime
this_day = date(2018, 2, 8)
	ValueError: name 'date' is not defined
	(Imported datetime, not date)

To create a datetime object with a constructor, you pass this sequence:
	year, month, day

To create a datetime object for the current date and time,
	now() method of the datetime class
	(when creating objects, the method is part of the class)

today = datetime(2018, 4, 26)
birthday = datetime(2018, 6, 21)
wait_time = birthday - today
wait_time.days
	There are 56 days until your birthday
	(year, month, day so June 6 - April 26)

To work with dates you need to import
	the date class from the datetime module
		(NOT both the date and datetime classes)

To store just the year, month, day you use a
	date object

To format a datetime object for the current date and time you can use the
	strftime() method of the datetime object
	(when working with objects, the methods are part of the object)


To compare 2 datetime objects you
	can use any of the comparison operators

from datetime import datetime
new_year = datetime(2017, 1, 1)
day_of_week = new_year.strftime("New Year's Day is on a %A")
print(new_year)
print(day_of_week)
	2017-01-01 00:00:00
	New Year's Day is on a Sunday

day = start.strftime("%d")
What variable holds the value of the beginning day?
	day


## Chapter 12


flowers = {"red": "rose", "white": "lily", "yellow": "buttercup"}
if key in flowers:
	flower = flowers\[key\]
	print("This is a", key, "flower:", flower)
Prints:
	This is a white flower: lily

pets = {"cat": {"type": "Siamese", "color": "black and white"}}
To print "black and white Siamese cat":
	pet = "cat"
	print(pets\[pet\]\["color"], pets\[pet]\["type"], pet)
	(printing the color for the key 'cat' and the pet type for the key 'cat')

flowers = {"red": "rose", "white": "lily", "yellow": "buttercup"}
print(flowers)
flowers["blue"] = "carnation"
print(flowers)
	prints:
		{'blue': 'carnation', 'red': 'rose', 'white': 'lily', 'yellow': 'buttercup'}

Flower name: buttercup

flowers = {"red": "rose", "white": "lily", "yellow": "buttercup"}
	contains 3 items

To avoid a key error when using pop() you can
	use the optional second argument to supply a default value

To convert a view object to a list, you can use the
	list(constructor)

colors = list(flowers.keys())
colors.sort()
show_colors = "Colors of flowers: "
for color in colors:
	show_colors += color + " "
print(show_colors)
	Colors of flowers: blue red white yellow
(getting the keys, sorting abc, then adding them with spaces to the opening phrase via loop)

The key in a dictionary can be
	any immutable type

The key() method returns a
	view object containing all the keys in a dictionary

The items()method returns a
	view object containing all of the key/value pairs in the dictionary

flowers = {"red": "rose", "white": "lily", "yellow": "buttercup"}
print(flowers)
flowers["blue"] = "carnation"
print(flowers)
print("This is a red flower:", flowers.get("red", "none"))
Prints:
	This is a red flower: rose
(flowers.get() method to get value from "red" key, with "none" as a default if not found)

key/value pair?
	red/rose

if key = "green"
	There is no green flower

Each item in a dictionary is a
	key/value pair

A dictionary stores a collection of
	unordered items

To delete all items from a dictionary you can
	use the clear() method

If each row in a list of lists has exactly two columns, you can convert it to a dictionary by using the
	dict() constructor

pet = pets\["bird"]
print(pet\["color"], pet\["type"])
	green parrot



