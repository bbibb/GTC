#!/usr/bin/env python3
# Bryan Bibb, January 21, 2024, CPT187-W12
# Purpose:      Presents a list of movie titles and year to the user, with the
#               option to list movies, add a movie, and delete a movie from the list.
# Related:      objects.py

# import Movie class
from objects import Movie

# list the rows currently in the movie_list
def list(movie_list):
    # if the list is empty, return error message
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    # iterate through list and display each row with enumeration
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie.getStr()}")
        print()

# append new movie to movie_list based on user input of name and year
def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = Movie(name, year)
    movie_list.append(movie)
    # the object is 'movie', and the name and year are attributes
    print(f"{movie.name} was added to the list.\n")

# delete a movie from the list based on user choice
def delete(movie_list):
    # Exception handling to prevent crash if choice is not an integer
    try:
        number = int(input("Number: "))
        if number < 1 or number > len(movie_list):
            print("Invalid movie number.\n")
    #  remove the chosen movie from the list with pop function
        else:
            movie = movie_list.pop(number-1)
            print(f"{movie.name} was deleted from the list.\n")
    # triggered if the entry is not a valid integer
    except ValueError:
        print("Please enter a valid integer.")
        print()
        main()

# initial display to inform user of the function choices
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

# intitalize movie_list variable with default values
def main():
    movie_list = [Movie("Monty Python and the Holy Grail", 1975),
                  Movie("On the Waterfront", 1954),
                  Movie("Cat on a Hot Tin Roof", 1958)]

    display_menu()
# present options to the user and follow input to correct function
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    print("Bye!")

if __name__ == "__main__":
    main()
