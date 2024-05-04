size = int(input('Enter the value of size : '))
symbol = input('Enter the symbol(character) : ')
def printN(size,symbol):
    for row in range(size):
        for col in range(size):
            if(col==0 or col==row or col==size-1):
                print(symbol,end=' ')
            else:
                print(' ',end=' ')
        print('')
printN(size,symbol)