# CMPT 120 - Lab #6
# Jack Mullane
# 10-17-2019


def show_intro():
    print("\nWelcome to the Arithmetic Engine!\n")
    print("=================================\n")
    print("Valid commands are: 'add', 'sub', 'mult', 'div', and 'quit'.\n")


def show_outro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!\n")


def do_loop():
    supported = ["add", "sub", "mult", "div", "quit"]
    while True:
        cmd = str(input("What computation do you want to perform?: "))
        if cmd.lower() in supported:
            if cmd == "quit":
                break
            else:
                try:
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                except:
                    print("You have to enter a number!\n")
                    continue
                if cmd == "add":
                    result = num1 + num2
                elif cmd == "sub":
                    result = num1 - num2
                elif cmd == "mult":
                    result = num1 * num2
                elif cmd == "div":
                    result = num1 / num2
                print("\nThe result is:", result, "\n")
        else:
            print("That command is not supported.\n")


def main():
    show_intro()
    do_loop()
    show_outro()


main()
