##load or dump account info
import json,os
from core import db_handle
from conf import settings

def load_account_data(account_data):
    
    db_path=db_handle.db_handler(settings.DATABASE)
    print(os.path.join(db_path,account_data['account_id']))
    with open(os.path.join(db_path,account_data['account_id']),'r') as f:
        account_data = json.load(f)
    return account_data

def dump_account_data(account_data):

    db_path=db_handle.db_handler(settings.DATABASE)
    with open(os.path.join(db_path,account_data['account_id']),'w') as f:
        json.dump(account_data,f)
