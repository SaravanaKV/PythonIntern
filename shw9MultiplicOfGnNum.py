# 1.Write a program to print multiplication tables of the number given by user. Do not accept negative values from the user.

import sys
num=int(input('Enter the number(multiplier): '))
Range=int(input('Enter the range(multiplicand): '))
if num<0:
    print('number must be positive')
    sys.exit()
for i in range(1,Range+1):
    print(i, 'x', num, '=', i*num)