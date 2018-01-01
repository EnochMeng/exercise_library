with open('name_password.txt','r') as f:
    name_password=f.read()
name_password=eval(name_password)

with open('count.txt','r') as f:
    i=int(f.read())
if i>=3:
    print('your account is blocked')
    exit()
    
name=input('pls enter your name:')

if name in name_password:
    correct_password=name_password[name]
    flag=True
    while flag:
        password=input('pls enter your password:')
        if password!=correct_password:
            print('incorrect password')
            i+=1
            if i>=3:
                with open('count.txt','w') as f:
                    i=str(i)
                    f.write(i)
                exit()
        else:
            print('welcome')
            flag=False
            
        
else:
    print('the name is not exist')
