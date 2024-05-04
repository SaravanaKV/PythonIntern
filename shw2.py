# accept a number and see if it ends with 0. use simple if statement


number=int(input('Enter the Number: '))
if number>9 and number%10==0:
    print('Given number is end with zero')
else:
    print('Given number is not end with zero')