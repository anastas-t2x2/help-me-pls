import time
user_names = ['anastas', 'timon', 'chimin', 'bts']
name = None
admin_credentials = {'admin' : 12345,
                     'alex' : 54321, 
                     'timati' : 00000} #и не взломать

def process_admin(name,attempt):
    password = int(input('Write your password...'))
    while attempt != 0:
        if password != admin_credentials[name]:
            print('Wrong, try again!')
            attempt -= 1
            password = int(input())
        else:
            print('welcome. Here is your list.')
            print(user_names)
            break
    else:
        print('Stop!!! You can try again only in')
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)

def process_user():
    for i in range(0,number_of_elements):
        if name == user_names[i]:
            print('Would you like to delete yourself? Enter "Yes" or "No".')
            say = input()
            if say == 'Yes':
                user_names.remove(name)
                print('Done.')
                break
            else:
                print('OK')
                break
        else:
            user_names.append(name)

number_of_elements = len(user_names)
while name != '':   
    print('Hi!!! Enter your name. \nIf you`re an administrator, write here something from the following list... (your own login)', list(admin_credentials.keys()))
    name = input()
    if name in admin_credentials:
        process_admin(name = name,attempt=3)
    else:
        process_user()
                    