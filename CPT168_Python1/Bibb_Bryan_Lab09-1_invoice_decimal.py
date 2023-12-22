#!/usr/bin/env python3
# Bryan Bibb, Oct 29, 2023, CPT168-434
# Program:      The Invoice Program
# Purpose:      This program takes user input for the order total, calculates the
#               appropriate discount based on the entered value, applies that discount
#               to the subtotal, adds calculated sales tax  and shipping costs to the subtotal,
#               and then returns the discount amount, order subtotal, sales tax, shipping
#               costs and final total amount due.

# import module for decimal math
from decimal import Decimal
from decimal import ROUND_HALF_UP

# import module for currency format and set locale to US
import locale as lc
lc.setlocale(lc.LC_ALL, "en_US")    # Mac format
# lc.setlocale(lc.LC_ALL, "us")     # PC format if needed

# display the program title
print("The Invoice program")
print()

# loop to receive user input, process values, and return results
choice = "y"
while choice == "y":
    
    # get the user entry as a decimal type number, rounded "half up" to 2 digits.
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent based on the magnitude of the entered value
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the discount by multiplying the entered amount * the correct percentage
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
    
    # subtract the discount amount from the total for a subtotal
    subtotal = order_total - discount
    
    # add 5% sales tax, rounded to 2 decimal places
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)

    # calculate and add 8.5% shipping cost, rounded to 2 decimal places
    shipping_percent = Decimal(".085")
    shipping_cost = subtotal * shipping_percent
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    
    # add up the final total
    invoice_total = subtotal + sales_tax + shipping_cost

    # set correct US currency formal for totals, with comma separator
    order_total = lc.currency(order_total, grouping=True)
    invoice_total = lc.currency(invoice_total, grouping=True)

    # set display preferences for strings and currency amounts for totals
    # and calculated values
    format_base = "10,"         # non-total currency amount, with comma
    format_string = 20          # string literals for titles
    format_currency = ">10"     # total currency amounts

    # display the results using variables for formats and for currency values
    print(f"{'Order total:':{format_string}}{order_total:{format_currency}}")
    print(f"{'Discount amount:':{format_string}}{discount:{format_base}}")
    print(f"{'Subtotal:':{format_string}}{subtotal:{format_base}}")
    print(f"{'Sales tax:':{format_string}}{sales_tax:{format_base}}")
    print(f"{'Shipping cost:':{format_string}}{shipping_cost:{format_base}}")
    print(f"{'Invoice total:':{format_string}}{invoice_total:{format_currency}}")
    print()

    # restart the loop if desired
    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
