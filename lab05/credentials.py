# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Jack Mullane
# Created: 2019-10-03


def names():
    print("\n")
    first = input("Enter your first name: ").lower()
    print("\n")
    last = input("Enter your last name: ").lower()
    print("\n")
    fullName = [first, last]
    return fullName


def maristUname(names):
    uName = str(names[0] + "." + names[1] + "1@marist.edu")
    return uName


def password():
    newPassword = input("Create a new password: ")
    print("\n")
    return passStrength(newPassword)


def passStrength(password):
    passFilter = password
    while len(passFilter) < 8:
        print("Fool of a Took! That password is feeble!\n")
        passFilter = input("Create a better password: ")
        print("\n")
    else:
        print("The force is strong in this one...")
        print("\n")
        return passFilter


def main():
    userName = maristUname(names())
    userPass = password()
    print(
        '''Congratulations, you have created a new Marist account!
        Your new email is:''', userName, "\n")
    print("Keep this password a secret: ", userPass, "\n")


main()
