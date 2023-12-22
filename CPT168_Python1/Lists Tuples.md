# Lists and Tuples
## List Index


**get** and **set** values of items in the list
Get
	list_name[index#]
Set
	list[index#] = value
	

scores = [0] * 5  [0, 0, 0, 0, 0]

Getting
scores = [99, 90, 85, 80, 75]
	scores[0] = 99
	scores[-5] = 99
	scores[2] = 85
	scores[-3] = 85

Setting
scores = [99, 90, 85, 80, 75]
	scores[4] = 50
	scores = [99, 90, 85, 80, 50]

## Add and remove items

append(item) - adds to end, increases length by 1
insert(index, item) - inserts at specific point, increases by 1
remove(item) - removes, decreases length by 1
index(item) - returns the index number of 
pop([index]) - arg is optional, without it removes last item and returns it

scores = [100, 95, 90, 85, 80]
scores.append(75)
	scores = [100, 95, 90, 85, 80, 75]
scores.insert(3, 75)
	scores = [100, 95, 90, 75, 85, 80]
scores.remove(90)
	scores = [100, 95, 85, 80]

scores = [100, 95, 90, 85, 80]
item = scores.pop()
	item = 80
	scores = [100, 95, 90, 85]

scores = [100, 95, 90, 85, 80]
i = scores.index(80)
scores.pop(i)
	i = 4
#	scores = [100, 95, 90, 85]


## Process items in a list

len(list) - returns length of the list (# of items)

scores = [100, 95, 90, 85, 80]
item = 80
if item in scores:
	scores.remove(item)
	# scores = [100, 95, 90, 85]

print(scores)

**for loop**
scores = [100, 95, 90, 85, 80]
total = 0
for score in scores:
	total += score
print(total)
	# total = 450

**while loop**
scores = [100, 95, 90, 85, 80]
total = 0
i = 0
while i < len(scores):
	total += scores[i]
	i += 1
print(total)
	# total = 450

**built-in functions**

enumerate(list[, start=0])
	add a counter to each item in the list
zip(list1, list2,...)
	returns the value of current item of each list

*Three ways to iterate through a list*
1) Counter variable
	i = 1
	for item in inventory:
		print(f"[i]. {item}")
		i +=i

2) range() 
	for i in range(len(inventory)):
		item = inventory[i]
		print(f"{i}. {item}")

3) enumerate()
	for i, item in enumerate(inventory, start=1):
		print(f"{i}. {item}")
		# notice the comma after i. That is new.

inventory = ["staff", "hat", "bread", "potion"]
1. staff
2. hat
3. bread
4. potion

*two lists in parallel*
inventory = ["staff", "hat", "bread", "potion"]
prices = [27, 10, 5, 19]

for item, price in zip(inventory, prices):
	print{f"{item} (${price})"}

staff ($27)
hat ($10)
bread ($5)
potion($19)


## How lists are passed to functions

objects store data
immutable types = str, int, float, bool
	can't change the data in the object

mutable type - list object
	eg, append directly changes the object
pass arguments to functions:
	variable in calling code and argument in function are the same object
	you have to return if immutable -> new object
		value = value * 2
		return value

if a mutable list, the changes are made to the preexisting object, so you don't have to return it.
		list.append(item)  # changed already
	


	

