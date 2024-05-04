import sys
email=input('Enter your email Id: ')
#saro458592@gmail.com
lengthOfEmail=len(email)
if lengthOfEmail<10:
    print('Email must be more than 10 characters')
    sys.exit()
if '@' not in email or '.' not in email:
    print('Invalid id. Email does not contain @ or .')
    sys.exit()
print(email)
splitedGmail=email.split('@')
print(splitedGmail)
userName=splitedGmail[0]
if not userName.isalnum():
    sys.exit()
print(userName)
lastPortion =splitedGmail[1]
print(lastPortion)
splitedLPOEmail=lastPortion.split('.')
print(splitedLPOEmail)
domainName=splitedLPOEmail[0]
if not domainName.isalpha():
    print('Domain name must be alphabert')
    sys.exit()
print(domainName)
extension=splitedLPOEmail[1]
lengthOfExtension=len(extension)
if not lengthOfExtension<=3:
    print('length of extension must be less tha 3 characters')
    sys.exit()
print(extension)
print(email)