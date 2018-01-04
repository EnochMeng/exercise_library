##main program

def repay():
    pass

def withdraw():
    pass

def transfer():
    pass



def interactive():
    pass


user_data={
    'account_id':None,
    'is_authentiacted':False,
    'account_data':None}


transaction_logger=logger.logger('transaction')

access_logger=logger.logger('access')

def run():
    acc_data=auth.acc_login(user_data,access_logger)
    
    if user_data['is_authentiacted']:
        user_data['account_data']=acc_data
        interactive(user_data)
##when the program called,implement user interaction logic
