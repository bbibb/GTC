#!/usr/bin/env python3
# Bryan Bibb, Nov 2, 2023, CPT168-434
# Program:      Create Account
# Purpose:      Receives user input for Full Name, Email Address, and Phone Number, validates
#               data so that it conforms to correct format, and returns a message to the
#               user with their first name and phone number included.


# initialize variables and call functions
def main():
    full_name = get_full_name()
    password = get_password()
    email_address = get_email()
    phone_number = get_phone()
    print()

    # print success message to screen
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"We'll text your confirmation code to this number: {phone_number}")
    
# receive user input of full name    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip() # strip excess white space
        if " " in name:                                 # name must be at least two words
            return name
        else:
            print("You must enter your full name.")
    
# extract the first name from the full_name string variable    
def get_first_name(full_name):
    index1 = full_name.find(" ")                        # identify the space between names
    first_name = full_name[:index1]                     # save the first name to variable
    return first_name                                   # variable used by print function in main

    
# receive user input for password    
def get_password():
    while True:
        # initialize variables for testing user entry
        digit = False
        cap_letter = False
        # take user data
        password = input("Enter password:        ").strip() # strip excess white space
        for char in password:
            if char.isdigit():                              # make sure there is at least one digit
                digit = True
            elif char.isupper():                            # and one uppercase letter
                cap_letter = True                           # and the length 8 or more
        if digit == False or cap_letter == False or len(password) < 8:  # error if not, loop restarts
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password                                 # validated password returned

# get user input of email address        
def get_email():
    while True:
        # take user data
        email = input("Enter email address:   ").strip()    # strip excess white space
        at_divider = email.find("@")                        # make sure the format is correct:
        dot_divider = email.find(".com", at_divider)        # check for @ and .com
        if at_divider == -1 or dot_divider == -1:
            print("Incorrect format. Please enter a valid email address.")    # error message if not, loop restarts
        else:
            return email

# get user input of phone number
def get_phone():
    while True:
        # take user data
        phone_number = input("Enter phone number:    ").strip() # strip excess white space
        for char in " -().":                                    # find "-" character
            phone_number = phone_number.replace(char, "")       # remove "-" character in entry
        if len(phone_number) != 10 or phone_number.isdigit() == False: # make sure number is correct
            print("Please enter a 10 digit phone number.")             # length and format
        else:
            # format phone number with periods between the three parts
            phone_number = phone_number[0:3] + "." + phone_number[3:6] + "." + phone_number[6:]
            return phone_number

        
if __name__ == "__main__":
    main()
