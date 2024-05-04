size = int(input('Enter the length(size) you want : '))
symbol = input('Enter the symbol(character) : ')
def printD(size,char):
    for row in range(size):
        for col in range(size):
            if(col==0 or row==0 or row==size//2):
                print(char,end=' ')
            else:
                print(' ',end=' ')
        print('')
printD(size,symbol)