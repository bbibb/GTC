#!/usr/bin/env python3
# Bryan Bibb, August 28, 2023, CPT168-434, Lab02-3
# Program:  Rectangle Area and Perimeter
# Purpose   Ask for user input for the length and width of
#           the rectangle. Calculate the area and perimeter
#           of the shape, and return those values to the user.

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user for length and width of rectangle
rectangle_length= float(input("Please enter the length:\t"))
rectangle_width = float(input("Please enter the width:\t\t"))

# calculate the area of the rectangle, rounded to 2 digits
rectangle_area = round(rectangle_length * rectangle_width, 2)

# calculate the perimeter of the rectangle, rounded to 2 digits
rectangle_perimeter = round((rectangle_length * 2) + (rectangle_width * 2), 2)
            
# format and display the results
print()
print(f"Area:\t\t\t\t{rectangle_area}")
print()
print(f"Perimeter:\t\t\t{rectangle_perimeter}")
print()
print("Bye!")


