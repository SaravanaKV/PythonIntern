num=int((input('Enter the number: ')))
SumOfOdd=0
SumOfEven=0
ispositive=True
if num<0:
    num*=-1
    ispositive=False
while(num>0):
    num1=num%10
    if num1%2==1:
        SumOfOdd+=num1
    else:
        SumOfEven+=num1
    num//=10
if ispositive==True:
    print(f'Sum of odd number is {SumOfOdd}\nSum of even number is {SumOfEven}')
else:
    print(f'Sum of odd number is {SumOfOdd*-1}\nSum of even number is {SumOfEven*-1}')
