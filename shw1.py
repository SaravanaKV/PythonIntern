'''1. Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name.
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'.

2. The user just bought a few things in your  shop. Ask the user what he bought. 
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype'''

#problem no 1

name = input('Enter your name: ').strip()
yearOfBirth = int(input('Enter your year of birth: '))
print('Hello '+name)
print('You are %d years old'%(2024-yearOfBirth))

#problem no 2

print('\n')
vadaiCost = 30
sodaCost = 20
sandwichCost =100
#Ask user what they bought
vadaiQuantity = int(input('Enter the Quantity of vadai: '))
sodaQuantity = int(input('Enter the Quantity of soda: '))
sandwichQuantity = int(input('Enter the Quantity of sandwich: '))
totalCost = ((vadaiCost*vadaiQuantity)+(sodaCost*sodaQuantity)+(sandwichCost*sandwichQuantity))
print('Total cost is ',totalCost)
userPayment = float(input('Enter the amount from the user: '))
print('Balance to be give: %2.f'%(userPayment-totalCost))