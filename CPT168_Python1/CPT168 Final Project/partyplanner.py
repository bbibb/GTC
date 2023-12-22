#! /usr/bin/env python3
# Bryan Bibb, Fall 2023, CPT168-434
# Program:      Party Planner
# Purpose:      Allows banquet planners to organize their event by adding and tracking attendees
#               (adding, editing, and deleting) along with their meal options, total
#               cost of their meal and optional contributions, and seating chart.
#               Also provides comprehensive financial and catering reports.

import sys, csv                         # sys provides exit() function
from csv import reader as csvreader     # for reading and writing data
import random                           # for shuffling seating chart


def menu_display():
    print()
    print("*********************************************")
    print("*               Party Planner               *")
    print("*********************************************")
    print()
    print("1.   Update Prices")
    print("2.   List Attendees")
    print("3.   Find Attendee Information")
    print("4.   Add Attendee Information")
    print("5.   Edit Attendee Information")
    print("6.   Delete Attendee Information")
    print("7.   Organizer Reports Menu")
    print("0    Exit Program")
    print()


def main():
    # data files for saving information as it is entered/changed
    people_file = ["partyplanner.csv"]
    prices_file = ["prices.csv"]

    # open CSV file and convert to a list of prices for use with data input
    with open("prices.csv", 'r') as prices:
        reader = csv.reader(prices)
        price_list = list(reader)

    childs_cost = float(price_list[0][1]) * float(price_list[1][1])
    childs_cost = float(childs_cost)

    print()
    # menu loop displays each time after a selection is finished
    while True:
        print()
        menu_display()    
        while True:
            try:
                command = int(input("Enter a menu number: "))
                if command in (1, 2, 3, 4, 5, 6, 7, 0):
                    break
                else:
                    continue
            except:
                print("Please enter a valid number.")
            
        if command == 1:
           # try:
                # the variables in the prices.csv file can be updated by the administrator
            update_prices()
           # except:
            #    continue
            
        elif command == 2:
            try:
                list_names()
            except:
                continue
        elif command == 3:
            try:
                # search only for last name; all matching entries will display
                find_name = input("Enter the last name of the attendee you wish to find: ")
                find_person(find_name)
            except:
                continue
        elif command == 4:
            # input for new entry is passed to the add_person() function
            print()
            print("Enter the information for the new attendee: ")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            # validate input for role and meal to preserve data integrity
            while True:
                role_type = input("Role/type [member, guest, staff, child]: ")
                if role_type in ("member", "guest", "staff", "child", "VIP", "musician"):
                    break
                else:
                    print("Please enter one of the listed roles.")
            while True:
                meal_type = input("Meal preference [chicken, beef, fish, kosher, vegetarian, vegan, child's] : ")
                if meal_type in ("chicken", "beef", "fish", "kosher", "vegetarian", "vegan", "childs"):
                    break
                else:
                    print("Please enter one of the listed meals.")
            while True:
                try:
                    payment = float(input(f"Enter the amount paid: adult: {price_list[0][1]:.2} or child's meal: {childs_cost:.2f} "))
                    break
                except:
                    print("Please enter a proper monetary value without the $ symbol.")
                    continue
            add_person(first_name, last_name, role_type, meal_type, payment)
           
            
        elif command == 5:
            try:
                print()
                # search for full name to prevent match collisions
                to_edit = input("Enter the full name of the attendee you would like to edit: ")
                edit_person(to_edit)
            except:
                continue
        elif command == 6:
            try:
                print()
                # search for full name to prevent match collisions
                to_delete = input("Enter the full name of the attendee you would like to delete: ")
                delete_person(to_delete)
            except:
                continue
        elif command == 7:
            # second menu for administrative reports
            report_display()
            
        elif command == 0:
            # exit command
            sys.exit()
        else:
            print("Please enter a menu number.")


def report_display():
    

    while True:
        print()
        print("*********************************************")
        print("*               Reports Menu                *")
        print("*********************************************")
        print("1.   List all attendee data")
        print("2.   Attendee Type and Meals Report")
        print("3.   Financial Report")
        print("4.   Seating Chart")
        print("0.   Back to Main Menu")
        print()
        print()
        try:
            command = int(input("Enter a menu number: "))
        except:
            print("Please enter a valid number.")
        if command == 1:
            # lists all of the attendee data
            list_all()
        elif command == 2:
            # how many of each meal is required
            meal_report()
            # calculation of money collected, paid, and profit from the event
        elif command == 3:
            financial_report()
        elif command == 4:
            # random division of the group into 8-person tables
            seating_chart()
        elif command == 0:
            main()
        else:
            print("Please enter a menu number.")


