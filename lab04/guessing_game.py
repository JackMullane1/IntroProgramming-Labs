# A guessing game made with a loop and conditional statements.
def main():
    animal = "cat"
    guess = input("Try to guess what animal I'm thinking of: ").lower()
    correct = 0
    while correct < 1:
        if guess == animal:
            correct += 1
            print("Congrats! It was a(n)", animal + "!")
        elif guess == "quit":
            return
        else:
            guess = input("Try again (or type quit to quit): ").lower()


main()
