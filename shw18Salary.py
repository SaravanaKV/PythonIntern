############## Problem  3  ####################
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000.
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones
# this month also, then he gets additional Rs5000.
additionalBonus=0
monthlySalary=int(input('Enter the monthly salary of your: '))
numberOfPhoneSold=int(input('Enter the number phones sold: '))
if numberOfPhoneSold>=20 and monthlySalary>=20000:
    additionalBonus=5000
if numberOfPhoneSold>=5:
    salaryWithBonusForFirst5Phones=5000
    numberOfPhoneSold-=5
    salaryWithBonusFor1100PerPhone=numberOfPhoneSold*1100
totalsalary=monthlySalary+salaryWithBonusForFirst5Phones+salaryWithBonusFor1100PerPhone+additionalBonus
print(f'Total salary for this month is {totalsalary}')

