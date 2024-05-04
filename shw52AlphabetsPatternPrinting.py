rows = int(input('Enter the value of rows: '))  # 3,5   4,7   5,9  6,11   7,13  8,15
column = (rows * 2) - 1
size = rows
symbol = input('Enter the symbol(character) : ')
columnk = rows
rowsk = (columnk * 2) - 3


def printA(rows, column, symbol):
    c = (column + 1) // 2
    r = rows // 2
    for row in range(rows + 1):
        for col in range(1, column + 1):
            if ((row == row and (col == c - row or col == c + row)) or row == r and (col > c - row and col < c + row)):
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print('')


printA(rows, column, symbol)


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


printB(size, symbol)


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


printC(size, symbol)


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


printD(size, symbol)


def printE(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or row == 0 or row == size - 1 or row == size // 2):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printE(size, symbol)


def printF(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or row == 0 or row == size // 2):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printF(size, symbol)


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


printG(size, symbol)


def printH(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or col == size - 1 or row == size // 2):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printH(size, symbol)


def printI(size, char):
    for row in range(size):
        for col in range(size):
            if (col == size // 2 or row == 0 or row == size - 1):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printI(size, symbol)


def printJ(size, char):
    for row in range(size):
        for col in range(size):
            if ((col == size // 2 and row != size - 1) or row == 0 or (row == size - 1 and col < size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printJ(size, symbol)


def printK(rowsk, columnk, char):
    for row in range(rowsk):
        for col in range(columnk):
            if (col == 0 or col == columnk - row - 1 or col == row - columnk + 3):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printK(rowsk, columnk, symbol)


def printL(size, char):
    for row in range(size):
        for col in range(size):
            if (col == 0 or row == size - 1):
                print("*", end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printL(size, symbol)


def printM(rows, column, char):
    for row in range(rows):
        for col in range(column):
            if (col == 0 or col == column - 1 or col == row or col == column - row - 1):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printM(rows, column, symbol)


def printN(size, symbol):
    for row in range(size):
        for col in range(size):
            if (col == 0 or col == row or col == size - 1):
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printN(size, symbol)


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


printO(size, symbol)


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


printP(size, symbol)


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


printQ(size, symbol)


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


printR(size, symbol)


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


printS(size, symbol)


def printT(size, char):
    for row in range(size):
        for col in range(size):
            if (col == size // 2 or row == 0):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printT(size, symbol)


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


printU(size, symbol)


def printV(rows, column, char):
    for row in range(rows):
        for col in range(column):
            if (col == row or col == column - row - 1):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printV(rows, column, symbol)


def printW(rows, column, char):
    for row in range(rows):
        for col in range(column):
            if (col == 0 or col == column - 1 or col == column // 2 - row or col == column // 2 + row):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printW(rows, column, symbol)


def printX(size, char):
    for row in range(size):
        for col in range(size):
            if (col == row or col == size - 1 - row):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printX(size, symbol)


def printY(size, char):
    for row in range(size):
        for col in range(size):
            if (((col == row or col == size - 1 - row) and row < size // 2) or (col == size // 2 and row >= size // 2)):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printY(size, symbol)


def printZ(size, char):
    for row in range(size):
        for col in range(size):
            if (row == 0 or row == size - 1 or col == size - 1 - row):
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('')


printZ(size, symbol)