def update_prices():
    # open CSV file and convert to a list of prices
    with open("prices.csv", 'r') as prices:
        reader = csv.reader(prices)
        price_list = list(reader)
        
    # price list is a list of two-value lists, accessed via index    
    print()
    print("Select an item to update prices or event costs ")
    print(f"1. Meal Price = ", price_list[0][1])
    print(f"2. Child Discount = ", price_list[1][1])
    print(f"3. Cost of chicken meal = ", price_list[2][1])
    print(f"4. Cost of beef meal = ", price_list[3][1])
    print(f"5. Cost of fish meal =", price_list[4][1])
    print(f"6. Cost of kosher meal =", price_list[5][1])
    print(f"7. Cost of vegetarian meal =", price_list[6][1])
    print(f"8. Cost of vegan meal =", price_list[7][1])
    print(f"9. Cost of child's meal =", price_list[8][1])
    print(f"10. Cost to user the venue = ", price_list[9][1])
    print(f"0. Save changes and exit to main menu")
    print()

    
        # exception handling
    while True:
        try:
            command = int(input("Enter a menu number: "))
        except ValueError:
            print("Please enter a valid number.")
        
        # pattern is repeated through this menu
        if command == 1:
            try:
                # user enters new price, which is converted to a float and saved in variable
                m_p = float(input("Enter the new base price for the meal: "))
                # new price placed within the pricelist
                price_list[0][1] = m_p
                #print("Testing"  , price_list[0][1])
                # success report
                print("Price has been changed to ",m_p)                
            except:
                # exception if entry is not a float value
                print("Please enter a valid number.")
                
        # same pattern with different variables repeats
        elif command == 2:
            try:
                c_d = float(input("Enter the new child discount as a decimal: "))
            except:
                print("Please enter a proper decimal number between 0 and 1.")
            # make sure that the value entered is a decimal between 0 and 1
            if c_d > 1 or c_d < 0:
                print("Please enter a decimal number between 0 and 1.")            
            else:
                price_list[1][1] = c_d
                # success message displays decimal in percent format
                print(f"Child Discount has been changed to {c_d:.0%}")
                
        # pattern repeats from here to end   
        elif command == 3:
            try:
                c_chicken = float(input("Enter the new cost of the chicken meal. "))
                price_list[2][1] = c_chicken
                print("The cost of the chicken meal has been changed to ", c_chicken)
            except:
                print("Please enter a valid number.")
                
        elif command == 4:
            try:
                c_beef = float(input("Enter the new cost of the beef meal. "))
                price_list[3][1] = c_beef
                print("The cost of the beef meal has been changed to ", c_beef)
            except:
                print("Please enter a valid number.")
                
        elif command == 5:
            try:
                c_fish = float(input("Enter the new cost of the fish meal. "))
                price_list[4][1] = c_fish
                print("The cost of the fish meal has been changed to ", c_fish)
            except:
                print("Please enter a valid number.")
                
        elif command == 6:
            try:
                c_kosher = float(input("Enter the new cost of the kosher meal. "))
                price_list[5][1] = c_kosher
                print("The cost of the kosher meal has been changed to ", c_kosher)
            except:
                print("Please enter a valid number.")
                
        elif command == 7:
            try:
                c_veg = float(input("Enter the new cost of the vegetarian meal. "))
                price_list[6][1] = c_veg
                print("The cost of the child meal has been changed to ", c_veg)
            except:
                print("Please enter a valid number.")
                
        elif command == 8:
            try:
                c_vegan = float(input("Enter the new cost of the vegan meal. "))
                price_list[7][1] = c_vegan
                print("The cost of the server meal has been changed to ", c_vegan)
            except:
                print("Please enter a valid number.")

        elif command == 9:
            try:
                c_child = float(input("Enter the new cost of the child's meal. "))
                price_list[8][1] = c_child
                print("The cost of the child's meal has been changed to ", c_child)
            except:
                print("Please enter a valid number.")        
                
        elif command == 10:
            try:
                c_venue = float(input("Enter the new venue rental cost. "))
                price_list[9][1] = c_venue
                print("The cost of the venue rental has been changed to ", c_venue)
            except:
                print("Please enter a valid number.")
                
        else:
            # once all changes have been made, save updated information to CSV
            with open("prices.csv", 'w') as file:
                writer = csv.writer(file)
                writer.writerows(price_list)
            # back to main menu
            main()
            

