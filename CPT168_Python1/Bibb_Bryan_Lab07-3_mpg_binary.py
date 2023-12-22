#!/usr/bin/env python3
# Bryan Bibb, CPT168-434, Oct 6, 2023
# Program:      Trip Data
# Purpose:      Displays current data in trips.bin, and asks user input of data
#               for additional trips. After user enters the length of a trip and
#               how many gallons of gas were used, program calculates the miles
#               per gallon, returns it to the user and saves trip data to the file
#               "trips.bin." Data for multiple trips are appended to the file
#               and displayed.


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

# receive a 2-dimensional list from main() and write it as a bin file
def write_trips(trips):
    with open("trips.bin", "wb") as file:
        pickle.dump(trips, file)

# read the current state of the bin file and copy it into an updated list
# and return to main()
def read_trips():
    trips = []
    with open("trips.bin", "rb") as file:
        trip_list = pickle.load(file)
        # append one row at a time
        for trip in trip_list:
            trips.append(trip)
    return trips

# read the current state of the bin file and write it to the console with headers
def list_trips(trips):
    # suppress the header line if the bin file is initially empty
    if len(trips) > 0:
        trip_header = ["Miles Driven", "Gallons Used", "MPG"]
        print(f"{trip_header[0]}\t {trip_header[1]}\t {trip_header[2]}")
    # print each row  to the console    
    for trip in trips:
        print(f"{trip[0]}\t\t {trip[1]}\t\t {trip[2]}")
    print()

        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # initialize variable for initial data display and print initial contents
    # to console
    old_trips = read_trips()
    list_trips(old_trips)

    # for each trip desired by the user, solicit data input
    more = "y"
    new_trips = []
    
    while more.lower() == "y":
        # user input passed to data validating function
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # calculate and print mpg from variables returned by the functions                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # record current trip data in a list
        this_trip = [miles_driven, gallons_used, mpg]
        # append current trip data a list of trips entered in this session
        new_trips.append(this_trip)
        
        more = input("More entries? (y or n): ")

    # once user enters all trips this session, write them to the bin file
    total_trips = old_trips + new_trips
    write_trips(total_trips)

    # display total list with prior trips as well as new ones entered
    trips = read_trips()
    list_trips(trips)
    
    print("Bye! Your trip data has been saved to trips.bin.")

if __name__ == "__main__":
    main()


