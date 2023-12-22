#!/usr/bin/env python3
# Bryan Bibb, Nov 10, 2023, CPT168-434
# Program:      Invoice
# Purpose:      Recieves user input of an invoice data, and caluates the
#               due date (one month after the invoice date), and compares
#               the due date to the current date, returning the number of
#               days overdue or until the due date.


# import date functions
from datetime import datetime, timedelta, date


# receive and process user input of invoice date
def get_invoice_date():
    # use loop to validate the user input
    while True:
        invoice_date_str = input("Enter invoice date (MM/DD/YYYY): ")

        # validation: if the format is incorrect, handle exception and restart.        
        try:
            # create datetime object from user input
            date_time = datetime.strptime(invoice_date_str, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format! Try again.")
            continue

        # create date object from datetime object
        invoice_date = date(date_time.year, date_time.month, date_time.day)

        # if invoice date is in the past, print error and restart loop
        if invoice_date > date.today():
            print("Invoice date must be today or earlier. Try again.")
        else:
            return invoice_date    # final date object returned after validation


def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    # loop repeats when user enters 'y'
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue based on timedelta = 30 days
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        
        # calculate overdue days
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            # multiple by -1 because the result of the subtraction is a negative number
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")  


if __name__ == "__main__":
    main()