def list_names():
    # open CSV file
    with open("partyplanner.csv", newline="") as file:
        attendees_list = csv.reader(file)
        
        # sort alphabetically
        attendees_list = sorted(attendees_list)
        
        # Names and roles printed in tabular format
        print("*********************************************")
        print()
        print("-------------------------------------------------")
        print(f"|   {'Last Name':12} |   {'First Name':12} |  {'Type'}\t|")
        print("-------------------------------------------------")
        for row in attendees_list:
            print(f"|   {row[2]:12} |   {row[1]:12} |   {row[3]}\t|")
        print("-------------------------------------------------")


def find_person(find_name):
    # open CSV and convert to sorted list
    with open("partyplanner.csv", newline="") as file:
        attendees_list = sorted(list(csv.reader(file)))
        
    # variables to help with search loop
    found = 'n'
    found_list = []
    
    # loop through the list from start to finish
    for i in range(len(attendees_list)):
        # if name is found, mark it 'y' and append to results list
        if find_name in attendees_list[i][2]:
            found_list.append(attendees_list[i][1:])
            found = 'y'
            
    # message if not found
    if found == 'n':
        print()
        print("Name not found in the attendees list.")
        
    # after iteration is completed, the results list is printed    
    elif found == 'y':
        print("*********************************************")
        print("              Attendee(s) found:                ")
        # there may be 1 or more entries to print
        for row in found_list:
            print(f"{row[0]:15} {row[1]:15} {row[2]}")
        print("*********************************************")
        print()

