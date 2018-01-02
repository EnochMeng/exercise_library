##menu={'jiangsu':{'nanjin':['a','b','c'],
##                 'yangzhou':['d','e','f'],
##                 'suzhou':['g','h','i']},
##      'zhejiang':{'hangzhou':['j','k','l'],
##                  'ningbo':['m','n','o'],
##                  'jinhua':['p','q','r']},
##      'sichuan':{'chendu':['s','t','u'],
##                 'wenchuan':['v','w','x'],
##                 'mianyang':['y','z','ab']}}
##province_list=[]
##for i in menu.keys():
##    province_list.append(i)
##    
##while True:
##    for i,v in enumerate(province_list,1):
##        print(i,'. ',v)
##    num=input('pls type the menu num you choose:')
##    if num.isdigit():
##        num=int(num)
##        if num>=1 and num<=len(province_list):
##            city=menu[province_list[num-1]]
##            city_list=[]
##            for i in city.keys():
##                city_list.append(i)
##                
##            while True:
##                for i,v in enumerate(city_list,1):
##                    print(i,'. ',v)
##                num2=input('pls type the menu num you choose:')
##                if num2.isdigit():
##                    num2=int(num2)
##                    town=city[city_list[num2-1]]
##                    
##                    while True:
##                        for i,v in enumerate(town,1):
##                            print(i,'. ',v)
##                        num3=input('pls type q to return to the upper layer:')
##                        if num3=='q':
##                            break
##                        else:
##                            print('incorrect instruction')
##                    
##                elif num2=='q':
##                    break
##                else:
##                    print('incorrect instruction')
##        else:
##            print('incorrect instruction')
##    elif num=='q':
##        break
##    else:
##        print('incorrect instruction')


##use new simple method to implement this function,it is perfect i think
import json
f=open('menu.txt','r')
menu=json.loads(f.read())
##print(type(menu))
f.close()
##menu={'jiangsu':{'nanjin':{'a':{},'b':{},'c':{}},
##                 'yangzhou':{'d':{},'e':{},'f':{}},
##                 'suzhou':{'g':{},'h':{},'i':{}}},
##      'zhejiang':{'hangzhou':{'j':{},'k':{},'l':{}},
##                  'ningbo':{'m':{},'n':{},'o':{}},
##                  'jinhua':{'p':{},'q':{},'r':{}}},
##      'sichuan':{'chendu':{'s':{},'t':{},'u':{}},
##                 'wenchuan':{'v':{},'w':{},'x':{}},
##                 'mianyang':{'y':{},'z':{},'ab':{}}}}

current_layer=menu
upper_layer=[]
while True:
    for i in current_layer:
        print(i)
    choice=input('pls type the name your choose:')
    
    if choice.strip() in current_layer:
##        try:
        upper_layer.append(current_layer)
        current_layer=current_layer[choice]
##---            
        if current_layer=={}:
            print('this is last layer,none')
                
##        except TypeError:
##            upper_layer.pop()
##            print('this is last layer')

##---add new function 'add,revise,delete menu'---
    elif choice.strip()=='add':
        user_add=input('pls enter the name you want to add:')
        current_layer[user_add]={}
        
    elif choice.strip()=='revise':
        user_revise=input('pls enter name you want to revise:')
        if user_revise in current_layer:
            user_revise_after=input('pls enter the new name:')
            current_layer[user_revise_after]=current_layer.pop(user_revise)
        else:
            print('the name is not exist')
    
    elif choice.strip()=='delete':
        user_delete=input('pls enter name you want to delete:')
        if user_delete in current_layer:
            current_layer.pop(user_delete)
        else:
            print('the name is not exist')
        
    elif choice.strip()=='return':
        if upper_layer==[]:
            print('this is the uppest layer')
        else:
            current_layer = upper_layer.pop()
        
    elif choice.strip()=='quit':
        if upper_layer!=[]:
            f=open('menu.txt','w')
            f.write(json.dumps(upper_layer[0]))
            f.close()
        break
    else:
        print('incorrect name!')


##m={'a','b'}
##if m['a']:
##    print('h')
##else:
##    print('n')
    
    
        
