# Bryan Bibb, CPT187-W12, Jan 24, 2024
# Program: Author's Tester
# Purpose: Provides a way to test the use of overriding system methods __str__ and __iter__
# Related: objects.py

# necessary for Book and Author dataclasses
from dataclasses import dataclass

# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    # creation of instance attribute, a list of authors
    def __init__(self):
        self.__list = []

    # method to add author parameter to the end of the list
    def add(self, author):
        self.__list.append(author)

    # @property decorator creates a property that is the length of the list
    @property
    def count(self):
        return len(self.__list)

    # override system __str__() method to print the list of authors
    def __str__(self):
        author_str = ""
        for author in self.__list:
            author_str += str(author) + ", "
        # this removes the final comma from the output
        author_str = author_str[:-2]
        # returned to callling function
        return author_str

    # generator function makes the object iterable
    def __iter__(self):
        # iterating through items in the object for return
        for author in self.__list:
            yield author

# Book class contains two attributes and one method
@dataclass
class Book:
    # title string and authors attribute of Authors type begin empty
    title:str = ""
    authors:Authors = None

    # override system __str__ method to return formatted title and author information
    def __str__(self):
        return f"{self.title} by {self.authors}"

# Author class contains two attriibutes and one method
@dataclass
# author name strings begin empty
class Author:
    firstName:str = ""
    lastName:str = ""

    # override system __str__ method to return formatted title and author information
    def __str__(self):
        return f"{self.firstName} {self.lastName}"


