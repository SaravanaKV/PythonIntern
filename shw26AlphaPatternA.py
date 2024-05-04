'''
      *
    * * *
  * * * * *
* * * * * * *
'''
rows= int(input('Enter the value of rows: ')) #3,5   4,7   5,9  6,11   7,13  8,15
column= int(input('Enter the value of column: '))
symbol=  input('Enter the symbol(character) : ')

def printA(rows,column,symbol):
    c = (column + 1) // 2
    r = (rows) // 2
    for row in range(rows+1):
        for col in range(1,column+1):
            if((row==row and(col==c-row or col==c+row)) or row==r and(col>c-row and col<c+row)):
                print(symbol,end=' ')
            else:
                print(' ',end=' ')
        print('')
printA(rows,column,symbol)