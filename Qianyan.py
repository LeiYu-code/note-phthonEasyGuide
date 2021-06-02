passwordFile = open('secretPasswordFile.txt')  
secretPassword = passwordFile.read()
print('Enter your password:')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
if typedPassword == '12345':
    print('That password is one that an ideiot puts on their luggage.')
else:
    print('Access denied')  