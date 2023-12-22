#!/usr/bin/env python3
# Bryan Bibb, Sept 9, 2023, CPT168
# Program:          Future Value Calculator
# Purpose:          Accepts user input of investment amount and terms, and then
#                   calculates and returns total value for each year of the contract.

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":
    # get input from the user

    # get the initital invesment account and validate the data as >0
    valid_data = True               # starts the input loop the first time
    while valid_data == True:               
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0:
            valid_data = False      # breaks out of the loop to continue to next input
        else:
            print("Please enter a value greater than zero.")

    # get the interest rate and validate the data as >0
    valid_data = True               # starts the input loop the first time
    while valid_data == True:   
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate >0:
            valid_data = False      # breaks out of the loop to continue to next input
        else:
            print("Please enter a value greater than zero.")

    # get the number of years and validate the data as >0
    valid_data = True               # starts the input loop the first time
    while valid_data == True:   
        years = int(input("Enter number of years:\t\t"))
        if years >0:
            valid_data = False      # breaks ouf out of the loop to continue with processing
        else:
            print("Please enter a value greater than zero.")
  

    # Process the data entered and display the results

    print()

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12


    # calculate the future value by iterating the investment return for the
    # number of months
    future_value = 0
    for i in range(1, months + 1):      # do not interate month 0 and include the last month
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

        # display the result of each 12 month period (i.e., yearly total)
        if i % 12 == 0:                 # print results for each even year
            print(f"Year {i // 12}\t\tFuture value:\t\t{round(future_value, 2)}")


    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
