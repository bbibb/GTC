# Bryan Bibb, January 21, 2024, CPT187-W12
# Program:      Movie List (object-based version)
# Purpose:      Presents a list of movie titles and year to the user, with the
#               option to list movies, add a movie, and delete a movie from the list.
# Related       movies.py

# dataclass is a built-in class for storing data objects
from dataclasses import dataclass

# dataclass decorator turns this into a data object
@dataclass
# The Movie class has two attributes and one public method.
class Movie:
    name:str = ""
    year:int = 2000

    # getStr takes the two attributes and returns them in a formatted string
    def getStr(self):
        return f"{self.name} - {self.year}"
