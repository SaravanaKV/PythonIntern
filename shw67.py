'''
Problem #5
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
'''

def operation(expression):
    inList=[]
    operatorList=[]
    for element in expression:
        if element in "+-*/":
            operatorList.append(element)
        else:
            inList.append(int(element))
            if len(inList) == 2:
                num2 = inList.pop()
                num1 = inList.pop()
                operator=operatorList.pop()
                if operator == '+':
                    inList.append(num1 + num2)
                elif operator == '-':
                    inList.append(num1 - num2)
                elif operator == '*':
                    inList.append(num1 * num2)
                elif operator == '/':
                    inList.append(num1 // num2)
    return inList.pop()
expression=["+","1", "2", "*", "5"]
result=operation(expression)
print(result)