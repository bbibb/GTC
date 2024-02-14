# Bryan Bibb, January 21, 2004, CPT187-W12
# Program:  Temperature Converter
# Purpose:  Converts user input Celsius temperatures to Fahrenheit, and
#           vice versa.
# Related: temperature.py

# import class from temperature module
from temperature import Temp

# Opening menu
def display_menu():
    print("The Convert Temperatures program")
    print()
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenhit")
    print()

# function to take user input and pass it to the Temp objects
def convert_temp():
    # exception handling to force valid number input
    try:
        option = int(input("Enter a menu option: "))
    except ValueError:
        print("Enter a menu number.")
        main()
    # create Temp() object -> temp
    temp = Temp()
    # exception handling to force valid number input
    if option == 1:
        try:
            # user input of Fahrenheit temperature sent to setFahrenheit
            f = float(input("Enter degrees Fahrenheit: "))
            temp.setFahrenheit(f)

            # getCelsius returned value is printed
            print("Degrees Celsius: ", temp.getCelsius())
        except ValueError:
            print("Enter a valid number.")
            print()
            main()
    elif option == 2:
        # exception handling to force valid number input
        try:
            # user input of Celsius temperature sent to setCelsius
            c = float(input("Enter degrees Celsius: "))
            temp.setCelsius(c)

            # getFahrenheit() returned value is printed
            print("Degrees Fahrenheit: ", temp.getFahrenheit())
        except ValueError:
            print("Enter a valid number.")
            print()
            main()
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    # user choice to continue
    again = "y"
    while again.lower() == "y":
        # initiating user-input function
        convert_temp()
        print()
        
        again = input("Convert another temperature? (y/n): ")
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()
