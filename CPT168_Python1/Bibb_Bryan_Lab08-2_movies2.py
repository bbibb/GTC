#!/usr/bin/env python3
# Bryan Bibb, October 18, 2023, CPT167-434
# Program:      Movie List
# Purpose:      Begins with a list of movies with years, and asks for user input
#               to list the movies, to add a new movie, or to delete a movie from the list.
#               Data is written to, and read from, a CSV file.


# import modules for CSV file operations, and Exception handling
import csv
import sys

# Global constant sets the name of the data file
FILENAME = "movies_test.csv"

# Exit the program with a final message
def exit_program():
    print("Terminating program.")
    # exit() is defined by the sys module
    sys.exit()

# Open the data file and read the current values into a list of movies
def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        # return the updated movie list as a list object
        return movies

    # Exception handling: if file not found, return the movies list to main()
    # which will enable it to be passsed to other functions as-is
    except FileNotFoundError as e:
        return movies
        # print(f"Could not find {FILENAME} file.")
        # exit_program()
    # Exception handling: with any other type of exception, print an error message and exit
    except Exception as e:
        print(type(e), e)
        exit_program()

# take the current movies list from other functions and write it to an updated csv file
def write_movies(movies):
    # attempt to open the existing csv file
    try:
        with open(FILENAME, "w", newline="") as file:
            #raise BlockingIOError("Error for testing")
            writer = csv.writer(file)
            writer.writerows(movies)
    # Exception handling: if the file is not found, print an error message and exit
    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    # Exception handling: if any other type of error, print an error message and exit
    except Exception as e:
        print(type(e), e)
        exit_program()

# list the movies as found in the current movies list 
def list_movies(movies):
    # include line numbers for each movie
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()

# receive the current list of movies and append a new movie to the list    
def add_movie(movies):
    # receive user input of the Name and Year of the movie
    name = input("Name: ")        
    while True:
        try:
            year = int(input("Year: "))
        # Exception handling: if the year is not a valid value, print message and restart
        except ValueError:
            print("Invalid numbers. Please enter positive integer.")
            continue
        # Data validation: if year is not a positive number, print message and restart
        if year <= 0:
            print("Sorry! Please enter a year greater than zero.")
            continue
        # if all entries are valid, exit loop
        else:
            break
    # append the new title to the movies list, and pass to write_movies() function
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

# delete a movie from the current movie list, and pass updated list to write_movies()
def delete_movie(movies):
    while True:
        # receive user input of the number for the movie to delete
        try:
            number = int(input("Number: "))
        # Exception handling: if the year is not a valid value, print message and restart
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        # Data validation: if year is not a positive number, print message and restart
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        # if all entries are valid, exit loop
        else:
            break
# delete the title from the movies list, and pass updated list to write_movies() function        
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

# display the opening menu
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

# main function to receive user input of menu selection, passed to appropriate function
def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        # if "exit," break out of the loop and proceed to closing message.
        elif command.lower() == "exit":
            break
        # If user input is not valid, restart loop
        else:
            print("Not a valid command. Please try again.\n")
        
    print("Bye!")

if __name__ == "__main__":
    main()
