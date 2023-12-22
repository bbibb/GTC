#!/usr/bin/env python3
# Bryan Bibb, Nov 11, 2023, CPT168-434
# Program:      Timer
# Purpose:      When the user presses Enter/return, the program records the time
#               of the button press and waits for a second press. When the user
#               presses Enter/return a second time, the current time is compared
#               with the recorded start time, and the elapsed time in hours, minues
#               and seconds is returned.

# import datetime functions
from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer and record the current time in a datetime object
    input("Press Enter to start...")
    start_time = datetime.now()
    print(f"Start time: {start_time:%X.%f}")
    print()
    
    # stop timer record the current time in a datetime object
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print(f"Stop time: {stop_time:%X.%f}")
    print()

    # calculate elapsed time by subtracting start time from stop time
    elapsed_time = stop_time - start_time

    # create objects with resulting time increments 
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes in whole numbers 
    hours = minutes // 60   # whole number represents number of minutes
    minutes = minutes % 60  # remainder represents the number of additional seconds

    # create time object with time increments
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    # if over one hour or one minute, print value for hours or minutes
    if hours > 0 or minutes > 0:
        print(f"Hours/minutes: {time_object:%H:%M}")
    # always print the number of seconds
    print(f"Seconds: {time_object:%S.%f}")

if __name__ == "__main__":
    main()
