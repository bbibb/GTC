# Bryan Bibb, January 21, 2004, CPT187-W12
# Program:  Temperature Converter
# Purpose:  Converts user input Celsius temperatures to Fahrenheit, and
#           vice versa.
# Related: convert_temperatures.py

# dataclass decorator enables data object
from dataclasses import dataclass

@dataclass

# class has two hidden attributes, both of float data type
class Temp:
    __fahrenheit:float = 32
    __celsius:float = 0

    # method to set the fahrenheit value and convert it to celsius
    def setFahrenheit(self, fahrenheit):
        # standard formula
        self.__celsius = (fahrenheit - 32) * 5/9
        self.__fahrenheit = fahrenheit

    # method to set the celsius value and conver it to fahrenheit
    def setCelsius(self, celsius):
        self.__celsius = celsius
        self.__fahrenheit = celsius * 9/5 + 32

    # method to round and return fahrenheit value
    def getFahrenheit(self):
        return round(self.__fahrenheit, 2)

    # method to round and return celsius value
    def getCelsius(self):
        return round(self.__celsius, 2)

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    # create object from Temp class
    temp = Temp()
    # three test values for fahrenheit
    for f in range(0, 212, 40):
        # for each value, set fahrenheit, convert to celsius, and print both.
        temp.setFahrenheit(f)
        print(temp.getFahrenheit(), "Fahrenheit equals", temp.getCelsius(), "Celsius")

    # three test values for celsius
    for c in range(0, 100, 20):
        # for each value, set celsius, convert to fahrenheit, and print both
        temp.setCelsius(c)
        print(temp,getCelsius(), "Celsius equals", temp.getFahrenheit(), "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

