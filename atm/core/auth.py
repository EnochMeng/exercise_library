##use the auth method to confirm user
import json,time,os
from core import db_handle
from conf import settings

def auth(account,password):
    db_path=db_handle.db_handler(settings.DATABASE)
    print(db_path)
    user_file=os.path.join(db_path,account)
    print(user_file)
    if os.path.isfile(user_file):
        
        with open(os.path.join(db_path,account)) as f:
            account_data=json.load(f)
        if password==account_data['password']:
            
            if time.strftime('%Y-%m-%d',time.localtime()) < account_data['expire_time']:
                print('welcome!')
                user_data['is_authentiacted'] = True
                return user_data['is_authentiacted'],account_data
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
        user_data['is_authentiacted'],acc_data = auth(account,password)
        retry+=1
    return acc_data

