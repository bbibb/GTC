#!/usr/bin/env python3
# Bryan Bibb, Feb 16, 2024, CPT187-W12
# Program: Lab 18-1 Future Value with GUI
# This program calculates the future value of an investment based on user-input monthly investment
# amount and interest rate. This version implements a tkinter GUI for the front-end.

# import GUI classes from tkinter and locale
import tkinter as tk
from tkinter import ttk, messagebox 
import locale

# import Investment class from business.py
from business import Investment

#***************************
# beginning of GUI section *
#***************************
# This class draws the root window which contains two Frame objects and an exit button
class FutureValueFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # grid() method places the windows side by side
        FutureValueFrame(parent).grid(row=0, column=0)
        FutureValueFrame(parent).grid(row=0, column=1)

        (ttk.Button(parent, text="Exit", command=parent.destroy).grid(row=1, column=1, sticky=tk.E, padx=10, pady=10))

# initialize each frame in the root window with needed variables and methods
class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.investment = Investment()
        self.message = ""
        
        locale.setlocale(locale.LC_ALL, 'en_US')

        # Define string variables for text fields for investment, rate, years, and future value.
        self.monthlyInvestment = tk.StringVar()
        self.yearlyInterestRate = tk.StringVar()
        self.years = tk.StringVar()
        self.futureValue = tk.StringVar()

        self.initComponents()

# function to create label and entry objects from the ttk Label() and Entry() constructors.
    def initComponents(self):
        # Display the grid of labels and text entry fields
        # each label and entry pair are tied to a specific name and string variable.
        ttk.Label(self, text="Monthly Investment:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(
            column=1, row=0)

        ttk.Label(self, text="Yearly Interest Rate:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.yearlyInterestRate).grid(
            column=1, row=1)

        ttk.Label(self, text="Years:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
            column=1, row=2)

        ttk.Label(self, text="Future Value:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.futureValue,
                  state="readonly").grid(
            column=1, row=3)

        # calling function to create button objects
        self.makeButtons()
        # winfo_children() returns a list of widgets. Each one is given x and y padding values.
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

# function to create button objects with ttk Button() constructor.
    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=1, row=0, padx=5)
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=0, row=0)

#****************************
#    end of GUI section     *
#****************************

# ****************************
# beginning of program logic *
# ****************************

# receive float input from the user and validate
    def get_float(self, val, fieldName):
        try:
            return float(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid number.\n"

# receive int input from the user and validate
    def get_int(self, val, fieldName):
        try:
            return int(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid whole number.\n"

# use the attribute definitions and CalculateFutureValue() method in the Investment class
    def calculate(self):
        self.message = "" # clear any previous error message

    # set atrribute values
        self.investment.monthlyInvestment = self.get_float(
            self.monthlyInvestment.get(), "Monthly investment")
        self.investment.yearlyInterestRate = self.get_float(
            self.yearlyInterestRate.get(), "Yearly interest rate")
        self.investment.years = self.get_int(
            self.years.get(), "Years")

    # set currency type and calculate the future value
        if self.message == "": # no errors
            self.futureValue.set(locale.currency(
                self.investment.calculateFutureValue(), grouping=True))
        else:
            messagebox.showerror("Error", self.message)

# reset function
    def clear(self):
        self.monthlyInvestment.set("")
        self.yearlyInterestRate.set("")
        self.years.set("")
        self.futureValue.set("")

#main function to run the program with root window object
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    FutureValueFrames(root)
    root.mainloop()
