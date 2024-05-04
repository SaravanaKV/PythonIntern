'''
write a program to get the number of members in a family. Ask the user to enter the age of every member.
Display the number of major, minor and senior citizens. Stop the execution if age is above 110.
Note-All senior citizens are major.
'''

import sys
numberOfMember=int(input('Enter the number of member in the family: '))
if numberOfMember>10 or numberOfMember<2:
    print('Invalid input')
    sys.exit()
numberOfMajor=0
numberOfMinor=0
numberOfSeniorCitizen=0
for i in range(numberOfMember):
    age=int(input(f'Enter the age of member{i+1}: '))
    if age>110 or age<0:
        print('Invalid input')
        sys.exit()
    if age>=60:
        numberOfSeniorCitizen+=1
    elif age>=18:
        numberOfMajor+=1
    else:
        numberOfMinor+=1
print(f'Number of Minor in the family is {numberOfMinor}')
print(f'Number of Major in the family is {numberOfMajor}')
print(f'Number of SeniorCitizen in the family is {numberOfSeniorCitizen}')