############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.

moneyNeeded=1000
totalAmount=0
for i in range(1,6):
    moneyFromParent=int(input('Enter the money given by parent: '))
    if moneyFromParent>=10:
        totalAmount += moneyFromParent
        print('Thank you')
        print(f'Totally I have {totalAmount} Rupees')
    if totalAmount>=moneyNeeded:
        break

