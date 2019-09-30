# A guessing game made with a loop and conditional statements.
def main():
    animal = "cat"
    guess = input("Try to guess what animal I'm thinking of: ")
    while guess != animal:
        guess = input("Incorrect, guess again: ")
    else:
        print("Congrats! It was a(n)", animal + "!")

main()

