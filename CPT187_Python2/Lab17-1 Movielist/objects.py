#!/usr/bin/env/python3
# Bryan Bibb, Feb 5, 2024, CPT187-W12
# Program:  Movies List
# Purpose:  Maintains a list of movies with name, year, length in minutes, and category. The data
#           is saved in a SQLite database. Functionality includes user input for adding a new movie
#           viewing movies by category, year, and length, and deleting a movie.
# Related:  ui.py, db.py

# Class to create an object for each movie with attributes for metadata.
# Includes Category objects and default values for each field.
class Movie:
    def __init__(self, id=0, name=None, year=0, minutes=0, category=None):
        self.id = id
        self.name = name
        self.year = year
        self.minutes = minutes
        self.category = category

# Class to create an object for each category with two fields: ID and name.
# Default values, 0 for ID and None for name.
class Category:
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name

