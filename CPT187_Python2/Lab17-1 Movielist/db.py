#!/usr/bin/env/python3
# Bryan Bibb, Feb 5, 2024, CPT187-W12
# Program:  Movies List
# Purpose:  Maintains a list of movies with name, year, length in minutes, and category. The data
#           is saved in a SQLite database. Functionality includes user input for adding a new movie
#           viewing movies by category, year, and length, and deleting a movie.
# Related:  objects.py, ui.py

# import modules for sqlite operation
import sqlite3
from contextlib import closing

# import Category and Movie classes
from objects import Category
from objects import Movie

# initialize variable for data connection
conn = None

# connect to the sqlite database if not already connected
def connect():
    # global variable to reuse the connection in all functions
    global conn
    if not conn:
        DB_FILE = "movies.sqlite"
        conn = sqlite3.connect(DB_FILE)
        # refer to each column by name
        conn.row_factory = sqlite3.Row

# close the database connection to release resources
def close():
    if conn:
        conn.close()

# create a category object containing ID and name
def make_category(row):
    return Category(row["categoryID"], row["categoryName"])

# create a movie object with metadata
def make_movie(row):
    return Movie(row["movieID"], row["name"], row["year"], row["minutes"],
            make_category(row))

# retrieve data for categories with name and ID from the database
def get_categories():
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    # with statement closes after execution
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

# write those results to a categories list, with a category object appended one row at a time
    categories = []
    for row in results:
        categories.append(make_category(row))
    # this list
    return categories

# retrieve name for a specified category and call make_category to create an object for it
def get_category(category_id):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()
        if row:
            # category object is returned, or else None
            return make_category(row)
        else:
            return None

# search the database for a movie based on movieID input. This and the following get functions receive
# user input from functions in the ui layer.
def get_movie(movie_id):
    query = '''SELECT movieID, Movie.name, year, minutes, Movie.categoryID as categoryID, Category.name as categoryName
                FROM Movie JOIN Category ON Movie.categoryID = Category.categoryID 
                WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (movie_id,))
        # if a row is returned, make an object or else return None
        row = c.fetchone()
        if row:
            return make_movie(row)
        else:
            return None

# search the database for movies with a user-input categoryID. Query requires a JOIN because
# the category name is not in the movie table.
def get_movies_by_category(category_id):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()
    # make an object for each movie and append to the movies list
    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

# search database and return movies from a user-input year
def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

# make an object for each and append to the movies list
    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

# search database and return movies that are under a certain length in minutes
def get_movies_by_minutes(minutes):
    query = '''SELECT movieID, Movie.name, year, minutes, Movie.categoryID as categoryID, 
                    Category.name as categoryName
                FROM Movie JOIN Category 
                    ON Movie.categoryID = Category.categoryID
                WHERE minutes < ?
                ORDER BY minutes DESC'''
    with closing(conn.cursor()) as c:
        c.execute(query, (minutes,))
        results = c.fetchall()

# make an object for each and append to the movies list
    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

# add a movies to the database with an INSERT statement. User-input values come from ui.add_movie()
# this and the delete_movie() function actually change the database and so require a commit() method.
def add_movie(movie):
    sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                        movie.minutes))
        conn.commit()

# delete a movie from the database with a DELETE statement. The movie_id parameter comes from ui.delete_movie()
def delete_movie(movie_id):
        sql = '''DELETE FROM Movie WHERE movieID = ?'''
        with closing(conn.cursor()) as c:
            c.execute(sql, (movie_id,))
            conn.commit()