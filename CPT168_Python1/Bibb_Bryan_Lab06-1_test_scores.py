#!/usr/bin/env python3
# Bryan Bibb, September 29, 2023, CPT268-434
# Program:      Test Scores
# Purpose:      Asks the user for test scores, performs calculations on entered
#               values, and returns the number of scores, the average of scores
#               enteres, and the low, high, and median scores in the list.

# print the name of of the program and give instructions for how to exit the program
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

# receive the user input of test scores and add each to a 'scores' list
def get_scores():
    # loop receives test scores until user enters 'x'
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            # scores list retured to main()
            return  scores
        # if score is valid, add to the 'scores' list
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
        # if score is invalid, print error message and restart loop
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

# process score_list to calculate arithmetic values
def process_scores(score_list):
    # initialize variables used for calculation
    total_score = 0
    score_number = len(score_list)
    # iterate through the list to create a sum total
    for n in score_list:
        total_score += n
    # calculation based on the total score, number of scores, and list of values
    average_score = round((total_score / score_number), 2)
    low_score = min(score_list)
    high_score = max(score_list)
    # sort the list so that the median can be calculated accurately
    # median score is found by indexing the middle value in the list
    score_list_sorted = sorted(score_list)
    median_index = len(score_list) // 2
    # if there is an odd number of scores, median is the middle value
    if len(score_list) % 2 == 1:
        median_score = score_list_sorted[median_index]
    # if there is an even number of scores, median is the average of the middle two values
    else:
        median_score = (score_list_sorted[median_index]
                        + score_list_sorted[median_index - 1]) / 2
                
    # format and display the results
    print()
    print("Score total:       ", total_score)
    print("Number of Scores:  ", score_number)
    print("Average Score:     ", average_score)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median_score)

# main function to call the relevant functions in order
def main():
    display_welcome()
    # create a variable from the list returned by get_scores()
    score_list = get_scores()
    # pass that variable to process_scores()
    process_scores(score_list)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


