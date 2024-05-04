import sys
number=input('Enter your number: ')
lengthOfNumber = len(number)
print(lengthOfNumber)
if number.startswith('+91') and lengthOfNumber==13:
    number=number.replace('+91','')
    print(number)
    lengthOfNumber=len(number)
    print(lengthOfNumber)
elif not lengthOfNumber==10:
    print('Invalid.')
    sys.exit()
if not number.isdigit():
    print('invalid')
    sys.exit()
print(number)