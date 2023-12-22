#!/usr/bin/env python3
# Bryan Bibb, Nov 17, 2023, CPT168-434
# Program:      Movie List
# Purpose       Begins with a list of movies with year, and asks
#               for user input to list the movies, to add a new movie,
#               or to delete a movie from the list.  

# list the rows currently in the movie_list
def list(movie_list):
    # if the list is empty, return error message
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    # iterate through list and display each row with enumeration
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie['name']} ({movie['year']})")
        print()

# append new movie to movie_list based on user input of name and year
def add(movie_list):
    name = input("Name: ")
    # Exception handling to prevent crash if a non-integer is entered for the year
    try:
        year = int(input("Year: "))
        movie = {"name": name, "year": year}
        movie_list.append(movie)
        print(f"{movie['name']} was added.\n")  
    # Error message if year is invalid
    except ValueError:
        print("Please enter a valid numeric year.")
    
# delete a movie from the list based on user choice
def delete(movie_list):
    # Exception handling to prevent crash if choice is not an integer
    try:
        # return error messager if choice is outside list length
        number = int(input("Number: "))
        if number < 1 or number > len(movie_list):
            print("Invalid movie number.\n")
        # remove the chosen movie from the list with pop function
        else:
            movie = movie_list.pop(number-1)
            print(f"{movie['name']} was deleted.\n")
    # Error message if menu selection is invalid data type
    except ValueError:
            print("Invalid decimal number. Please try again.")

# initial display to inform user of the function choices      
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    # intitalize movie_list variable with default values
    movie_list = [{"name": "Monty Python and the Holy Grail", "year": 1975},
                  {"name": "On the Waterfront", "year": 1954},
                  {"name": "Cat on a Hot Tin Roof", "year": 1958}]

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
