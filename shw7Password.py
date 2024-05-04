import sys
password=input('Enter the password: ')
lengthOfPassword=len(password)
if lengthOfPassword<8:
    print('password is too small')
    sys.exit()
numberOfAlphabet=0
numberOfNumeric=0
numberOfSpecialCharacter=0
for i in password:
    if i.isalpha():
        numberOfAlphabet+=1
    elif i.isdigit():
        numberOfNumeric+=1
    else:
        numberOfSpecialCharacter+=1
print('Number of Alphabet ',numberOfAlphabet)
print('Number of numeric ',numberOfNumeric)
print('Number of specialcharacter ',numberOfSpecialCharacter)