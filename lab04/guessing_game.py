# A guessing game made with a loop and conditional statements.
def main():
    animal = "cat"
    guess = input("Try to guess what animal I'm thinking of: ").lower()
    correct = 0
    while correct < 1:
        if "q" == guess[:1]:
            return
        elif guess == animal:
            correct += 1
            answer = input(
                "You got it right! So do you like " + str(animal) +
                '''s? (Type y for yes, n for no): ''').lower()
            if answer == "y":
                print("That's great! So do I!")
            else:
                print("What did", animal + "s do to you huh?")
        else:
            guess = input("Try again (or type q to quit): ").lower()


main()
