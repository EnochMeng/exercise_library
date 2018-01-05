##main program
from core import logger
from core import auth

user_data={
    'account_id':None,
    'is_authentiacted':False,
    'account_data':None}


transaction_logger=logger.logger('transaction')

access_logger=logger.logger('access')

def repay():
    pass

def withdraw():
    pass

def transfer():
    pass

def interactive(user_data):
    func_dic={
        '1': repay,
        '2': withdraw,
        '3': transfer
        }
    while True:
        for i in func_dic:
            print(i,'. ',func_dic['1'])
        choice = input('pls choose:')
        if choice in func_dic:
            func_dic[choice](user_data)
        else:
            print('maloperation!')

def run():
    acc_data=auth.acc_login(user_data,access_logger)
    
    if user_data['is_authentiacted']:
        user_data['account_data']=acc_data
        interactive(user_data)
##when the program called,implement user interaction logic
