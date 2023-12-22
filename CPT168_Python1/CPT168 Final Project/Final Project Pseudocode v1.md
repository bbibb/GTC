
Hierarchy Chart

MAIN
	- display main menu
	- update prices
	- list names
	- add person
	- find person
	- edit person
	- delete person
	- display report menu
		- show financial report
		- show seating chart



**Main()**
Initialize Global Constants
	PEOPLE_FILE = [people.csv]
	SEATING_FILE = [seating.csv]
	PRICES_FILE = [prices.csv]
		MEAL_PRICE = [22]
		CHILD_DISCOUNT = [.75]
		COST_CHICKEN = []
		COST_BEEF = []
		COST_VEG = []
		COST_FISH = []
		COST_KOSHER = []
		COST_CHILD = []
		COST_PER_SERVER = []
		COST_VENUE = []

continue = [y]

While true:
Call initial_display
 If the choice is 1:
		update_prices
	If the choice is 2:
		list_names
	If the choice is 3:
		find_person
	If the choice is 4:
		edit_person
	If the choice is 5:
		delete_person
	If the choice is 6:
		report_display
	If the choice is 0:
		break
Print Goodbye


**Initial_Display**
Print header
Print choices:
	1. Update Prices
	2. List names
	3. Add attendee
	4. Find attendee
	5. Edit attendee
	6. Remove attendee
	7. Organizer Reports
	0. Exit
Take user input = choice
Return choice

**update_prices**
print header
load prices file to prices_list
print list formatted
prompt for user input to update each of these
	1.  MEAL_PRICE = [22]
	2. CHILD_DISCOUNT = [0.75]
	3. COST_CHICKEN = []
	3.	COST_BEEF = []
	4. COST_VEG = []
	5. COST_FISH = []
	6. COST_KOSHER = []
	7. COST_CHILD = []
	8. COST_PER_SERVER = []
	9. COST_VENUE = []
	0. Cancel, exit to main menu
for each choice, update the value in the list
write updated list to prices file

**list_names**
read people file to a list
display list with formatting

**find_person**
read people file to a list
prompt for user input = searched_person
if searched_person is in list:
	print record
	print further choices - edit person or exit to main menu
	prompt for user input
		if edit:
			edit_person
		if add:
			add_person
		if delete:
			delete_person
		else:
			exit to main menu
else if not:
	print error message, name not found
	print futher choices - try again or exit to main menu
	if try again:
		find_person
	if not:
		exit to main menu

**add_person**
load people to master list
prompt for input = entered_name
if entered name is in the list:
	print error - already in list
	prompt for further input - try again or exit
	if try again:
		add_person
	else:
		exit to main menu
else if name is not in the list
	name = name
	prompt for meal choice = meal
	display meal options
		if  1, meal = chicken
		if 2, meal = beef
		if 3, meal = vegetarian
		if 4, meal = fish
		if 5, meal = kosher
		if 6, meal = soup and salad
		if 7, meal = child
		if 0 (cancel)
			exit to main menu
	display role options
		if 1, role = member
		if 2, role = guest
		if 3, role = staff
		if 4, role = VIP
		if 5, role = musician
		if 6, role = child
		if 0, (cancel):
			exit to main menu
	prompt for extra donation = donation
		if >0, add to donation total
	write master list to csv
	return to main

**edit_person**
	load people to master list
	prompt for user input = name
	find_person(name)
	if person is not in list:
		print error - not in list
		prompt for further input - try again or exit
		if try again:
			edit_person
		else:
			exit to main menu
	else prompt user input, edit = y/n
		if y:
			get index # of found name
			prompt for new values
			write new values to index #
	write updated master list to csv
	return to main

**delete_person**
load people to master list
	prompt for user input = name
	find_person(name)
	if person is not in list:
		print error - not in list
		prompt for further input - try again or exit
		if try again:
			delete_person
		else:
			exit to main menu
	else prompt user input, delete = y/n
		if y:
			get index # of found name
			delete found name
	write updated master list to csv
	return to main

**report_display**
Print header
Print choices:
	1. List all data
	2. List members, guests, VIP and children
	3. List staff and musicians
	4. Meal report
	5. Financial report
	6. Seating chart
	0. Cancel, back to main menu
Take user input = choice
read People to master list

If choice is 0:
	back to main
Elif choice is 2:
	extract all members, guests, VIP, and children
Elif choice is 3:
	extract all staff and musicians
Elif choice is 4:
	 extract how many of each type of meal
Elif choice is 5:
	financial_report
Elif choice is 6:
	seating_chart

print list formatted
back to report_display


**financial_report**
Print header
load prices file
Calculate costs = cost_list:
	catering = cost of each meal * number of each meal
	servers needed:
		if number of seated adults and children % 10 = 0:
			servers = number / 10
		else
			servers=  (number /10) + 1
	server_cost = servers * COST_PER_SERVER
 calculate cost_sum = 
	 catering + venue_fee + server_cost
Calculate revenue = revenue_list:
	paid_adult_meals * MEAL_PRICE
	paid_child_meals * (MEAL_PRICE * CHILD_DISCOUNT)
	donations
	calculate revenue_sum
total_net = revenue_sum - cost_sum
	print formatted cost_list, revenue_list, total_net

**seating_chart**
load CSV into master list
print header
Unpack (name and meal choice):
	all children into child_list
	all staff and musicians into staff_list
	guests, members, VIPs
Slice lists
	slice child_list into even tables < 6
		how many children?
		how many tables?
		create that many tables
		divide list and put one part into each table
	slice adult_list into even tables < 8
		how many adults?
		how many tables?
		create that many tables
		divide list and put one part into each table
Print tables
	Child tables 1 through
	Adult tables 1 through
	Servers and musicians area (one combined)




NOTES:
add "Update Meals" and let organizer fill in 7 blanks
	call specific one in the add_person function

create a loop in add_person that puts multiple people in a mini-list embedded in the larger list, to keep members and guests together

