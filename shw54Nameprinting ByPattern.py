rows = int(input('Enter the value of rows: '))  # 3,5   4,7   5,9  6,11   7,13  8,15
column = (rows * 2) - 1
size = rows
char = input('Enter the symbol(character) : ')
columnk = rows
rowsk = (columnk * 2) - 3


def printA(rows, column, char):
    c = (column + 1) // 2
    r = rows // 2
    for row in range(rows + 1):
        for col in range(1, column + 1):
            if ((row == row and (col == c - row or col == c + row)) or row == r and (col > c - row and col < c + row)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')


def printB(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or ((row == 0 or row == size - 1 or row == size // 2) and col != size - 1) or (
                    col == size - 1 and row != 0 and row != size - 1 and row != size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printC(size, char):
    for row in range(size):
        for col in range(size):
            if ((col == 0 and row != 0 and row != size - 1) or (row == 0 and col != 0) or (
                    row == size - 1 and col != 0)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printD(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or ((row == 0 or row == size - 1) and col != size - 1) or (
                    col == size - 1 and (row != 0 and row != size - 1))):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printE(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or row == 0 or row == size - 1 or row == size // 2):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printF(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or row == 0 or row == size // 2):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printG(size, char):
    for row in range(size):
        for col in range(size):
            if ((col == 0 and row != 0 and row != size - 1) or (row == 0 and col != 0) or (
                    row == size - 1 and col != 0 and col != size - 1) or (
                    col == size - 1 and row >= size // 2 and row != size - 1) or (
                    row == size // 2 and col >= size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printH(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or col == size - 1 or row == size // 2):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printI(size, char):
    for row in range(size):
        for col in range(size):
            if (col == size // 2 or row == 0 or row == size - 1):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printJ(size, char):
    for row in range(size):
        for col in range(size):
            if ((col == size // 2 and row != size - 1) or row == 0 or (row == size - 1 and col < size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printK(rowsk, columnk, char):
    for row in range(rowsk):
        for col in range(columnk):
            if (col == 0 or col == columnk - row - 1 or col == row - columnk + 3):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printL(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or row == size - 1):
                print("*", end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printM(rows, column, char):
    for row in range(rows):
        for col in range(column):
            if (col == 0 or col == column - 1 or col == row or col == column - row - 1):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printN(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or col == row or col == size - 1):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printO(size, char):
    for row in range(size):
        for col in range(size):
            if (((row == 0 or row == size - 1) and (col != size - 1 and col != 0)) or (
                    (col == size - 1 or col == 0) and (row != 0 and row != size - 1))):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printP(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or ((row == 0 or row == size // 2) and col != size - 1) or (
                    col == size - 1 and row != 0 and row < size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printQ(size, char):
    for row in range(size):
        for col in range(size):
            if (((row == 0 or row == size - 1) and (col != size - 1 and col != 0)) or (
                    (col == size - 1 or col == 0) and (row != 0 and row != size - 1)) or (
                    row == size - 2 and col == size - 2) or (row == size - 1 and col == size - 1)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printR(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or ((row == 0 or row == size // 2) and col != size - 1) or (
                    col == size - 1 and row != 0 and row < size // 2) or (col == row and col > size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printS(size, char):
    for row in range(size):
        for col in range(size):
            if ((col == 0 and row < size // 2) or row == 0 or row == size - 1 or row == size // 2 or (
                    col == size - 1 and row > size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printT(size, char):
    for row in range(size):
        for col in range(size):
            if (col == size // 2 or row == 0):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printU(size, char):
    for row in range(size):
        for col in range(size):
            if ((row == size - 1 and (col != size - 1 and col != 0)) or (
                    (col == size - 1 or col == 0) and row != size - 1)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printV(rows, column, char):
    for row in range(rows):
        for col in range(column):
            if (col == row or col == column - row - 1):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printW(rows, column, char):
    for row in range(rows):
        for col in range(column):
            if (col == 0 or col == column - 1 or col == column // 2 - row or col == column // 2 + row):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printX(size, char):
    for row in range(size):
        for col in range(size):
            if (col == row or col == size - 1 - row):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printY(size, char):
    for row in range(size):
        for col in range(size):
            if (((col == row or col == size - 1 - row) and row < size // 2) or (col == size // 2 and row >= size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


def printZ(size, char):
    for row in range(size):
        for col in range(size):
            if (row == 0 or row == size - 1 or col == size - 1 - row):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')

name=input('Enter your name : ')
for i in name:
    match i:
        case 'A':
            printA(rows,column,char)

        case 'B':
            printB(size,char)

        case 'C':
            printC(size,char)

        case 'D':
            printD(size, char)

        case 'E':
            printE(size, char)

        case 'F':
            printF(size, char)

        case 'G':
            printG(size, char)

        case 'H':
            printH(size, char)

        case 'I':
            printI(size, char)

        case 'J':
            printJ(size, char)

        case 'K':
            printK(rowsk,columnk,char)

        case 'L':
            printL(size, char)

        case 'M':
            printM(rows,column, char)

        case 'N':
            printN(size, char)

        case 'O':
            printO(size, char)

        case 'P':
            printP(size, char)

        case 'Q':
            printQ(size, char)

        case 'R':
            printR(size, char)

        case 'S':
            printS(size, char)

        case 'T':
            printT(size, char)

        case 'U':
            printU(size, char)

        case 'V':
            printV(rows,column,char)

        case 'W':
            printW(rows,column,char)

        case 'x':
            printX(size, char)

        case 'y':
            printY(size, char)

        case 'Z':
            printZ(size, char)
