# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Jack Mullane
# Created: 2019-10-03

import re


def names():
    print("\n")
    first = input("Enter your first name: ").lower()
    print("\n")
    last = input("Enter your last name: ").lower()
    print("\n")
    fullName = [first, last]
    return fullName


def maristUname(names):
    uName = str(names[0] + "." + names[1] + "@marist.edu")
    return uName


def password():
    newPassword = input("Create a new password: ")
    print("\n")
    return passStrength(newPassword)


def passStrength(password):
    passFilter = password
    lenCheck = len(password) < 8
    numCheck = re.search("[0-9]", password) is None
    upCheck = re.search("[A-Z]", password) is None
    lowCheck = re.search("[a-z]", password) is None
    passCheck = not (lenCheck or numCheck or upCheck or lowCheck)
    if passCheck is False:
        print("Fool of a took! Your password is feeble!")
        print("\n")
        if lenCheck is True:
            passFilter = input("Your password needs at least 8 characters: ")
            print("\n")
        elif numCheck is True:
            passFilter = input("Your password needs numbers: ")
            print("\n")
        elif upCheck is True:
            passFilter = input("Your password needs uppercase characters: ")
            print("\n")
        elif lowCheck is True:
            passFilter = input("Your password needs lowercase characters: ")
            print("\n")
        return passStrength(passFilter)
    else:
        print("The force is strong in this one...")
        print("\n")
        return passFilter


def main():
    userList = []
    userNum = 0
    stop = ""
    while stop != "e":
        userName = maristUname(names())
        userList.append(userName)
        userCount = userList.count(userName)
        index = userName.find("@")
        userNum += 1
        countedName = userName[:index] + str(userCount) + userName[index:]
        userPass = password()
        print(
            '''Congratulations, you have created a new Marist account!\n
Your new email is:''', countedName, "\n")
        print("Keep this password a secret: ", userPass, "\n")
        stop = input(
            '''Type E to exit the user generator or press Enter to
proceed: ''').lower()
        print("\n")
    else:
        print("Congratulations! You generated", userNum, "email(s).", "\n")


main()
