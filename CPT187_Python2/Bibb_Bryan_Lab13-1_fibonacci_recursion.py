#!/usr/bin/env python3
# Bryan Bibb, CPT187-W12, Jan 14, 2024
# Program:  Fibonacci Recursion
# Purpose:  Calculates and returns the fibonacci sequence
#           using a recursive algorithm.

# function definition

def fib(n):
    if n == 0:      # base case that does not require the recursive function
        return 0
    elif n == 1:    # second base case
        return 1
    # calculate the sequence with a recursive algorithm
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    # attribute sets how many levels of recursion, and digits returned
    for i in range(100):
        print(fib(i), end=", ")
    print("...")

if __name__ == "__main__":
    main()
