Problem #1
You have a list of numbers in ascending order, but with duplicates.
Remove the duplicated, append _ at the end for each duplicate removed
eg input = [1,2,3,3,3,4,4,7,7,9]
output = [1,2,3,4,7,9,_,_,_,_]

Problem #2
Same as above,but print the list in descending order
input = [1,2,3,3,3,4,4,7,7,9]
output = [9,7,4,3,2,1,_,_,_,_]

Problem #3
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)

Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop.
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.


Problem #5
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25