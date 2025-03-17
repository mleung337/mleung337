# Matthew Leung

# Variables with dictionaries containing usernames and passwords
user1 = {'username':'Etwaroo', 'password':'123456789'}
user2 = {'username':'Foti', 'password':'987654321'}
user3 = {'username':'Papadatos', 'password':'543219876'}
user4 = {'username':'Trembly', 'password':'9058899696'}
user5 = {'username':'Leung', 'password':'335772380'}
user_list = [user1, user2, user3, user4, user5]
login_attempt = 0
login_valid = False

while True:
    username = input('\nEnter your username here. ')
    password = input('Enter your password here. ')

    for user in user_list:
        
        if username == user['username'] and password == user['password']:
            print(f'\nWelcome, {user["username"]}.')
            login_valid = True
            raise SystemExit

        elif login_attempt == 2:
            print('\nToo many attempts. Quitting...')
            raise SystemExit

        elif username != user_list[-1]['username'] and password != user_list[-1]['password']:
            print('\nInvalid password or username.')
            login_attempt += 1
            break

    continue
