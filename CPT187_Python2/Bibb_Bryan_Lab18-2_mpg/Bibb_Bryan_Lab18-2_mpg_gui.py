#!/usr/bin/env python3
# Bryan Bibb, Feb 16, 2024, CPT187-W12
# Program: Miles Per Gallon, GUI version
# Purpose: Calculates the miles per gallon of a trip based on user input of gallons used and miles driven.
#          Implements a tkinter GUI for the application.

# import GUI classes
import tkinter as tk
from tkinter import ttk, messagebox

# Frame class draws the application window with string variable attributes and GUI objects including
# label, entry fields, and a submit button.
class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.message = ""
        self.pack()

        # Define string variables for text entry fields
        self.miles_driven = tk.StringVar()
        self.gallons_used = tk.StringVar()
        self.miles_per_gallon = tk.StringVar()

        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.miles_driven).grid(column=1, row=0)
        ttk.Label(self, text="Gallons of Gas Used:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gallons_used).grid(column=1, row=1)
        ttk.Label(self, text="Miles Per Gallon").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.miles_per_gallon).grid(column=1, row=2)
        ttk.Button(self, text="Calculate", command=self.calculate).grid(column=1, row=3, sticky=tk.E)

# winfo_children returns a list of widgets, and each is given x and 7 padding values.
        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

# method to receive float values and validate them
    def get_float(self, val, field):
        try:
            return float(val)
        except ValueError:
            self.message = f"{field} is not a number.\n"

# method for application logic
    def calculate(self):
        self.message = ""
# get the user input values from the two attributes
        miles_driven = self.get_float(self.miles_driven.get(), "Miles Driven")
        gallons_used = self.get_float(self.gallons_used.get(), "Gallons Used")

# calculate the mpg with simple division and rounding
        if self.message == "":
            mpg = miles_driven / gallons_used
            mpg = round(mpg, 2)

            self.miles_per_gallon.set(mpg)
# error message if for example, someone enters 0 for the gallons_used.
        else:
            messagebox.showerror("Error", self.message)

# main function to create root window object and call the mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    MyFrame(root)
    root.mainloop()
