"""def add(a,b):
    sum=a+b
    print(sum)
add(2,4)
"""
n=int(input('Enter the number '))
sum=1
for i in range(1,n+1):
	sum*=i
print(sum)