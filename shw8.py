'''1. Write a program to print multiplication tables of the number given by user. Do not accept negative values from the user.
Write a program to print fibonacci series of the number given by the user.
'''
import sys
num=int(input('Enter the number: '))
if num<0:
    sys.exit()
for i in range(1,10):
    print(i,'x',num = i*num),end=('')
