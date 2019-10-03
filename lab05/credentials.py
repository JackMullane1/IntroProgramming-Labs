# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Jack Mullane
# Created: 2019-10-03


def main():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # generate a Marist-style password
    uname = str(first + "." + last + "1")

    # ask user to create a new password
    passwd = input("Create a new password: ")

    # ensure the password has at least 8 characters
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a better password: ")
    else:
        print("The force is strong in this one...")
        print(
            "Account configured. Your new email address is",
            uname + "@marist.edu")
        return True


main()
