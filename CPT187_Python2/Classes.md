
## Intro to classes and objects

**UML Diagrams for the Product Class**

A class is a template or blueprint from which objects are made.
Attributes define the kind of data it can store
methods define the tasks the object can perform
	eg modify its attributes
Object is an instance of a class - called *instantiation*

Unified Modeling Language UML - OOP standard
	class diagram for *class*
	3 attributes *name*, *price*, *discountPercent*
	3 methods *\_\_init\_\_()*, *getDiscountAmount()*, *getDiscountPrice()*

\_\_init\_\_ is a *constructor* that creates an object from the class and initializes its attributes
	accepts 3 parameters that set the values of the 3 attributes
		parameter = argument

Group related atttributes and methods into data structures called *objects*
	Procedural programming - passes data between a series of functions
	OOP is different

Once you create an object from a class, the object has an identity (memory address), a *state* (the data it stores), and *behavior* (the methods it contains)
	the object's state may change

![[CleanShot 2024-01-16 at 19.46.35@2x.jpg]]
**Code that defines a product class**

import dataclass module
class definition with dataclass decorator
	tells python to generate an init method for the class
*class* keyword, name of class and colon
attribute name colon type hint, default value
public methods
	each has parameter that's a reference to the object itself *self*

**code that uses a product class**

import Product class from objects module
create product objects
	generated constructor initializes attributes to the values passed

define class

	from dataclass import dataclass

	@dataclass
	class Product:
		name:str
		price:float
		discountPercent:int
	def getDiscountAmount(self):
		return self.price * self.getDiscountAmount()
	def getDiscountPrice(self):
		return self.price - self.getDiscountAmount()

create objects

	from objects import Product

	product1 = Product('Hammer', 12.99, 62)
	product2 = Product('Nails', 5.06, 0)


**How to create and use objects**

import

	from objects import Product
create object with required parameters
	correct number, in correct sequence, with compatible data types
get/set attribues

	objectName = ClassName(parameters)
	objectName.attributeName
	product1.discountPercent = 40
	percent = product1.discountPercent # percent = 40
	
calling a method is similar to getting an attribute, but you use ()
method may or may not have parameters

	objectName.methodName(parameters)
	discount = product1.getDiscountAmount()
calling a function is similar to calling a method
	but must preface method with name of the object and .dot operator

## How to define a class

default values not required but a good idea

use decorator to create a data class
	decorator uses @symbol @dataclass
	assigned default values for attributes
	Python creates a constructor  with type hints

	from dataclasses import dataclass

	@dataclass
	class Product:
		name:str = ""
		price:float = 0.0
		discountPercent:int = 0
can also code the constructor yourself
	code init method
	self parameter as reference to the object itself
		access the attributes and methods from within the class
		not visible to calling code, so don't supply a value
	assign values to init parameters

	class Product:
		def \_\_init\-\-(self, name = "", price = 0.0, discountPercent = 0):
			self.name = name
			self.price = price
			self.discountPercent = discount_percent

usually use data classes, code is simpler
	might make your own init
	or might use data class for attributes and post_init() method for other initialization (executes after the init)
	code any attributes with default values that are a mutable type (list or dict)
		data classes don't allow attributes with default values that are mutable



**How to code methods**

only difference is that the first parameter must be a reference to the object itself

within the body, use the self parameter to access the object's attributes
	use those attributes to do something
	return the value to the calling code

	def methodName(self[, paramters]):
		statements

	def getDiscountAmount(self):
		return self.price * self.discountPercent / 100

	def getDiscounPrice(self):
		return self.price - self.getDiscountAmount()
call it
	discountPrice = product.getDiscountPrice

with a parameter

	def getPriceStr(self, country):
		priceStr = f"{self.price:.2f}"
		if country == "US":
			priceStr += " USD"
		elif country = "DE":
			priceStr ++ " EUR":
		return priceStr

	prince(f"Price: {product.getPriceStr("US")}")

don't forget to include self parameter
don't forget to prefix self parameter to attribute names
	(if you don't you've just created a local variable with that name)


