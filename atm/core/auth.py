##use the auth method to confirm user
import json


def auth(account,password):
    db_path=os.path.join(settings.BASE_DIR,)

def acc_login(user_data,log_obj):
    retry=0
    while user_data['is_authentited'] is not True and retry<3:
        account=input('ACCOUNT:')
        password=input('PASSWORD:')
        auth(account,password)
    
