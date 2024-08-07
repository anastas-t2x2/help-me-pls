import time
user_names = ['anastas', 'timon', 'chimin', 'bts']
name = None
admin_credentials = {'admin' : "12345",
                     'alex' : "abc", 
                     'timati' : "00000"} #и не взломать

def process_admin(name,attempt,timeout_sec):
    password = input('Write your password...')
    while attempt != 0:
        if password != admin_credentials[name]:
            print('Wrong, try again!')
            attempt -= 1
            password = input()
        else:
            print('welcome. Here is your list.')
            print(user_names)
            break
    else:
        print('Stop!!! You can try again only in')
        for i in range(timeout_sec,0,-1):
            print(i)
            time.sleep(1)

def process_user(name):
    if name in user_names:
        print('Would you like to delete yourself? Enter "Yes" or "No".')
        say = input()
        if say == 'Yes':
            user_names.remove(name)
            print('Done.')
        else:
            print('OK')
    else:
        user_names.append(name)

while name != '':   
    print('Hi!!! Enter your name. \nIf you`re an administrator, write here something from the following list... (your own login)', list(admin_credentials.keys()))
    name = input()
    if name in admin_credentials:
        process_admin(name = name,attempt=3,timeout_sec=5)
    else:
        process_user(name)
                    