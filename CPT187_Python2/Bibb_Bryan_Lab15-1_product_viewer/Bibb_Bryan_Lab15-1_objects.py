# Bryan Bibb, CPT187-W12, 01/25/2024
# Program:  Product Viewer
# Purpose:  Program initializes a data set of objects based on the Product
#           superclass, with subclasses for Books, Movies, Albums, and Media.
#           Application prints each item, formatted, with appropriate data
#           for each subclass.
# Related:  product_viewer.py

# necessary for each of 5 dataclasses in module
from dataclasses import dataclass

# superclass Product has 3 attributes and 3 methods
@dataclass
class Product:
    # three attributes with data types, initialized empty
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    # method to calculate discount from two attributes
    # returns a number that is used by the next method
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    # calculation of price by subtracting prior returned value from price attribute
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    # Each subclass has a name, so this method applies to all.
    # no need to include name attribute in subclasses
    def getDescription(self):
        return self.name

# Media subclass adds format attribute and formatted description
# This attribute and method are inherited by Book, Movie, Album
@dataclass
class Media(Product):
    format:str = ""

    def getDescription(self):
        return f"{Product.getDescription(self)}"

# Book subclass adds author and format attributes and formatted description
@dataclass
class Book(Media):
    author:str = ""
#    format:str = ""    # format attribute provided by Media()
    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.author}"

# Movie subclass adds year and format attributes and formatted description
@dataclass        
class Movie(Media):
    year:int = 0
#    format:str = ""  # format attribute provided by Media()
    def getDescription(self):
        return f"{Product.getDescription(self)} ({self.year})"

# Media subclass adds artist and format attribute and formatted description
@dataclass
class Album(Media):
    artist:str = ""
#    format:str = ""   # format attribute provided by Media()

    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.artist}"

