#!/usr/bin/env python3
# Bryan Bibb, September 23, 2023, CPT168-434, Lab-5-1
# Program:          Test Scores
# Purpose:          Asks for input of test scores, and averages them together. Returns both
#                   the total of the entered scores as well as the numeric average rounded
#                   to one digit.

# display a welcome message and directs users to enter values as integers, since there
# is no data type validation in the program
print("The Test Scores application")
print()
print("Enter test scores as whole numbers between 0 and 100")
print("Enter 'x' to end input")
print("======================")

# initialize variables for the number of scores, test score values, and the running total.
counter = 0
score_total = 0
test_score = 0

# iterate through test scores as they are entered
while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    # convert entered test score to an integer; if 'x' is entered, break the loop
    if test_score != "x":
        test_score = int(test_score)
        # counter += 1 This line was the bug as it counted incorrect entries for the avg
    else:
        break
    # test whether the integer is a positive score between 0 and 100,
    # and add to the running total, or print an error message and restart loop
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# calculate average score
average_score = round(score_total / counter, 1)
                
# format and display the result
print("======================")
print(f"Total Score: {score_total}"
      f"\nAverage Score: {average_score}")
print()
print("Bye")


