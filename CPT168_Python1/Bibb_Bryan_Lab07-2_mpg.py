#!/usr/bin/env python3
# Bryan Bibb, CPT168-434, Oct 6, 2023
# Program:      Trip Data
# Purpose:      Displays current data in trips.csv, and asks user input of data
#               for additional trips. After user enters the length of a trip and
#               how many gallons of gas were used, program calculates the miles
#               per gallon, returns it to the user and saves trip data to the file
#               "trips.csv." Data for multiple trips are appended to the file
#               and displayed.


# csv module is needed for file writing
import csv

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

# receive a 2-dimensional list from main() and write it as a csv file
def write_trips(trips):
    with open("trips.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

# read the current state of the csv file and copy it into an updated list,
# return to main()
def read_trips():
    trips = []
    with open("trips.csv", newline="") as file:
        reader = csv.reader(file)
        # append one row at a time
        for row in reader:
            trips.append(row)
    return trips

# read the current state of the csv file and write it to the console with headers
def list_trips(trips):
    # suppress the header line if the CSV file is initially empty
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

    # initialize variable for initial data display and print initial csv
    # contents to console
    trips = read_trips()
    list_trips(trips)

    # for each trip desired by the user, solicit data input
    more = "y"

    # initialize variable used to collect trips in this run of the program
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
        # append current trip data to the list of trips entered in this session
        new_trips.append(this_trip)
        
        more = input("More entries? (y or n): ")

    # once user enters all trips this session, write them to the csv file
    write_trips(new_trips)

    # display total list with prior trips as well as new ones entered
    trips = read_trips()
    list_trips(trips)
    
    print("Bye! Your trip data has been saved to trips.csv.")

if __name__ == "__main__":
    main()


