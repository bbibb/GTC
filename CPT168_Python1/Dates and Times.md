
common methods:
	date.today()
	datetime.now()

Constructors:
	date(year, month, day)
	time(hour, min, sec, msec)
	datetime(year, month, day, hour, min, sec, msec)

from datetime import date, time, datetime
aware or naive of time zones and dst
	add optional tzinfo argument


**create datetime objects**
strptime()
	string representation of the date and time
	format string that specifies what each part represents
	%d
	%m
	%y
	%Y (4 digit)
	%H
	%M
	%S


fstrings to format dates and times
	print(f"{halloween:%Y-%m-%d}")

strftime()
	accepts a single argument - a format string

**work with spans of time**
timedelta class constructor creates timedelta object
	7 possible arguments
	stores a **span of time**
	adjust a datetime object by adding or subtracting a timedelta object

from datetime import timedelta

timespan = timedelta(weeks=2, days=3, minutes=14)

three_hours_from_now = datetime(now) - timedelta(hours=3)

you can get a timedelta object by subtracting one date/time object from another

**Getting date and time parts using attributes**
attributes (read only)
	year
	month
	day
	hour
	minute
	second
	microsecond

halloween = datetime(1988, 10, 31, 14, 32, 30)
year = halloween.year - 1998

today = date.today()
if (today.month == 10 and today.day == 31):
	print("Happy Halloween")

compare date/time objects with comparison operators

if date.one > date.two




