# Bryan Bibb, CPT187-W12, January 17, 2024
# Program: Dice class file
# Purpose: Provides the objects with attributes and methods for the Dice Roller program
# Related File: Bibb_Bryan_Lab14-1_dice_roller.py

# import random number generator, and dataclass decorator
import random
from dataclasses import dataclass

# Create Die class for die objects

@dataclass
class Die:
    # default value = 1. All values are private; subsequently set by roll() not by direct assignment
    __value: int = 1

    # initial roll to set value
    def __post_init__(self):
        self.__value = self.roll()

    # value property to return the rolled value
    @property
    def value(self):
        return self.__value

    # setter to set value returned by roll()
    @value.setter
    def value(self, value):
        # error if an invalid number is returned
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        else:
            self.__value = value

    # property to set the image for each die based on its rolled value
    @property
    def image(self):
        if self.__value == 6:
            return " _____ \n" + \
                   "|o   o|\n" + \
                   "|o   o|\n" + \
                   "|o___o|"
        elif self.__value == 5:
            return " _____ \n" + \
                   "|o   o|\n" + \
                   "|  o  |\n" + \
                   "|o___o|"
        elif self.__value == 4:
            return " _____ \n" + \
                   "|o   o|\n" + \
                   "|     |\n" + \
                   "|o___o|"
        elif self.__value == 3:
            return " _____ \n" + \
                   "|o    |\n" + \
                   "|  o  |\n" + \
                   "|____o|"
        elif self.__value == 2:
            return " _____ \n" + \
                   "|o    |\n" + \
                   "|     |\n" + \
                   "|____o|"
        elif self.__value == 1:
            return  " _____ \n" + \
                    "|     |\n" + \
                    "|  o  |\n" + \
                    "|_____|"

    # method to roll the die by assigning a random number between 1 and 6
    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value


# create the Dice class
class Dice:
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)
    def __init__(self):
        self.__list = []

    # addDie method adds a die to the Dice list
    def addDie(self, die):
        self.__list.append(die)

    # attribute to hold the tuple of die values
    @property
    def list(self):
        return tuple(self.__list)

    # The list is populated by rolling the dice once for each die in the addDie() list
    def rollAll(self):
        for die in self.__list:
            die.roll()

    # each die value in the list is added to the tally for an overall total
    def getTotal(self):
        total = 0
        for die in self.__list:
            total += die.value
        return total