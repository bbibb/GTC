# Bryan Bibb, CPT187-W12, Jan 24, 2024
# Program: Author's Tester
# Purpose: Provides a way to test the use of overriding system methods __str__ and __iter__
# Related: objects.py

# import classes from the objects module
from objects import Book, Author, Authors

# main function to initialize, format, and print the test author data
def main():
    print("The Authors Tester program")
    print()

    author1 = Author("Mark", "Twain")
    author2 = Author("Charles", "Warner")
    # authors list created by Authors() constructor
    authors = Authors()
    # author1, author2 variables added to authors list
    authors.add(author1)
    authors.add(author2)
    # book object created by Book constructor with title and data from authors list
    book = Book("The Gilded Age", authors)


    print("BOOK DATA - SINGLE LINE")
    # display data from the book object
    print(book)
    print()

    # display data from the book object in parts: title then authors
    print("BOOK DATA - MUTLIPLE LINES")
    print("Title:   ", book.title)
    if authors.count < 2:
        print("Author: ", book.authors)
    else:
        print("Authors: ", book.authors)
    print()

    # display the authors, printed one per line via redefined __str__() method
    print("AUTHORS")
    for author in authors:
        print(author)

if __name__ == "__main__":
    main()
