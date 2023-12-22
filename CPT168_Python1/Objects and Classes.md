
When we began to discuss "objects" in Python with their included attributes and methods, I felt well-prepared to dive into object-oriented programming because of our prior work in CPT113 with Alice. In the Alice program, each of the items that you work with is an object, and each object has both attributes and methods associated with it. We learned how to set and change attributes in these objects, and apply instructions to them to make the program elements actually do things. However, I have had to do a good bit of reading to nail down the specifics.

  

(Below is my understanding, written out here in order to help myself get it straight. Let me know if this is incorrect.)

--------------------------------------------------------------------------------------------------------------------------------------------------------

Objects in Python are similar to sprites in Alice, in that an object contains attributes and methods (both accessed with "dot" syntax). A "class" in Python is like a template that defines which attributes and methods are included in that class, and you use a "constructor" to create an object, that is, an "instance" of that class. So, if the "class" is "student," an object in the "student" class might be "bryan." Attributes included in that class might be student.age, student.email, student.major, and so on. Methods included in the class might be student.email() or student.enroll(), and so on. The object bryan would have attributes, eg., bryan.age = 51, or you could call bryan.email() to send an email to me with the "instance method" email().

  

The data types we have been working with are actually built-in classes. The module "datetime" will let you create objects of different classes: datetime.date, datetime.time, and (confusingly) datetime.datetime (which is module_datetime.class_datetime). Each of those types/classes has attributes and methods. The attributes of that class are accessed through parenthetical syntax:

datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

So, that would be _module_datetime.class_datetime(attributes)_.

  

Methods are just special kinds of attributes that let you do things with data stored in the object. Instance methods work with specific objects, and class methods work at the class level. datetime.today() is a method that creates an object containing the current datetime. You can include attributes in the parentheses when you call the class method to give the object you create those attributes, depending on how the class method is defined.

  

So, overall, an object oriented approach to programming is not that complicated. An object is little bundle of information and potential actions. Your program creates and works with these objects to do what you want. But object-oriented programming gets its full power from the idea of a "class," or a blueprint for creating objects. Instead of working with the built-in classes/data types, we can create our own classes that construct objects with just the collection of attributes and methods needed for our program. That lets you re-use the class over and over without duplicating code, and puts a custom set of capabilities right at your fingertips.

  

Helpful reads:

[https://www.learnpython.org/en/Classes_and_Objects](https://www.learnpython.org/en/Classes_and_Objects)

[https://pynative.com/python-classes-and-objects/](https://pynative.com/python-classes-and-objects/)

[https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

[https://docs.python.org/3/library/datetime.html#datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)

[https://realpython.com/instance-class-and-static-methods-demystified/](https://realpython.com/instance-class-and-static-methods-demystified/)