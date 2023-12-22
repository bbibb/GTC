
exception is thrown
error message called stack trace
exception handling

ValueError exception
	invalid literal for int()
	float()

runtime error - throwing an exception


try statement
	try clause
	except clause

try:
	statements
except [ExceptionName]
	statements

Exception class is most general type of exception
	parent class of child OSError and ValueError
OSError is parent class of specific cases:
	FileExistsError and FileNotFoundError

code from most specific to most general
	except FileNotFoundError:
	except OSError:
	except Exception:

use as keyword to get information from exception
	as (exception object)
	use that name in a print function

also can use type() to get the kind of exception
	type(object)
sys.exit() function of sys module stops the execution of the program
	exits python program

finally clause
	executed no matter what before program closes
		clean up system resources

raise an exception
	for testing
	to raise it again and pass to calling function after you've done something with it like log_exception(e)

	raise ExceptionName("Error message")


