
CSV comma separated values

text file
binary file

1. open
2. write
3. close

RAM - main memory
disk file - persistant data storager

error in file IO leads to exception

Open and Close
open(file, mode)
	r
	w
	a
	b

close(file)

with statement
	automatically closes a file when you're done
	with open(file, mode) as file_object:
		statements

write(str)

with open("members.txt", "w") as file:
	file.write("John Cleese\\n")

	data is written from main memory to a file


Read a text file
FOR LOOP
with open("members.txt") as file:
	for line in file:
		print(line, end="")
	print()


read entire file as a string
	with open...:
		contents = file.read()
		print(contents)

as a list
	with open...:
		members = file.readlines()
		print(members[0], end="")
		print(members[1])

READLINE()
use this for large files


List in a text file
remove the new line character with replace()

before writing non-string to a textfile, write() converts to string
	an f-string statement
	later, convert back to original when you use it with append(int(line))

with open("years.txt", "w") as years_file:
	for year in years:
		years_file.write(f"{year}\\n")


CSV Files
stores tabular data
	rows and columns
	also, records and fields
csv module

reader(file)
with open("movies.csv", newline="") as file:
	reader = csv.reader(file)
	for row in reader:
		print(f"{row[0]} ({row[1]})")


open() with newline as "universal newlines mode"
	fixes cross-platform issues

writer(file)
	writer  function object converts data in comma-separated values

writerows(rows)
	a method of the CSV writer object
	writes specified rows to the file using CSV format

To read a csv file
	reader() to get a reader object for the file
	for loop to get each row
		in loop, print displays each row

csv module adds double quotes to fields that have special characters and commas
	you can also set a custom separator
optional arguments
	quoting=csv.QUOTE_MINIMAL
	quotechar='"'
	delimiter=","

Binary files

pickle module
dump(object, bfile)
	saves object such as list to a binary file
	in Python called pickling and unpickling
		(usually called serializing and deserializing)
load(bfile)
	reads an object from a binary file

open() in rb mode (read binary)
wb write binary


