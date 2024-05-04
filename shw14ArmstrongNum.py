''' Get input from user and check whether it is Armstrong number or not.
Armstrong numbers: 0 1 153 370 371 407 ...
'''
num=int(input('Enter the number: '))
sum=0
num1=num
while num1>0:
    sum+=((num1%10)**3)
    num1//=10
if sum==num:
    print(f'{num} is a armstrong number')
else:
    print(f'{num} is not a armstrong number')
