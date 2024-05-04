rows=10
column=5
for i in range(column):
    for j in range(rows):
        if (i==0 and j==0) or (i==0 and j==9)or (i==4 and j==0)or (i==4 and j==9):
            print('A',end=' ')
        else:
            print(' ',end=' ')
    print('')