#!/usr/bin/env python3
# Bryan Bibb, CPT187-W12, Jan 14, 2024
# Program:      Towers of Hanoi
# Purpose:      Given a number of discs, calculates the steps needed to solve
#               the Tower of Hanoi puzzle, moving all disks from one post to
#               another without placing a larger disk on top of a smaller one.

# move_disk function with attributes for the number of disks, plus the 3 posts
def move_disk(n, src, dest, temp):
    print("     move_disk(n={:d}, src={:s}, dest={:s}, temp={:s})" .format(n, src, temp, dest))
    if n == 0:  # base case with zero disks to move
        return
    else:
        # moves disks by rotating the src, temp, and dest posts
        move_disk(n-1, src, temp, dest)
        print("Move disk", n, "from", src, "to", dest)
        move_disk(n-1, temp, dest, src)
        
def main():
    # welcome message and user input for number of disks
    print("**** TOWERS OF HANOI ****")
    print()
    num_disks = int(input("Enter number of disks: "))
    print()

    # function called with names for the three attributes    
    move_disk(num_disks, "A", "C", "B")

    print()
    print("All disks have been moved.")

if __name__ == "__main__":
    main()
