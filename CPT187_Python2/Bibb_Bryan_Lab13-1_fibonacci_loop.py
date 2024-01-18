#!/usr/bin/env python3
# Bryan Bibb, CPT187-W12, Jan 14, 2024
# Program:  Fibonacci Loop
# Purpose:  Calculates and returns the fibonacci sequence
#           using a looping algorithm.

# function definition
def fib(n):
    if n == 0:      # base case that does not require the loop function
        return 0
    elif n == 1:    # a second base case
        return 1
    n1 = 0          # initialize 3 variables used for calculation
    n2 = 1
    fib = 0
    # calculate the sequence by adding each number to the total of the
    # prior calculation in the previous loop
    for i in range(2, n+1):
        fib = n1 + n2
        n1 = n2
        n2 = fib
    return fib

def main():
    # attribute sets how many times the loop will run, and digits returned
    for i in range(100):
        print(fib(i), end=", ")
    print("...")

if __name__ == "__main__":
    main()
