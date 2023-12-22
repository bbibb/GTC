#!/usr/bin/env python3
# Bryan Bibb, September 9, 2023, CPT168
# Program:  Miles Per Gallon
# Purpose:  Take user values for miles driven, gallons of fuel used,
#           and price per gallon; then calculate the miles per gallon (mpg,
#           total gas cost, and cost per mile. Program repeats for
#           multiple trips if desired.

# display a welcome message
print("The Miles Per Gallon program")
print()

choice = "y"
while choice.lower() == "y": 

    # get input from the user for miles, gallons, and price per gallon
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    gas_price = float(input("Enter the cost per gallon:  "))

    # validate each user input as a value greater than zero
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
        print()
        continue
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
        print()
        continue
    elif gas_price <=0:
        print("Cost per gallon must be greater than zero. Please try again.")
        print()
        continue
    else:
        print()
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)

        # calculate and display the cost per mile
        cost_gas = round(gallons_used * gas_price, 2)
        cost_mile = round(cost_gas / miles_driven, 2)
        print("Total Gas Cost:            ", cost_gas)
        print("Cost Per Mile:             ", cost_mile)
        print()

    # ask if user wants to enter another trip
    choice = input("Get entries for another trip? (y/n)?: ")
    print()
    
print("Bye!")



