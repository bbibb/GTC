#!/usr/bin/env python3
## Bryan Bibb, September 16, 2023, CPT168-434, Lab04-1
## Program:                 Calculate Future Value
## Associated Files:        validation.py
## Purpose:                 Asks for user input for three values: monthy investment amount,
##                          yearly interest rate, and numer of years in an investment. Then
##                          calculates the future value of the investment given the user input
##                          and returns the value at the end of the term.


# validation.py provides the get_float() and get_init() functions
# import validation modules into specified namespace 'v'
import validation as v

# calculate the future value based on user input.
# take the three variables provided by the main() function, perform calculations, and return the
# calculated future value to main() for printing to the console.

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value by iterating over the number of months to add each month's interest
    # income to the total
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    # future_value returned to main()
    return future_value

def main():
# Ask user if they wish to repeat the calculation with new values. Repeat if so, otherwise exit
    choice = "y"
    while choice.lower() == "y":
        # get input from the user via get_float() and get_init() from validation.py. Take three values
        # for each, validate the first entered amount relative to the low and high values, and return the
        # validated numbers to main(). 
        monthly_investment = v.get_float("Enter monthly investment amount:\t\t", 0, 1000)
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t\t\t", 0, 15)
        years = v.get_int("Enter number of years:\t\t\t\t", 0, 50)

        # get and display future value
        # Use the values returned by get_float() and get_init() as the input to calculate_future_value()
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        # print the calculated value, rounded to 2 decimal places
        print(f"Future value:\t\t\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue. if y, restart loop, if no, exit loop
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
##def get_float(prompt, low, high):
##    while True:
##        monthly_amount = float(input(prompt))
##        if monthly_amount <= low:
##            print("Please enter a value greater than", low)
##        elif monthly_amount > high:
##            print("Please enter a value less than or equal to", high) 
##        else:
##            return monthly_amount
##
##def get_int(prompt, low, high):
##    while True:
##        monthly_amount = int(input(prompt))
##        if monthly_amount <= low:
##            print("Please enter a value greater than", low)
##        elif monthly_amount > high:
##            print("Please enter a value less than or equal to", high) 
##        else:
##            return monthly_amount  
        
if __name__ == "__main__":
    main()
