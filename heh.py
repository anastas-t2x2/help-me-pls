import time

admin_password = 12345 #Для админов можно потом сделать как-нить отдельно создание пароля :) (через int(input()) само собой:) )
user_names = ['anastas', 'timon', 'chimin', 'bts']
name = None
attempt = 2

number_of_elements = len(user_names)
while name != '':   
    print('Hi!!! Enter your name.', "If you`re an administrator, write here 'admin'.", end='\n')
    name = input()
    if name == 'admin':
        print('Enter your password...')
        password = int(input())
        while attempt != 0:
            if password != admin_password:
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
                attempt = 2
    else:
        count = 0
        for i in range(0,number_of_elements):
            if name == user_names[count]:
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
                count += 1
                    