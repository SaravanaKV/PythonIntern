'''
Write a program to continuously get firstname and last name of various students from the user.
Stop when the user's first name or last name starts with "Z".
'''

firstName=input('Enter the first name of the student 1 : ').capitalize()
lastName=input('Enter the last name of the student 1: ').capitalize()
print('Name of the student 1 is ',firstName+lastName)
i=2
while firstName[0]!='Z' and lastName[0]!='Z':
    firstName = input(f'Enter the first name of the student {i}: ').capitalize()
    lastName = input(f'Enter the last name of the student {i} : ').capitalize()
    print(f'Name of the student {i} is ',firstName+lastName)
    i+=1
