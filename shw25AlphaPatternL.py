rows=int(input('Enter the value of row: '))
colum=int(input('Enter the value of column: '))
for row in range(rows):
    for col in range(colum):
        if(col==0 or row==rows-1):
            print("*",end=' ')

        else:
            print(' ',end=' ')
    print('')