'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop.
Parse the input list one element at a time. Convert to integer, push it to a stack.
Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.
'''
def operation(expression):
    inList=[]
    for element in expression:
        if element in "+-*/":
            num2=inList.pop()
            num1=inList.pop()
            if element=='+':
                inList.append(num1+num2)
            elif element=='-':
                inList.append(num1-num2)
            elif element=='*':
                inList.append(num1*num2)
            elif element=='/':
                inList.append(num1//num2)
        else:
            inList.append(int(element))
    return inList.pop()
expression=["10", "2", "3", "+","-", "5", "*"]
result=operation(expression)
print(result)