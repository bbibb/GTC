#!/usr/bin/env python3
# Bryan Bibb, Nov 2, 2023, CPT168-434
# Program:  Word Counter
# Purpose:  Opens a file of the Gettysburg Address, and prints the total number
#           of words, the number of unique words, and the number of sentences.


# read the file into a list, split into sentences
def get_sentences_from_file(filename):
    with open(filename) as file:
        text = file.read()      # read string from file
    sentences = text.split(".") # save string to list by searching for . delimiter
    return sentences

# read the file into a list, split into individualy words
def get_words_from_file(filename):
    with open(filename) as file:
        text = file.read()    # read str from file

    # print(text), removing newline and punctuation characters
    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    
    words = text.split(" ")   # convert str to list
    words.sort()              # sort list in default string order
    # print(words)
    return words

# analyze the words list just created to get a list of unique items
def get_unique_words(words):
    unique_words = []
    unique_words.append(words[0])

    # process the list one at a time, adding words with only one occurence
    # to a new list of unique words
    for i in range(1, len(words)):
        if words[i] == words[i - 1]:    # test whether the word was just added
            continue
        else:
            unique_words.append(words[i]) # if not, add to the unique list
    return unique_words

def main():
    filename = "gettysburg_address.txt"
    print("The Word Counter program\n")  

    # get words, unique words, and sentences from the file
    words = get_words_from_file(filename) # get list of words
    unique_words = get_unique_words(words)
    sentences = get_sentences_from_file(filename)

    # display number of words, unique words, and sentences  
    print(f"Number of sentences = {len(sentences)}")
    print(f"Number of words = {len(words)}")
    print(f"Number of unique words = {len(unique_words)}")

    # display unique words and their word counts
    print("Unique word occurrences:")
    for word in unique_words:
        # print each word and the number of times it appears in the list
        print(f"    {word} = {words.count(word)}")  # count function
 
if __name__ == "__main__":
    main()
