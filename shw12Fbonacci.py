#number of iteration
num=int(input('Enter the number: '))
num1=0
num2=1
print(f'{num} number of iteration')
print(num1,num2,end=' ')
for i in range(2,num):
    temp=num2
    num2+=num1
    num1=temp
    print(num2,end=' ')

#Upto that number
print(f'\nUpto {num}')
num1=0
num2=1
print(num1,num2,end=' ')
for i in range(2,num):
        temp=num2
        num2+=num1
        num1=temp
        if num2>num:
            break
        print(num2,end=' ')