#!/usr/bin/env python3
## Bryan Bibb, September 16, 2023, CPT168-434, Lab04-1
## Program:             Validate float and integer input
## Associated File:     Bibb_Bryan_Lab04-1_future_value.py
## Purpose:             Two functions take a value entered by the user,
##                      float and integer respectively, and validate them
##                      as higher or lower than predefined values coded in main().
        

# Take user input, set data type as float, and compare with 'low' and 'high' variables
# as defined in the calling function.
def get_float(prompt, low, high):
    # loop continues until user enters a valid float and then returns it
    while True:
        monthly_amount = float(input(prompt))
        if monthly_amount <= low:
            print("Please enter a value greater than", low)
        elif monthly_amount > high:
            print("Please enter a value less than or equal to", high) 
        else:
            return monthly_amount

# Take user input, set data type as int, and compare with 'low' and 'high' variables
# as defined in the calling function.
def get_int(prompt, low, high):
# loop continues until user enters a valid integer and then returns it
    while True:
        monthly_amount = int(input(prompt))
        if monthly_amount <= low:
            print("Please enter a value greater than", low)
        elif monthly_amount > high:
            print("Please enter a value less than or equal to", high) 
        else:
            return monthly_amount


# test function
def main():
    choice = "y"
    while choice.lower() == "y":
        # test values for low and high float set as 0, 100
        test_float = get_float("Enter the monthly investment:\t", 0, 100)
        print("Test float = ", test_float)
        print()
        # test values for low and high integer set at 0, 10
        test_int = get_int("Enter the number of years:\t", 0, 10)
        print("Test integer = ", test_int)
        print()

        # see if the user wants to continue. If so, restart loop. If not, exit loop
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
        
if __name__ == "__main__":
    main()
