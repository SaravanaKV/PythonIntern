'''
Write a program to get input string from the user. Print all the capital letters as a string. Print all the small letters as a string.
Print all digits as a string. Print all the other characters as a string. So, totally 4 output strings.
Input: My pin code is 600045.
Outputs:
M
ypincodeis
600045
'''

str=input('Enter the string: ')
ALPHA=''
alpha=''
numeric=''
for i in str:
    if i.isalpha():
        if i.isupper():
            ALPHA=(ALPHA+i)
        else:
            alpha=(alpha+i)
    elif i.isdigit():
        numeric=(numeric+i)
print(ALPHA)
print(alpha)
print(numeric)
print(ALPHA+alpha+numeric)
print(str)