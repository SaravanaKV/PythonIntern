size = int(input('Enter the length(size) you want : '))
symbol = input('Enter the symbol(character) : ')
def printD(size,char):
    for row in range(size):
        for col in range(size):
            if(((row==0 or row==size-1) and (col!=size-1 and col!=0)) or ((col==size-1 or col==0)and(row!=0 and row!=size-1))):
                print(char,end=' ')
            else:
                print(' ',end=' ')
        print('')
printD(size,symbol)