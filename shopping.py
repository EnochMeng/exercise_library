product=[
    ('TSLMO',5000),
    ('MAC BOOK',8000),
    ('COFFEE',120),
    ('IPHONE',5600),
    ('BICYLE',2200)
    ]
purchase=[]
saving=input('pls type your money:')
if saving.isdigit():
    saving=int(saving)
    while True:
        for i,v in enumerate(product,1):
            print(i,'.',v)
        num=input('pls type the number of product you want:')
        if num.isdigit():
            num=int(num)
            if num<=len(product) and num>=1:
                if saving>=product[num-1][1]:
                    saving-=product[num-1][1]
                    purchase.append(product[num-1])
                else:
                    print('your money is not enough!')
            else:
                print('sorry , the number is not exist!')                
        elif num=='quit':
            print('your balance:',
                  saving,
                  'your purchased commodity:')
            unique=set(purchase)
            for item in unique:
                print(item,' x',purchase.count(item))
            break
        else:
            print('pls type a number!')            
elif saving=='quit':
    print('welcome to your next visit!')
else:
    print('pls type a sum of money!')
