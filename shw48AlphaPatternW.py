rows = int(input('Enter the value of rows : ')) #3,5   4,7   5,9
column = rows*2-1#int(input('Enter the value of column : '))
symbol = input('Enter the symbol(character) : ')
def printD(rows,column,char):
    for row in range(rows):
        for col in range(column):
            if(col==0 or col==column-1 or col==column//2-row or col==column//2+row):
                print(char,end=' ')
            else:
                print(' ',end=' ')
        print('')
printD(rows,column,symbol)