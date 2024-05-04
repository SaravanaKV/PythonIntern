size = int(input('Enter the length(size) you want : '))
def printD(size,char):
    for row in range(size):
        for col in range(size):
            if(col==0 or((row==0 or row==size-1) and col!=size-1) or (col==size-1 and(row!=0 and row!=size-1))):
                print(char,end=' ')
            else:
                print(' ',end=' ')
        print('')
    print('')

siz = int(input('Enter the length(size) you want : '))
symbol = input('Enter the symbol(character) : ')
def printSD(siz,cha):
    for row in range(siz):
        for col in range(siz):
            if(col==0 or((row==0 or row==siz-1) and col!=siz-1) or (col==siz-1 and(row!=0 and row!=siz-1))):
                print(cha,end=' ')
            else:
                print(' ',end=' ')
        print('')
    print('')
printD(size,symbol)
printSD(siz,symbol)
printD(size,symbol)