def add_person(first_name, last_name, role_type, meal_type, payment):
    with open("partyplanner.csv", newline="") as file:
        attendees_list = sorted(list(csv.reader(file)))

    # create a nameID value from last name and first initial
    nameID = last_name + first_name[0]

    # create a new person entry with entered user data and the name ID
    new_person = [nameID, first_name, last_name, role_type, meal_type, payment]
    # print(new_person)

    # add the new person to the list
    attendees_list.append(new_person)

    # print(attendees_list)
    # write updated list back to the CSV file
    with open("partyplanner.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(attendees_list)


def delete_person(to_delete):
    with open("partyplanner.csv", newline="") as file:
        attendees_list = sorted(list(csv.reader(file)))
    # split the entered full name into a 2-word list
    found = 'n'
    to_delete = to_delete.split()
    
    # loop through list to identify the full name, first and last
    for i in range(len(attendees_list)):
        # if the first and last name are matched, show and ask for confirmation
        if to_delete[0] in attendees_list[i][1] and to_delete[1] in attendees_list[i][2]:
            found = 'y'
            print("*********************************************")
            print("              Attendee found:                ")
            print(f"{attendees_list[i][1]} {attendees_list[i][2]}: {attendees_list[i][3]}, {attendees_list[i][4]}")
            print("*********************************************")
            print()
            choice = input("Are you sure you would like to delete this attendees? Y/N ")
            if choice.lower() in ["y", "yes"]:
                # remove identified name via pop()
                attendees_list.pop(i)
                print(f"Attendee deleted from the list...")
                # break from loop once the name has been found
                break
            elif choice.lower() in ["n", "no"]:
                break
            else:
                print("Please enter Y or N. ")
                
    # if found is not changed to 'y', print an error message
    if found == 'n':
        print()
        print("Name not found in list")

    # write updated list back to CSV file
    with open("partyplanner.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(attendees_list)

def edit_person(to_edit):
    # the same basic find process as the delete_person function
    with open("partyplanner.csv", newline="") as file:
        attendees_list = sorted(list(csv.reader(file)))
        
    # initialize variable to test whether name was found
    found = 'n'
    to_edit = to_edit.split()
    for i in range(len(attendees_list)):
        if to_edit[0] in attendees_list[i][1] and to_edit[1] in attendees_list[i][2]:
            found = 'y'
            print("*********************************************")
            print("              Attendee found:                ")
            print(f"{attendees_list[i][1]} {attendees_list[i][2]}: {attendees_list[i][3]}, {attendees_list[i][4]}, {attendees_list[i][5]}")
            print("*********************************************")
            print()
            choice = input("Are you sure you would like to edit this attendee? Y/N ")
            print()

            # process found name by receiving new input for each variable. Old data included for reference.
            if choice.lower in ["y", "yes"]:
                # go through the input process, replacing values in the list with new values
                attendees_list[i][1] = input(f"{attendees_list[i][1]}: First name: ")
                attendees_list[i][2] = input(f"{attendees_list[i][2]}: Last name: ")
                # while loop for data validation
                while True:
                    attendees_list[i][3] = input(f"{attendees_list[i][3]}: Role/type [member, guest, staff, child, VIP]: ")
                    if attendees_list[i][3] in ("member", "guest", "staff", "child", "VIP", "musician"):
                        break
                    else:
                        print("Please enter one of the listed roles.")
                # while loop for data validation
                while True:
                    attendees_list[i][4] = input(f"{attendees_list[i][4]}: Meal preference [chicken, beef, fish, kosher, vegetarian, vegan, child's]: ")
                    if attendees_list[i][4] in ("chicken", "beef", "fish", "kosher", "vegetarian", "vegan", "childs"):
                        break
                    else:
                        print("Please enter one of the listed meals.")
                try:   
                    attendees_list[i][5] = float(input(f"{attendees_list[i][5]}: Payment Amount: "))
                except:
                    print("Please enter a valid monetary amount.")
                break
            # abort editing
            elif choice.lower() in ["n", "no"]:
                break
            # if user enters value other than n/no or y/yes
            else:
                print("Please enter Y or N.")
            
    # if name is not found, print an error message
    if found == 'n':
        print()
        print("Name not found in list")
        
    # write back to CSV
    with open("partyplanner.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(attendees_list)

def list_all():
    with open("partyplanner.csv", newline="") as file:
        attendees_list = sorted(list(csv.reader(file)))
    # insert a header for display purposes
    
    header_list = ["NAME_ID", "FIRST NAME", "LAST NAME", "ROLE/TYPE", "MEAL CHOICE", "PAYMENT"]
    attendees_list.insert(0, header_list)
    
    # find max length of each to determine spacing
    n = max(len(x) for l in attendees_list for x in l)
    
    # print each row left justified with two spaces beyond the maximum value needed
    for row in attendees_list:
        print(''.join(x.ljust(n+2) for x in row))

def meal_report():
    with open("partyplanner.csv", newline="") as file:
        attendees_list = sorted(list(csv.reader(file)))
        
    # initialize list for searching
    flat_list = []
    
    # convert array to flat list
    for row in attendees_list:
        flat_list.extend(row)
        
    # count number of meal items in the list
    beef = flat_list.count('beef')
    chicken = flat_list.count("chicken")
    fish = flat_list.count("fish")
    kosher = flat_list.count("kosher")
    veg = flat_list.count("vegetarian")
    vegan = flat_list.count("vegan")
    childs = flat_list.count("childs")

    # count number of attendee types in the list 
    members = flat_list.count("member")
    guests = flat_list.count("guest")
    VIP = flat_list.count("VIP")
    musician = flat_list.count("musician")
    staff = flat_list.count("staff")
    children = flat_list.count("child")
    
    # print results
    print()
    print("*********************************************")
    print("            Attendee Totals:                 ") 
    print(f"Members:\t\t{members}\nGuests:\t\t\t{guests}\nVIPs:\t\t\t{VIP}\nMusicians:\t\t{musician}\
          \nStaff:\t\t\t{staff}\nChildren:\t\t{children}")
    print()
    print("*********************************************")
    print("              Meals Ordered:                 ") 
    print(f"Beef:\t\t\t{beef}\nChicken:\t\t{chicken}\nFish:\t\t\t{fish}\
          \nKosher:\t\t\t{kosher}\nVegetarian:\t\t{veg}\nVegan:\t\t\t{vegan}\nChild's:\t\t{childs}")
    print("*********************************************")
    

def seating_chart():
    with open("partyplanner.csv", newline="") as file:
         attendees_list = sorted(list(csv.reader(file)))
         
    # create a list based on the nameID field
    nameID_list = []
    for row in attendees_list:
        NID = row.pop(0)
        nameID_list.append(NID)
        
    # calculate the number of tables needed with 8 people max per each
    table_count = 1 + len(nameID_list)//8
    print()
    print(f"You will need {table_count} tables.")
    print()

    # randomize the list
    random.shuffle(nameID_list)
    
    # divide the nameID list into a new array with 8 people per inner list
    n = 8
    
    # this line grabs groups of 8 people in as a nested list. It establishes the range
    # from 1 to a number that is more than the total but less than the total plus the
    # table size. In this case, a length of 100 becomes 107 // 8 = 13. It then splits
    # the nameID list into n-sized sized chunks into table_list, in this case [0:8], [8:16], etc.
    table_list = [nameID_list[i * n:(i+1) * n] for i in range((len(nameID_list) + n - 1) // n)]

    # variable to initialize table number
    number = 1
    
    # print randomized and chunked list in sections with Table Number heading
    for row in table_list:
        print("*********************************************")
        print(f"Table {number}: ")
        number += 1
        for item in row:
            print(f"{item[0:]}")
        print("*********************************************")
        print()

def financial_report():
    # open CSV file and convert to a list of prices
    with open("prices.csv", 'r') as prices:
        reader = csv.reader(prices)
        price_list = list(reader)

    # extract the prices for each item into variables
    chicken_cost = price_list[2][1]
    beef_cost = price_list[3][1]
    fish_cost = price_list[4][1]
    kosher_cost = price_list[5][1]
    veg_cost = price_list[6][1]
    vegan_cost = price_list[7][1]
    childs_cost = price_list[8][1]
    facility = price_list[9][1]
    total_revenue = []
    
    # extract the payment column and add rows together for total revenue
    with open("partyplanner.csv", newline="") as file:
        attendees_list = sorted(list(csv.reader(file)))
    # iterate through rows, adding column[5] to total_revenue
    total_revenue = sum(float(row[5]) for row in attendees_list)
                        

    # initialize list for searching
    flat_list = []
    
    # convert array to flat list for counting
    for row in attendees_list:
        flat_list.extend(row)
        
    # count number of each item in the list
    beef = flat_list.count('beef')
    chicken = flat_list.count("chicken")
    fish = flat_list.count("fish")
    kosher = flat_list.count("kosher")
    veg = flat_list.count("vegetarian")
    vegan = flat_list.count("vegan")
    childs = flat_list.count("childs")

    # calculate the total cost per entree
    # multiply the count of each meal times its wholesale cost
    # convert all string variables to float type
    beef = float(beef) * float(beef_cost)
    chicken = float(chicken) * float(chicken_cost)
    fish = float(fish) * float(fish_cost)
    kosher = float(kosher) * float(kosher_cost)
    veg = float(veg) * float(veg_cost)
    vegan = float(vegan) * float(vegan_cost)
    child_total = float(childs) * float(childs_cost)
    
    facility = float(facility)
    total_revenue = float(total_revenue)

    # add cost of each entree for total food costs
    total_cost = beef + chicken + fish + kosher + veg + vegan + child_total

    # add food cost to facility cost for total expenses
    total_expenses = total_cost + facility

    # caluclate final proft by subtracting expenses from revenue
    final_profit = total_revenue - total_expenses
    

    # format and print results
    print("*********************************************")
    print("             Financial Report                ")
    print("*********************************************")
    print(f"Beef cost:\t\t${beef:,.2f}")
    print(f"Chicken cost:\t\t${chicken:,.2f}")
    print(f"Fish cost:\t\t${fish:,.2f}")
    print(f"Kosher cost:\t\t${kosher:,.2f}")
    print(f"Veg cost:\t\t${veg:,.2f}")
    print(f"Vegan cost:\t\t${vegan:,.2f}")
    print(f"Child's cost:\t\t${child_total:,.2f}")
    print("---------------------------------------------")
    print(f"Total food cost:\t${total_cost:,.2f}")
    print()
    print(f"Facility fee:\t\t${facility:,.2f}")
    print()
    print(f"Total Expenses:\t\t${total_expenses:,.2f}")
    print()
    print(f"Total Revenue:\t\t${total_revenue:,.2f}")
    print()
    print("*********************************************")
    print(f"Final Profit:\t\t{final_profit:,.2f}        ")
    print("*********************************************")
    

if __name__ == "__main__":
    main()
