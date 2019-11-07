# CMPT 120 - Intro to Programming
# Lab 6 - Lists, Functions, and Error Handling.
# Author: Jack Mullane
# Created: 10-24-2019


def printRow(row):
    output = "|"
    for square in row:
        if square == 0:
            output += ("   |")
        elif square == 1:
            output += (" x |")
        elif square == 2:
            output += (" o |")
    print(output)    
    pass


def printBoard(board):
    print("+-----------+")
    for row in board:
        printRow(row)
        print("+-----------+")
    pass


def markBoard(board, row, col, player):    
        if board[row][col] == 0:
            board[row][col] = player
        else:
            print("\nThat square is already marked!")
        pass


def getPlayerMove():  
    while True:
        try:
            row = int(input("\nInput the row number for your mark (1-3): "))
            if row < 1 or row > 3:
                print("\nThe value has to be between 1 and 3.")
                continue
        except ValueError:
            print("\nPlease input a number.")
            continue
        try:
            col = int(input("\nInput the column number (1-3): "))
            if col < 1 or col > 3:
                print("\nThe value has to be between 1 and 3.")
                continue
            break
        except ValueError:
            print("\nPlease input a number.")
            continue
    row -= 1
    col -= 1
    return (row, col)


def winRow(board):
    pass


def winCol(board):
    pass


def winDiag(board):
    pass


def hasBlanks(board):
    flag = False
    for row in board:
        for square in row:
            if square != 0:
                continue
            else:
                flag = True
    return flag


def main():
    board = ([0, 0, 0],
             [0, 0, 0],
             [0, 0, 0])
    player = 1
    while hasBlanks(board):
        printBoard(board)   
        row, col = getPlayerMove()
        markBoard(board, row, col, player)
        player = player % 2 + 1


main()
