#!/usr/bin/env/python3
# Bryan Bibb, Feb 5, 2024, CPT187-W12
# Program:  Movies List
# Purpose:  Maintains a list of movies with name, year, length in minutes, and category. The data
#           is saved in a SQLite database. Functionality includes user input for adding a new movie
#           viewing movies by category, year, and length, and deleting a movie.
# Related:  objects.py, db.py

# db module allows database connection; Movie class from objects file
import db
from objects import Movie

# display the title and menu
def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("1.  - View movies by category")
    print("2.  - View movies by year")
    print("3.  - View movies by max length")
    print("4.  - Add a movie")
    print("5.  - Delete a movie")
    print("6.  - Exit program")
    print()    

# call a list of categories from the database
def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    # print each row from the results list
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()

# call a list of movies, called by "display" functions to format the output
def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        # list is displayed with int datatypes changed to str()
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

# get a list of movies by specified user-input category
def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    # error if category does not exist
    if category == None:
        print("There is no category with that ID.\n")
    else:
        # get a list of movies based on categoryID and send to display_movies
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())

# get a list of movies by specified user-input year
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    # get a list of movies based on year and send to display_movies
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

# get a list of movies by max length
def display_movies_by_minutes():
    minutes = int(input("Max minutes: "))
    print()
    # get a list of movies based on max minutes and send to display_movies
    movies = db.get_movies_by_minutes(minutes)
    display_movies(movies, str(minutes))

# add a movie based on user-input data for name, year, length, and category
def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    # error message if categoryID is invalid
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    # create Movie object with attributes and add to database with db.add_movie
    else:
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(name + " was added to database.\n")

# delete movie from the database, based on input movieID
def delete_movie():
    movie_id = int(input("Movie ID: "))
    # get the details from the database with query of movieID
    movie = db.get_movie(movie_id)

    # error if not found
    if movie == None:
        print("Movie not found.\n")
    else:
        # confirmation dialogue
        confirm = input(f"Do you want to delete\" {movie.name}\"? Enter 'y' or 'n'. ")
        if confirm.lower() == 'y':
            # delete the movie from the database and report success.
            db.delete_movie(movie_id)
            print(f"\n\"{movie.name}\" was deleted from database.\n")
        else:
            print(f"\n\"{movie.name}\" was not deleted from database.\n")

# main function initializes the databse connection, shows the menu and category list
def main():
    db.connect()
    display_title()
    display_categories()
    # user command selection
    try:
        while True:
            command = int(input("Please enter a number: "))
            if command == 1:
                display_movies_by_category()
                display_menu()
                display_categories()
            elif command == 2:
                display_movies_by_year()
                display_menu()
                display_categories()
            elif command == 3:
                display_movies_by_minutes()
                display_menu()
                display_categories()
            elif command == 4:
                add_movie()
            elif command == 5:
                delete_movie()
            elif command == 6:
                break
            else:
                print("Not a valid command. Please try again.\n")
                display_menu()
    except:
        print("Invalid command. Please try again.\n")
        main()
    # close the database on exit
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
