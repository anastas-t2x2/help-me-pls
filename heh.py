a = ['anastas', 'timon', 'chimin', 'bts']
name = None
while name != '':   
    print('Hi!!! Enter your name.', "If you`re an administrator, write here 'admin'.", end='\n')
    name = input()
    if name == 'admin':
        print('Enter your password...')
        pw = int(input())
        while pw != 12345:
            print('Wrong!')
            break
        else:
            print('welcome. Here is your list.')
            print(a)
            break
    else:
        print('Hi')
        a.append(name)
        break
        