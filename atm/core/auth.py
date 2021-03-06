##use the auth method to confirm user
import json,time,os
from core import db_handle
from conf import settings

def auth(account,password,log_obj):
    db_path=db_handle.db_handler(settings.DATABASE)
##    print(db_path)
    user_file=r'%s.json'%os.path.join(db_path,account)
##    print(user_file)
    if os.path.isfile(user_file):
        
        with open(user_file) as f:
            account_data=json.load(f)
        if password==account_data['password']:
            
            if time.strftime('%Y-%m-%d',time.localtime()) < account_data['expire_time']:

                log_obj.info('%s login'%account_data['account_id'])
                
                return account_data
            else:
                print('your card is expired!')
        else:
            print('incorrect password!')
    else:
        print('the account is not exist!')


def acc_login(user_data,log_obj):
    retry=0
    while user_data['is_authentiacted'] is not True and retry < 3:
        account=input('ACCOUNT:')
        password=input('PASSWORD:')
        acc_data = auth(account,password,log_obj)
        if acc_data:
            user_data['is_authentiacted'] = True
            user_data['account_id'] = account
            return acc_data
        retry+=1
        
    else:
        log_obj.error('logging many times!')
        exit()

