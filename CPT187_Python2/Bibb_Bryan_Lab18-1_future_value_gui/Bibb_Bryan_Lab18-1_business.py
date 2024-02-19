#!/usr/bin/env python3
# Bryan Bibb, Feb 16, 2024, CPT187-W12
# Program: Lab 18-1 Future Value with GUI
# This program calculates the future value of an investment based on user-input monthly investment
# amount and interest rate. This version implements a tkinter GUI for the front-end.

# dataclass constructor
from dataclasses import dataclass

# 3 attributes for user input, initialized with 0 default values
@dataclass
class Investment():
    monthlyInvestment:float = 0.0
    yearlyInterestRate:float = 0.0
    years:int = 0

# method to calculate value from those attributes
    def calculateFutureValue(self):
        # calculate the percentage interest rate and number of months
        monthlyInterestRate = self.yearlyInterestRate / 12 / 100
        months = self.years * 12

        # add each month's calculate interest revenue to the running total for the range of months
        futureValue = 0
        for i in range(months):
            futureValue += self.monthlyInvestment
            monthlyInterestAmount = futureValue * monthlyInterestRate
            futureValue += monthlyInterestAmount
        # final value
        return futureValue
