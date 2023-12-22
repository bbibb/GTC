#!/usr/bin/env python3
# Bryan Bibb, CPT168-434, Oct 5, 2023
# Program:      Trip Data
# Purpose:      Asks user input of data for multiple trips. After user enters
#               the length of a trip and how many gallons of gas were used,
#               program calculates the miles per gallon, returns it to the user
#               and saves trip data to the file "trips.bin." Data for multiple
#               trips are appended to the file.

# csv module is needed for file writing
import pickle

# receive user input, convert to float, and assign to miles_driven variable
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven

# receive user input, convert to float, and assign to gallons_used variable          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # initialize variables for aggregate trip data
    this_trip = []
    trip_data = []

    # for each trip desired by the user, solicit data input
    more = "y"

    # fill variables with user input and validation in functions
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # calculate and print mpg from variables returned by the functions                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        # record trip data in a list
        this_trip = [miles_driven, gallons_used, mpg]
        # append current trip data in a 2-dimensional list
        trip_data.append(this_trip)
        more = input("More entries? (y or n): ")
    
    # after user is finished with all trips, write data to a binary file 
    with open("trips.bin", "wb") as file:
        pickle.dump(trip_data, file)

    print("Bye! Your trip data has been saved to trips.bin.")

    # test code to make sure binary file is written correctly
##    with open("trips.bin", "rb") as file:
##        trip_list = pickle.load(file)
##        for trip in trip_list:
##            print(f"{trip[0]}\t\t {trip[1]}\t\t {trip[2]}")
 
if __name__ == "__main__":
    main()

