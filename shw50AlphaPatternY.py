size = int(input('Enter the length(size) you want : ')) # 3,5,7,9,11,,,,
symbol = input('Enter the symbol(character) : ')
def printD(size,char):
    for row in range(size):
        for col in range(size):
            if(((col==row or col==size-1-row) and row<size//2) or (col==size//2 and row>=size//2)):
                print(char,end=' ')
            else:
                print(' ',end=' ')
        print('')
printD(size,symbol)
'''
1 0 1
0 1 0
0 1 0

1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0

1 0 0 0 0 0 1
0 1 0 0 0 1 0
0 0 1 0 1 0 0
0 0 0 1 0 0 0
0 0 0 1 0 0 0
0 0 0 1 0 0 0 
0 0 0 1 0 0 0

1 0 0 0 0 0 0 0 1
0 1 0 0 0 0 0 1 0
0 0 1 0 0 0 1 0 0
0 0 0 1 0 1 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 0 1 0 0 0 0 
0 0 0 0 1 0 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 0 1 0 0 0 0
'''
