# A program used to compute a user given number for the term in the fobonnaci
# sequence.
def main():
    num = int(input("Enter a number for the fibonnaci sequence: "))
    result = fibonacci(num)
    print(result)


def fibonacci(num):
    if num < 0:
        return
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


main()
