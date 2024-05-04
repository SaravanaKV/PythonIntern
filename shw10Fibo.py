# Write a program to print fibonacci series of the number given by the user.

num=int(input('Enter the number: '))
fibonacciSeries=[0,1]
while fibonacciSeries[-1]+fibonacciSeries[-2]<=num:
    fibonacciSeries.append(fibonacciSeries[-2]+fibonacciSeries[-1])
print('Fibonacci series upto',num,'is: ',fibonacciSeries)