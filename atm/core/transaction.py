#make transaction
from conf import settings
from core import account

def make_transaction(transaction_logger,account_data,transaction_type,amount):
    amount = float(amount)
    if transaction_type in settings.TRANSACTION_TYPE:
        interest = float(settings.TRANSACTION_TYPE[transaction_type]['interest'])*amount
        old_balance = float(account_data['balance'])
        if settings.TRANSACTION_TYPE[transaction_type]['action'] == 'plus':
            new_balance = old_balance + amount - interest
            
        else:
            settings.TRANSACTION_TYPE[transaction_type]['action'] == 'minus'
            new_balance = old_balance - amount - interest
            
            if new_balance < 0:
                print('your balance is not enough!')
                return


        account_data['balance'] = new_balance
        
        account.dump_account_data(account_data)
        
        transaction_logger.info('account_id:%s  operation:%s  amount:%s  interest:%s'%(account_data['account_id'],transaction_type,amount,interest))

        return new_balance
    
    else:
        print('incorrect transaction type!')
        

    
    
