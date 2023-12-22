#!/usr/bin/env python3
# Bryan Bibb, August 28, 2023, CPT168-434, Lab02-2
# Program:  Test Scores
# Purpose:  Ask for user input of three test scores, add them together,
#           and calculate the average score. Print each score plus the total
#           and average score to the console.

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# input scores from the user and tranform each string into an integer
total_score = 0       # initialize the variable for accumulating scores
score1 = int(input("Enter test score: ")) # ask for 3 user scores
score2 = int(input("Enter test score: ")) # int function transforms each 
score3 = int(input("Enter test score: ")) # into an integer

# add user scores together and save as total_score variable
total_score = score1 + score2 + score3

# calculate average score and round to the nearest whole number
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye!")


