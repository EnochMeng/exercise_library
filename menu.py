menu={'jiangsu':{'nanjin':['a','b','c'],
                 'yangzhou':['d','e','f'],
                 'suzhou':['g','h','i']},
      'zhejiang':{'hangzhou':['j','k','l'],
                  'ningbo':['m','n','o'],
                  'jinhua':['p','q','r']},
      'sichuan':{'chendu':['s','t','u'],
                 'wenchuan':['v','w','x'],
                 'mianyang':['y','z','ab']}}
province_list=[]
for i in menu.keys():
    province_list.append(i)
    
while True:
    for i,v in enumerate(province_list,1):
        print(i,'. ',v)
    num=input('pls type the menu num you choose:')
    if num.isdigit():
        num=int(num)
        if num>=1 and num<=len(province_list):
            city=menu[province_list[num-1]]
            city_list=[]
            for i in city.keys():
                city_list.append(i)
                
            while True:
                for i,v in enumerate(city_list,1):
                    print(i,'. ',v)
                num2=input('pls type the menu num you choose:')
                if num2.isdigit():
                    num2=int(num2)
                    town=city[city_list[num2-1]]
                    
                    while True:
                        for i,v in enumerate(town,1):
                            print(i,'. ',v)
                        num3=input('pls type q to return to the upper layer:')
                        if num3=='q':
                            break
                        else:
                            print('incorrect instruction')
                    
                elif num2=='q':
                    break
                else:
                    print('incorrect instruction')
        else:
            print('incorrect instruction')
    elif num=='q':
        break
    else:
        print('incorrect instruction')
