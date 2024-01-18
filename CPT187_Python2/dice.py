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
    __value:int = 1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value < 1:
            raise ValueError("Die value can't be less than 1.")
        else:
            self.__value = value

    # method to roll the die by assigning a random number between 1 and 6
    def roll(self):
        self.__value = random.randrange(1, 7)

# create the Dice class
class Dice:
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        return tuple(self.__list)
                
    def rollAll(self):
        for die in self.__list:
            die.roll()
