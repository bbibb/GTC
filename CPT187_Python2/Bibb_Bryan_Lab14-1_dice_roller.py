#!/usr/bin/env Python3
# Bryan Bibb, CPT187-W12, Jan 17, 2024
# Program: Dice Roller
# Purpose: Returns a dice roll based on user input for the number of dice to roll.
# Related File: dice.py class file

# import classes from dice module
from dice import Dice, Die

# Draw welcome art by looping through 6 possible die values for the die.image property
def main():
    print("The Dice Roller program")
    for i in range(1, 7):
        die = Die()
        die.value = i
        print(die.image)
    print()

    # get number of dice from user. Error message and restart if invalid value
    try:
        count = int(input("Enter the number of dice to roll: "))
    except ValueError:
        print("Invalid number. Please enter an integer between 1 and 6.")
        main()

    # create Die objects and add to Dice object
    dice = Dice()
    # count variable from the user input above
    for i in range(count):
        # create each die in the loop
        die = Die()
        # add each die to the list of dice
        dice.addDie(die)

    # enable repeat rolling
    choice = "y"
    while choice.lower() == "y":        
        # roll the dice
        # process the dice list created in the above section
        dice.rollAll()

        # display to user
        print("YOUR ROLL: ", end="")
        # print each die value to the console
        for die in dice.list:
            print(die.image)
        # print the total sum of dice value
        print("Total:", dice.getTotal())
        print()

        print("\n")

        # ask for user choice to roll again
        choice = input("Roll again? (y/n): ")
        
    print("Bye!")


if __name__ == "__main__":
    main()
