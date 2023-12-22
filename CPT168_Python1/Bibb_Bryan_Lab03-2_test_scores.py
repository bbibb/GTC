#!/usr/bin/env python3
# Bryan Bibb, September 9, 2023, CPT168
# Program:      Test Scores
# Purpose:      Accepts user input for any number of test scores,
#               and then totals and averages them; Returns the
#               total and average test score to the user and gives
#               the option to repeat for another set.

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'end' to end input")
print("======================")

# initialize variables for the scores and the repeated loop
counter = 0
score_total = 0
test_score = 0
choice = 'y'

# the outside loop runs the first time and again if the user enters 'y'
while choice.lower() == 'y':

    # the inner loop runs as long as test scores are entered and breaks when
    # the user enters the string "end"
##    while True:
##        test_score = input("Enter test score: ")
##        if test_score.lower() == "end":
##            break
##        # this loop receives, validates, adds and averages user scores
##        else:                                   
##            test_score = int(test_score)        
##            if test_score >= 0 and test_score <= 100:
##                score_total += test_score
##                counter += 1
##            # an invalid score is not counted and the loop repeats
##            else:                               
##                print(f"Test score must be from 0 through 100. "
##                      f"Score discarded. Try again.")

    # the assignment expression replaces the while loop in the above section
    # if the user enters 'end' or 'END' the loop breaks, otherwise it runs

    while (test_score := input("Enter test score: ")).lower() != 'end':
        test_score = int(test_score)        
        # this loop receives, validates, adds and averages user scores
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        # an invalid score is not counted and the loop repeats
        else:                               
            print(f"Test score must be from 0 through 100. "
                      f"Score discarded. Try again.")
        
    # calculate average score
    average_score = round(score_total / counter)
                
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
    print()
    
    # ask if the user wants to repeat the program
    choice = input("Calculate another set of scores? (y/n)?: ")
    print()
    continue

# exit message    
print("Bye!")


