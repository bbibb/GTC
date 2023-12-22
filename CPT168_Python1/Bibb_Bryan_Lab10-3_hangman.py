#!/usr/bin/env Python3
# Bryan Bibb, Nov 2, 2023, CPT168-434
# Program:      Hangman
# Purpose:      Selects a random word and allows user to guess the letters,
#               until either the word is spelled, or seven incorrect letters
#               have been entered, "hanging" the man.

# module containing a random list of words 
import wordlist


# draw the parts of the hangman as incorrect guesses are entered.
def draw_hangman(num_wrong):
    print("____")
    print("    |")
    if num_wrong == 0:      # no wrong guesses
        print()
    if num_wrong == 1:      # 1 wrong guess, head
        print("    O\n")
    elif num_wrong == 2:    # 2 wrong guesses, head and torso
        print("    O")
        print("    |\n")
    elif num_wrong == 3:    # 3 wrong guesses, add one arm
        print("    O")
        print("   \\|\n")
    elif num_wrong == 4:    # 4 wrong guesses, add second arm
        print("    O")
        print("   \\|/\n")
    elif num_wrong == 5:    # 5 wrong guesses, add more torso
        print("    O")
        print("   \\|/")    
        print("    |\n")      
    elif num_wrong == 6:    # 6 wrong guesses, add one leg
        print("    O")
        print("   \\|/")
        print("    |")      
        print("   /\n")
    elif num_wrong == 7:    # 7 wrong guesses, add second leg
        print("    O")
        print("   \\|/")
        print("    |")      
        print("   / \\\n")
        
# Get a random word from the word list
def get_word():
    word = wordlist.get_random_word()
    return word.upper()                 # convert words to uppercase

# Add spaces between letters, which will be used for screen display
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the display with current statistics related to guesses and letters
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79) # draw line across screen
    draw_hangman(num_wrong) # call draw function with the current wrong guess total
    # current stats
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))


# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper() # uppercase
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. ",
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()
    
    word_length = len(word)             # variable to track number of needed letters
    remaining_letters = word_length     # variable to track unguessed letters
    displayed_word = "_" * word_length  # underlines to show the letter positions

    # initialize variables
    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""

    # print current game status and stats
    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    # loop for receiving user input and recording letters already guessed
    while num_wrong < 7 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        # search loop to find the guessed letter in the word
        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char      
                    remaining_letters -= 1  # keep track of remaining letters
                else:
                    displayed_word += "_"   # display blank for unguessed positions           
        else:
            num_wrong += 1                  # if the letter is wrong, add to the number wrong

        num_guesses += 1                    # keep track of the number of guesses

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word) # update status

    # end game, based on whether word was spelled before 7 incorrect guesses
    print("-" * 79)
    if remaining_letters == 0:
        print(f"Congratulations! You got it in {num_guesses} guesses.")    
    else:    
        print("Sorry, you lost.")
        print(f"The word was: {word}")

def main():
    # start with game title and image of fully hanged man
    print("Play the H A N G M A N game")
    draw_hangman(7)

    # game play loop
    again = "y"
    while again.lower() == "y":
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ")

    print("Bye!")

if __name__ == "__main__":
    main()
