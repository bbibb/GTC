#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox

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

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def get_float(self, val, field):
        try:
            return float(val)
        except ValueError:
            self.message = f"{field} is not a number.\n"

    def calculate(self):
        self.message = ""

        miles_driven = self.get_float(self.miles_driven.get(), "Miles Driven")
        gallons_used = self.get_float(self.gallons_used.get(), "Gallons Used")

        if self.message == "":
            mpg = miles_driven / gallons_used
            mpg = round(mpg, 2)

            self.miles_per_gallon.set(mpg)
        else:
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    MyFrame(root)
    root.mainloop()
