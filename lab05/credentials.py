# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Jack Mullane
# Created: 2019-10-03


def main():
    userN = maristUname(names())
    passW = password()
    print(
        '''Congratulations, you have created a new Marist account!
        Your new email is:''', userN, "\n")
    print("Keep this password a secret: ", passW, "\n")

def names():
    print("\n")
    first = input("Enter your first name: ")
    print("\n")
    last = input("Enter your last name: ")
    print("\n")
    fullName = [first, last]
    return fullName

def maristUname(fullName):
    uName = str(fullName[0] + "." + fullName[1] + "1@marist.edu")
    return uName

def password():
    passwd = input("Create a new password: ")
    print("\n") 
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!\n")
        passwd = input("Create a better password: ")
        print("\n")
    else:
        print("The force is strong in this one...")
        print("\n")
        return passwd


main()
