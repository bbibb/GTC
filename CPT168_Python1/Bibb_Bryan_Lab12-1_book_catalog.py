#!/usr/bin/env python3
# Bryan Bibb, Nov 17, 2023, CPT168-434
# Program:          Book Catalog
# Purpose:          Presents a list of menu options through which the user can
#                   list book information as well as add, edit, and delete books
#                   within the data structure.


# function to list all books
def list_book(book_catalog):
    # list the fields in each dictionary entry one by one
    for book in book_catalog:
        print()
        print(f"Title:       {book}")
        print(f"Author:      {book_catalog[book]['author']}")
        print(f"Pub year:    {book_catalog[book]['pubyear']}")

def show_book(book_catalog):
    title = input("Title: ")
    # search for the user's title in the book catalog dictionary
    if title in book_catalog:
        book = book_catalog[title]
        # return the title along with the other two fields
        print(f"Title:    {title}")
        print(f"Author:   {book['author']}")
        print(f"Pub year: {book['pubyear']}")
    else:
        # error if not found
        print(f"Sorry, {title} doesn't exist in the catalog.")

def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    # check if user wants to add or edit a current entry
    if mode == "add" and title in book_catalog:
        print(f"{title} already exists in the catalog.")
        # if search finds the title already, give option to edit
        response = input ("Would you like to edit it? (y/n): ").lower()
        # if yes, proceed to data entry
        if(response != "y"):
            return
    # if title not found, and user chooses, give option to add
    elif mode == "edit" and title not in book_catalog:
        print(f"{title} doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        # if yes, proceed to data entry
        if (response != "y"):
            return

    # Data entry: get remaining book data and create a dictionary for the data
    author = input("Author name: ")
    pubyear = input("Publication year: ")
    book = {title: {"author": author, "pubyear": pubyear}}

    # Add the book data to the catalog using the update operator
    book_catalog |= book

def delete_book(book_catalog):
    title = input("Title: ")
    # if title is found, remove entry from the dictionary
    if title in book_catalog:
        del book_catalog[title]
        print(f"{title} removed from catalog.")
    else:
        # error message if not found
        print(f"{title} doesn't exist in the catalog.")

# initial menu
def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("list - List all books") 
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")

def main():
    # initial menu
    display_menu()
    # initialize dictionary with starting book data
    # each dictionary etnry contains Title and an embedded dictionary object
    book_catalog = {
        "Moby Dick": 
            {"author" : "Herman Melville",
             "pubyear" : "1851"},
        "The Hobbit":
            {"author" : "J. R. R. Tolkien", 
             "pubyear" : "1937"},
        "Slaughterhouse Five":
            {"author" : "Kurt Vonnegut",
             "pubyear" : "1969"}
        }
    while True:
        # loop to enable user command selection
        print()
        command = input("Command: ").lower()
        if command == "list":
            list_book(book_catalog)
        elif command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
