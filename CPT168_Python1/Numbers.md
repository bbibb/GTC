int
	4 bytes to store integer
float
	8 bytes to store floating-point
	16 significant digits possible
	approximate values, not exact

scientific notation
	decimal value for significant digits
	e and a positive or negative exponent
	2.302e+5

**Math Module**
import math as m

pow(num, pow) 
	raises num to specified power
sqrt(num)
ceil(num)
	rounds floating point number up to nearest integer
floor(num)
	rounds floating point number down to nearest integer
pi constant

m.pow(2, 3)
	8.0

circumference = m.pi * radius * 2

to round to specific decimal place, multiply by 10s then divide by 10s
m. floor(2.0083 * 1000) / 1000.    #2.008

**Format Specifications with f-strings**
colon with format specification
show a certain number of digits
use field widths to align values column

"f{value: format_specification}"
	[field_width comma .decimal_places type_code

d integer
f floating point
% percent
e scientific notation


print(f"{number: .2f}"). #2 decimal places

print(f"{number: , .2f}") # with comma separator

print(f"{number:15 , .2f}")  #15 space field

print(f"{number: .0%}")    # integer with %


**Aligning results**
print(f"{'Description': 15} {'Price' :>10} {'Qty' :>5}")
print(f"{'Hammer': 15} {9.99:10.2f} {3:5d}")

Description           Price      Qty
Hammer                  9.99         3


**locale module**

setlocale(category, locale)
currency(num, grouping])
format(format, num, grouping)

us (Win)
en-US (Mac and WIn)
uk
de

import locale as lc
lc.setlocale(lc.LC_ALL, "us")
lc.setlocale(lc.LC_ALL, "en-US")

currency(num, grouping)
print(lc.currency(12345.15, grouping=True))    # $12,345.15

format(format, num, grouping)
print(lc.format("%d", 12345, grouping=True))    # $12,345
	the format begins with % sign

**fixing rounding errors**

round any results that can have more than 2 decimal places immediately after they are calculated, before they are passed to other arithmetic operations


**decimal() module**

like floating point, except they are exact values
	don't have to worry about unexpected floating point values
slower than floating point, and more complex code
	typically only used with financial calculations

import decimal class
	*from decimal import Decimal*
use constructor to create decimal objects from string values
then use standard arithmetic operations

can't mix floating point and decimal numbers

quantize()
object.quantize(Decimal("positions_code"), rounding constant)

 round decimal values to specified number of decimal places
	default is ROUND_HALF_EVEN, where 10.005 is 10.00 and 10.015 is 10.02
	business math needs ROUND_HALF_UP, where 10.005 is 10.01

	from decimal import Decimal
	order_total = Decimal("100.05")
	discount_percentage = Decimal(".1")
	discount = order_total * discount_percentage   # 10.005

	from decimal import ROUND_HALF_UP
	discount = Decimal("10.005")
	discount = discount.quantize(Decimal"1.00"), ROUND_HALF_UP # 10.01





