##main program
import collections
from core import logger
from core import auth
from core import transaction
from core import account

user_data={
    'account_id':None,
    'is_authentiacted':False,
    'account_data':None}


transaction_logger=logger.logger('transaction')

access_logger=logger.logger('access')

def repay(user_data):

    account_data = account.load_account_data(user_data)
    
    current_balance = account_data['balance']
    print('balance:%s'%current_balance)
    flag = True
    while flag:
        repay_amount = input('pls enter your amount(q:return main menu):').strip()
        if repay_amount.isdigit() and len(repay_amount) > 0:
            new_balance = transaction.make_transaction(transaction_logger,account_data,'repay',repay_amount)
            if new_balance:
                
                print('success,balance: %f'%new_balance)
                flag = False
        elif repay_amount == 'q':
            flag = False                  

        else:
            print('error!')    
    

def withdraw():
    pass

def transfer():
    pass

def logout(user_data):
    access_logger.info('%s logout'%user_data['account_id'])
    exit()
    

def interactive(user_data):
    func_dic={
        '1': repay,
        '2': withdraw,
        '3': transfer,
        '4': logout
        }
    
    func_dic_view=[('1','repay'),('2','withdraw'),('3','transfer'),('4','logout')]
    func_dic_view=collections.OrderedDict(func_dic_view)
    
    while True:
        for i in func_dic_view:
            print(i,'. ',func_dic_view[i])
        choice = input('pls choose:')
        if choice in func_dic:
            func_dic[choice](user_data)
        else:
            print('maloperation!')

def run():
    acc_data=auth.acc_login(user_data,access_logger)
    
    if user_data['is_authentiacted']:
        user_data['account_data'] = acc_data
##        print(user_data)
        
        interactive(user_data)
##when the program called,implement user interaction logic
