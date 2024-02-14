
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




## Review

Which will print the value of the \_\_value attribute to the console?
	print(die.getValue())

what is another way to code getArea() method?
	return self.height * self.width

create a read_only property
	coding only a getter method with the @property decorator

**Which of the following is the constructor for this class?**
	**def \_\_init\_\_(self, height:int, width:int):**
		**self.height = height**
		**self.width = width**

**which of the following sets the \_\_value attribute**
	**die.roll()**

what are the attributes of the class?
	num1, num2

to prevent a programmer from directly accessing attributes
	encapsulation

you can't access a private attribute
	by using the dot operator followed by the attribute's name

which defines a constructor that initializes one attribute?
	def init(self, name):
			self.name = name

to code a property with private attribute, which decorator?
	@property

when you define a class, Python generates
	an init() method if you don't code one

if you want to execute code after an object is initialized use
	post_init method

given variable p which refers to Product object, which accesses the price attribute?
	p.price

in a method the first parameter, self, refers to the current
	object

how many public attributes does this class define
	2 - height and width

when this code is executed, what does it print to the screen
	7 x 3 = 21


Which of the following defines the tasks an object can perform?
	methods of a class


the methods contained in an object that has been created from a class is it
	behavior


The Unified Modeling Language
	describes the classes and objects of an application

When an object of one class stores one or more objects of another class this is
	composition

UML class diagram
	describes the attributes and methods of one or more classes

dot operator after an object
	public attributes and methods of the object

code an init() method if you need to
	set the default value to a mutable type


how many public methods does this class define
	3

cust variable, which calls the getFullName() method
	cust.getFullName()

class Customer - which creates a Customer object and assigns it to variable cust1
	cust1 = Customer()

***code a property that sets a private attribute, which of the following decorators?***
	**\@propertyName.setter**
	

module shapes, Rectangle class - import and create object
	from shapes import Rectangle
	rectangle = Rectangle(10,20)


Once you create an object from a class, the object's ----  can change
	state

which defines the type of data an object can store
	attributes of a class

what are the methods of the class
	getProduct()

which defines a data class Product with one attribute
	@dataclass
	class Product:
	name:str = ""




