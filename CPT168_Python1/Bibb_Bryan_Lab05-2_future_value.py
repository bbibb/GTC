#!/usr/bin/env python3
# Bryan Bibb, September 23, 2023, CPT168-434, Lab05-2
# Program:          Future Value
# Purpose:          Asks for user input for three values: monthy investment amount,
#                   yearly interest rate, and numer of years in an investment. Then
#                   calculates the future value of the investment given the user input
#                   and returns the value at the end of the term.


# Take user input, set data type as float, and compare with 'low' and 'high' variables
# as defined in the calling function.        
def get_float(prompt, low, high):
    # loop continues until user enters a valid float and then returns it
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")

# Take user input, set data type as int, and compare with 'low' and 'high' variables
# as defined in the calling function.            
def get_integer(prompt, low, high):
    # loop continues until user enters a valid float and then returns it
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")

# calculate the future value based on user input.
# take the three variables provided by the main() function, perform calculations, and return the
# calculated future value to main() for printing to the console.

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = (yearly_interest / 12)
    months = years * 12

    # calculate future value by iterating over the number of months to add each month's interest
    # income to the total
    future_value = 0.0
## one bug was that the range function requires (months + 1) to include the last month
    for i in range(1, months + 1):
        ##print("month #\t\t\t\t\t", i)

        future_value += monthly_investment
        ##print("new future value without interest is\t\t", round(future_value, 2))

## one bug was that the interest rate was not converted to hundreths
        monthly_interest = future_value * (monthly_interest_rate / 100)
        ##print("monthly interest added is\t\t\t", round(monthly_interest, 2))

        future_value += monthly_interest
        ##print("new future value with interest is\t\t", round(future_value, 2))

    # future_value returned to main()
    return future_value

def main():
# Ask user if they wish to repeat the calculation with new values. Repeat if so, otherwise exit
    choice = "y"
    while choice.lower() == "y":
        # get input from the user via get_float() and get_integer() from validation.py. Take three values
        # for each, validate the first entered amount relative to the low and high values, and return the
        # validated numbers to main(). 
 
        monthly_investment = get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        # Use the values returned by get_float() and get_init() as the input to calculate_future_value()

        future_value = round(calculate_future_value(
            monthly_investment, yearly_interest_rate, years), 2)
        
        # print the calculated value, rounded to 2 decimal places
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue; if y, restart loop, if no, exit loop
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
