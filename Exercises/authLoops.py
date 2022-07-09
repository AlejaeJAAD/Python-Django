password = '12345'
pw = ''
auth = False
count = 0
max_attempt = 3

while pw != password:
    count = count + 1
    if count > max_attempt:
        break
    pw = input(f'{count} What is the password? ')
    print('Wrong, try again' if pw != password else 'You in')
else:
    auth = True

print('Authorized' if auth else 'Account locked')