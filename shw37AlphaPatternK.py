rows = int(input('Enter the value of rows : ')) #3,3   5,4   7,5   9,6   11,7   13,8
column = int(input('Enter the value of column : '))
symbol = input('Enter the symbol(character) : ')
def printD(rows,column,char):
    for row in range(rows):
        for col in range(column):
            if(col==0 or col==column-row-1 or col==row-column+3):
                print(char,end=' ')
            else:
                print(' ',end=' ')
        print('')
printD(rows,column,symbol)
'''
1 0 0 0 1
1 0 0 1 0 
1 0 1 0 0
1 1 0 0 0
1 0 1 0 0
1 0 0 1 0
1 0 0 0 1

1       1
1     1
1   1
1 1
1   1
1     1
1       1

1 0 0 0 0 0 1
1 0 0 0 0 1 0
1 0 0 0 1 0 0
1 0 0 1 0 0 0
1 0 1 0 0 0 0
1 1 0 0 0 0 0
1 0 1 0 0 0 0
1 0 0 1 0 0 0
1 0 0 0 1 0 0
1 0 0 0 0 1 0
1 0 0 0 0 0 1

0           0
0         0 
0       0 
0     0 
0   0 
0 0 
0   0 
0     0
0       0 
0         0 
0           0

1 0 0 0 0 0 0 1
1 0 0 0 0 0 1 0
1 0 0 0 0 1 0 0
1 0 0 0 1 0 0 0
1 0 0 1 0 0 0 0
1 0 1 0 0 0 0 0
1 1 0 0 0 0 0 0
1 0 1 0 0 0 0 0
1 0 0 1 0 0 0 0
1 0 0 0 1 0 0 0
1 0 0 0 0 1 0 0
1 0 0 0 0 0 1 0
1 0 0 0 0 0 o 1

o             0
0           0
0         0 
0       0 
0     0 
0   0 
0 0 
0   0 
0     0
0       0 
0         0 
0           0
0             0
'''