''' Write a program to get first name, last name, age, phone number and email id from the user. Validate all the inputs and print the user information in a readable manner.
User's name must be printed in capital letters (or first letter should be capital). Phone number must contain 10 digits and no alphabets. Email id must contain a dot and @. Age must be a valid number.
Think of all possible ways to validate the inputs.'''

firstName= input('Enter your first name: ').strip()
if len(firstName<3):
lastName= input('Enter your last name: ')
age= int(input('Enter your age: '))
number= input('Enter the phone number: ')
email= input('Enter your email_ID')
