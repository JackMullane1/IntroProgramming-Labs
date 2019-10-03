# A program to compute pi based on a math sequence, takes user's input.
import math


def main():
    num = int(input("Enter the nth term of the pi sequence: "))
    result = (pi(num))
    print("Sum: ", result)
    print("Accuracy: ", (math.pi - result))


def pi(num):
    if num <= 0:
        print("The number has to be positive")
    elif num % 2 == 0:
        num *= 2
    else:
        num *= 2
        num -= 1
    add = 0
    for i in range(1, num, 4):
        now = (4/i)
        add += now
        after = (4/(i+2))
        add -= after
    return add


main()
