'''
Problem #3
Add two number represented in a list as reversed.
print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
explanation (321 + 765 = 1086)
'''
def ListToReversedNumber(list):
    revNum=0
    for i in range(len(list)):
        revNum+=list[i]*10**i
    return revNum
def Reverse(num):
    result=[]
    for digit in str(num):
        result.insert(0,int(digit))
    return result
list1=[1, 2, 3]
list2=[5, 6, 7]
num1=ListToReversedNumber(list1)
num2=ListToReversedNumber(list2)
num=num1+num2
print(Reverse(num))