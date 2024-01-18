#!/usr/bin/env Python3
# Bryan Bibb, CPT187-W12, Jan 17, 2024
# Program: Dice Roller
# Purpose: Returns a dice roll based on user input for the number of dice
# Related File: dice.py class file

# import classes from dice module
from dice import Dice, Die

# mail function to draw welcome art and call function
def main():
    print("The Dice Roller program")
    print(" _____ \n" + \
          "|     |\n" + \
          "|  o  |\n" + \
          "|_____|")
    print(" _____ \n" + \
          "|o    |\n" + \
          "|     |\n" + \
          "|____o|")    
    print(" _____ \n" + \
          "|o    |\n" + \
          "|  o  |\n" + \
          "|____o|")
    print(" _____ \n" + \
          "|o   o|\n" + \
          "|     |\n" + \
          "|o___o|")          
    print(" _____ \n" + \
          "|o   o|\n" + \
          "|  o  |\n" + \
          "|o___o|")
    print(" _____ \n" + \
          "|o   o|\n" + \
          "|o   o|\n" + \
          "|o___o|")
    print()

    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Die objects and add to Dice object
    dice = Dice()
    # count variable from the user input above
    for i in range(count):
        # create each die in the loop
        die = Die()
        # add each die to the collection of dice
        dice.addDie(die)

    # enable repeat rolling
    choice = "y"
    while choice.lower() == "y":        
        # roll the dice
        # process the dice collection created in the above section
        dice.rollAll()

        # display to user
        print("YOUR ROLL: ", end="")
        # print each die value to the console
        for die in dice.list:
            print(die.value, end=" ")
        print("\n")

        # ask for user choice to roll again
        choice = input("Roll again? (y/n): ")
        
    print("Bye!")


if __name__ == "__main__":
    main()
