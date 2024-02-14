# Bryan Bibb, CPT187-W12, 01/25/2024
# Program:  Product Viewer
# Purpose:  Program initializes a data set of objects based on the Product
#           superclass, with subclasses for Books, Movies, Albums, and Media.
#           Application prints each item, formatted, with appropriate data
#           for each subclass.
# Related:  objects.py

# import superclass Product and subclasses
from objects import Product, Media, Book, Movie, Album

# function to show the contents of the products tuple
def show_products(products):
    print("PRODUCTS")
    # iterate through the tuple, print each line with enumeration
    for i, product in enumerate(products, start=1):
        # output formatted with getDescription() method
        print(f"{i}. {product.getDescription()}")
    print()

# function to show the contents of the product list, from user choice
def show_product(product):
    # variable to adjust spacing
    w=18
    print("PRODUCT DATA")
    # the product is evaluated for its datatype and approprate f-string passed to print()
    # all instances of Book, Movie, and Album also have a name attribute
    # from Product, and a format attibute from Media.
    print(f"{'Name:':{w}}{product.name}")
    # subclasses have unique data items to add to output
    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")
    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")
    if isinstance(product, Album):
        print(f"{'Artist:':{w}}{product.artist}")
    if isinstance(product, Media):
        print(f"{'Format: ':{w}}{product.format}")

    # all instances have price and discount data for calculating discount price
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()

# main function
def main():
    print("The Product Viewer program")
    print()
# data structure: instance of each class is added to a tuple 'products'
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book("The Big Short", 15.95, 34, "Hardback", "Michael Lewis"),
                Movie("The Holy Grail", 14.99, 68, "DVD", 19751),
                Album("Weathervanes", 12.99, 15, "Digital Download", "Jason Isbell and the 400 Unit"))
    # tuple passed to show function
    show_products(products)

    # loop to enable repeating of the program
    choice = "y"
    while choice.lower() == "y":
        # user input of number to view
        number = int(input("Enter product number: "))
        print()
        # the user's input is copied from tuple into new 'product' list
        product = products[number-1]
        # the new list is passed to the show function
        show_product(product)

        # option to repeat
        choice = input("View another product? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
