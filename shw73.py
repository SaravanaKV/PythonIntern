'''
problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint -
there are many simple answers. you can try with slice function
'''
def findSameStr():
num1=123456789
num2=987654321
pnum1=sorted(str(num1))
pnum2=sorted(str(num2))
if pnum1==pnum2:
    print(f'{num1} is same as {num2}')
else:
    print(f'{num1} is not same as {num2} ')